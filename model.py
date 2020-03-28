import torch
from torch import nn
from torch.nn import functional as F

class WaveStyleNet(nn.Module):
    def __init__(self):
        pass
    
    """
    Forward step
    Args:
        inputs (Tensor): One-hot encoded audio signal, shape (Batch x Time)
    """
    def forward(self, inputs):
        # inputs [batch, time]
        x = self.embedding(inputs).transpose(1,2)
        # x [batch, feature, time]
        