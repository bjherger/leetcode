"""Attention model for IMDB sentiment (sequence + tabular features)."""
import torch
import torch.nn as nn


class AttentionModel(nn.Module):
    """Embedding + MultiheadAttention + mean pool; concat tabular; classifier."""

    def __init__(
        self,
        vocab_size: int,
        embedding_dim: int,
        hidden_dim: int,
        output_dim: int,
        num_heads: int = 4,
        num_tabular_features: int = 2,
    ):
        super().__init__()
        if embedding_dim % num_heads != 0:
            raise ValueError("embedding_dim must be divisible by num_heads")
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.attention = nn.MultiheadAttention(embedding_dim, num_heads, batch_first=True)
        combined_dim = embedding_dim + num_tabular_features
        self.fc = nn.Sequential(
            nn.Linear(combined_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, text: torch.Tensor, tabular: torch.Tensor):
        # text: (batch, seq_len), tabular: (batch, num_tabular_features)
        embedded = self.embedding(text)  # (batch, seq_len, emb_dim)
        attn_out, _ = self.attention(embedded, embedded, embedded)  # (batch, seq_len, emb_dim)
        pooled = attn_out[:, -1, :]  # (batch, emb_dim) — last token hidden state
        combined = torch.cat([pooled, tabular], dim=1)  # (batch, emb_dim + num_tabular)
        return self.fc(combined)
