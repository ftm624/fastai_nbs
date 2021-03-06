
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/03_minibatch_training.ipynb

from exp.nb_02 import *

import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.utils.data import DataLoader, SequentialSampler, RandomSampler

def accuracy(yh, y): return (torch.argmax(yh, dim=1)==y).float().mean()

def get_model():
    model = nn.Sequential(nn.Linear(m, nh), nn.ReLU(), nn.Linear(nh, 10))
    return model, optim.SGD(model.parameters(), lr=lr)

class Dataset():
    def __init__(self, x, y):
        self.x, self.y = x,y

    def __len__(self):
        return len(self.x)

    def __getitem__(self,key):
        return self.x[key], self.y[key]

def get_dls(train_ds, valid_ds, bs, **kwargs):
    return (DataLoader(train_ds, batch_size=bs, shuffle=True, **kwargs),
            DataLoader(valid_ds, batch_size=bs*2, **kwargs))