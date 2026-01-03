import torch, torch.nn as nn


class LSTM(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(1, 50)
        self.fc = nn.Linear(50, 1)


    def forward(self, x):
        o, _ = self.lstm(x)
        return self.fc(o[-1])