
import torch
import torch.nn.functional as F
from torch.nn.functional import relu
from torch import nn
from dnadna.nets import Network

class MyCNN(Network):
    def __init__(self, n_features, n_outputs):
        super().__init__()
        self.conv1 = nn.Conv2d(1, n_features, kernel_size=3, stride=2, bias=False)
        self.bn1 = nn.BatchNorm2d(n_features)
        self.pool = nn.MaxPool2d(2, 2)

        self.conv2 = nn.Conv2d(n_features, 20, kernel_size=3, stride=2, bias=False)
        self.pool2 = nn.MaxPool1d(1, 2)
        self.fc1 = nn.Linear(480, 5)  # constraint for 400 snp and 50 indiv.
        self.fc2 = nn.Linear(5, n_outputs)

    def forward(self, x):
        batch_size = x.size(0)
        print(x.size(0))
        x = x.unsqueeze(1)
        x = self.pool(relu(self.conv1(x)))
        x = self.bn1(x)
        x = self.pool(relu(self.conv2(x)))
        x = x.view(batch_size, -1)  # flatten the tensor for each batch element
        x = self.pool2(x)
        x = relu(self.fc1(x))
        x = self.fc2(x)
        return x
