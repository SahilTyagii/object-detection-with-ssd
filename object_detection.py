# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:30:37 2024

@author: Sahil
"""

# importing libraries
import torch
from torch.autograd import Variable
import  cv2
from data import BaseTransform, VOC_CLASSES as labelmap
from ssd import build_ssd
import imageio

# defining functions
def detect(frame, net, transform):
    height, width = frame.shape[:2]
    frame_t = transform(frame)[0]
    x = torch.from_numpy(frame_t).permute(2, 0, 1)
    x = Variable(x.unsqueeze(0))
    