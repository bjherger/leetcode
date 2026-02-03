"""Train and evaluate IMDB sentiment model. Run: python ml_v2/imdb_attention/main.py (from repo root)"""
import sys
from pathlib import Path

# Allow running as script: python ml_v2/imdb_attention/main.py
_pkg_dir = Path(__file__).resolve().parent
if str(_pkg_dir) not in sys.path:
    sys.path.insert(0, str(_pkg_dir))

import torch
import torch.nn as nn
import torch.optim as optim

import config
import data_loader
import model


def train_epoch(model, loader, loss_fn, optimizer):
    model.train()
    total_loss, n = 0.0, 0
    for inputs, tabular, labels in loader:
        inputs = inputs.to(config.device)
        tabular = tabular.to(config.device)
        labels = labels.to(config.device)
        optimizer.zero_grad()
        logits = model(inputs, tabular)
        loss = loss_fn(logits, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        n += 1
    return total_loss / n if n else 0.0


def test_epoch(model, loader, loss_fn):
    model.eval()
    total_loss, correct, n = 0.0, 0, 0
    with torch.no_grad():
        for inputs, tabular, labels in loader:
            inputs = inputs.to(config.device)
            tabular = tabular.to(config.device)
            labels = labels.to(config.device)
            logits = model(inputs, tabular)
            total_loss += loss_fn(logits, labels).item()
            correct += (logits.argmax(1) == labels).sum().item()
            n += labels.size(0)
    return total_loss / len(loader) if loader else 0.0, correct / n if n else 0.0


def main():
    train_ds, test_ds = data_loader.load_imdb()
    print(f"Train: {len(train_ds)}, Test: {len(test_ds)}")

    train_loader, test_loader, vocab_size = data_loader.build_train_test_loaders(train_ds, test_ds)

    net = model.AttentionModel(
        vocab_size=vocab_size,
        embedding_dim=config.embedding_dim,
        hidden_dim=config.hidden_dim,
        output_dim=config.output_dim,
        num_heads=config.num_heads,
        num_tabular_features=config.num_tabular_features,
    ).to(config.device)

    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr=config.learning_rate)

    for epoch in range(config.epochs):
        train_loss = train_epoch(net, train_loader, loss_fn, optimizer)
        test_loss, test_acc = test_epoch(net, test_loader, loss_fn)
        print(f"Epoch {epoch+1}  train_loss={train_loss:.4f}  test_loss={test_loss:.4f}  test_acc={test_acc:.2%}")
    print("Done!")


if __name__ == "__main__":
    main()
