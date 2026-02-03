"""Configuration for IMDB attention model."""
import torch

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Training
batch_size = 64
epochs = 3
learning_rate = 1e-3

# Text / vocab
max_vocab_size = 20_000
max_seq_len = 256

# Model
embedding_dim = 128
hidden_dim = 128
num_heads = 4
output_dim = 2  # binary sentiment
num_tabular_features = 2  # log1p(num_tokens), log1p(num_unique_tokens)

# Data subset (for quick runs; set to None for full dataset)
train_subset_size = 2000
test_subset_size = 500
