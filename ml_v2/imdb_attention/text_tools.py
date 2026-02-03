"""Tokenization and vocabulary for IMDB text."""
from collections import Counter


def tokenize(text: str) -> list[str]:
    """Split text into lowercase word tokens, normalizing <br />."""
    return text.lower().replace("<br />", " ").split()


def build_vocab(train_ds, max_vocab_size: int) -> dict[str, int]:
    """Build word -> id vocabulary from training dataset. Includes <pad>=0, <unk>=1."""
    word_counts: Counter = Counter()
    for example in train_ds:
        word_counts.update(tokenize(example["text"]))
    vocab = {"<pad>": 0, "<unk>": 1}
    for w, _ in word_counts.most_common(max_vocab_size - 2):
        vocab[w] = len(vocab)
    return vocab


def text_to_ids(text: str, vocab: dict[str, int], max_seq_len: int) -> list[int]:
    """Convert text to list of token ids, truncating to max_seq_len."""
    tokens = tokenize(text)[:max_seq_len]
    unk_id = vocab["<unk>"]
    return [vocab.get(t, unk_id) for t in tokens]
