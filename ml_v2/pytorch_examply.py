import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Constants
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load data
iris = datasets.load_diabetes()
batch_size = 64
epochs = 10

data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Define model (diabetes: 10 features, regression)
class NeuralNetwork(nn.Module):
    def __init__(self, in_features=10, out_features=1):
        super().__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(in_features, 512),
            nn.ReLU(),
            nn.Linear(512, out_features),
        )

    def forward(self, x):
        return self.linear_relu_stack(x)

model = NeuralNetwork().to(device)
print(model)

# Set up data loader
train_dataset = TensorDataset(
    torch.from_numpy(X_train).float(),
    torch.from_numpy(y_train).float().unsqueeze(1),
)
test_dataset = TensorDataset(
    torch.from_numpy(X_test).float(),
    torch.from_numpy(y_test).float().unsqueeze(1),
)
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

# Train model
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=1e-3)

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()   
        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
    num_batches = len(dataloader)
    model.eval()
    test_loss = 0.0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
    test_loss /= num_batches
    print(f"Test MSE: {test_loss:>8f}\n")

for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)
print("Done!")
# Run inference on test
X_test_tensor = torch.from_numpy(X_test).float().to(device)
y_test_tensor = torch.from_numpy(y_test).float().unsqueeze(1).to(device)
pred = model(X_test_tensor)
print(pred)

# Generate metrics on test set
mse = loss_fn(pred, y_test_tensor)
print(f"Test MSE: {mse:>8f}\n")
print(f"constants used. batch size: {batch_size}, epochs: {epochs}")