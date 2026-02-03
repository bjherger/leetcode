"""IMDB data loading, dataset, and dataloaders."""
import math
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

import config
import text_tools


def load_imdb():
    """Load IMDB train and test splits from Hugging Face datasets."""
    try:
        from datasets import load_dataset
    except ImportError:
        raise ImportError("Install Hugging Face datasets: pip install datasets")
    ds = load_dataset("imdb", split=None)
    return ds["train"], ds["test"]


def _tabular_features(ids: list[int]) -> tuple[float, float]:
    """Return (log1p(num_tokens), log1p(num_unique_tokens)) for scale."""
    n_tok = len(ids)
    n_uniq = len(set(ids))
    return (math.log1p(n_tok), math.log1p(n_uniq))


class IMDBDataset(Dataset):
    """PyTorch Dataset: (token_ids, tabular_features, label) per example."""

    def __init__(self, hf_ds, vocab: dict[str, int], max_seq_len: int):
        self.data = []
        for example in hf_ds:
            ids = text_tools.text_to_ids(example["text"], vocab, max_seq_len)
            tab = _tabular_features(ids)
            self.data.append((ids, tab, example["label"]))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        ids, tab, label = self.data[i]
        return (
            torch.tensor(ids, dtype=torch.long),
            torch.tensor(tab, dtype=torch.float32),
            torch.tensor(label, dtype=torch.long),
        )


def collate(batch):
    """Pad sequences; return (padded_ids, tabular [B, 2], labels)."""
    ids = [b[0] for b in batch]
    tabular = torch.stack([b[1] for b in batch])
    labels = torch.stack([b[2] for b in batch])
    padded = nn.utils.rnn.pad_sequence(ids, batch_first=True, padding_value=0)
    return padded, tabular, labels


def build_train_test_loaders(train_ds, test_ds):
    """Build vocab from train_ds, create datasets and dataloaders. Returns (train_loader, test_loader, vocab_size)."""
    vocab = text_tools.build_vocab(train_ds, config.max_vocab_size)
    vocab_size = len(vocab)

    n_train = getattr(config, "train_subset_size", None)
    n_test = getattr(config, "test_subset_size", None)
    train_subset = (
        train_ds.select(range(min(n_train, len(train_ds)))) if n_train is not None else train_ds
    )
    test_subset = (
        test_ds.select(range(min(n_test, len(test_ds)))) if n_test is not None else test_ds
    )

    train_dataset = IMDBDataset(train_subset, vocab, config.max_seq_len)
    test_dataset = IMDBDataset(test_subset, vocab, config.max_seq_len)

    train_loader = DataLoader(
        train_dataset,
        batch_size=config.batch_size,
        shuffle=True,
        collate_fn=collate,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=config.batch_size,
        collate_fn=collate,
    )
    return train_loader, test_loader, vocab_size
