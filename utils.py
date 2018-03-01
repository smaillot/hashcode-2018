# compatibility
from __future__ import division
from __future__ import print_function

# custom
from IO import *
import numpy as np

def distance(depart, arrivee):
    difference = arrivee - depart
    return np.abs(difference[0]) + np.abs(difference[1])