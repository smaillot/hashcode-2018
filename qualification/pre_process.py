# compatibility
from __future__ import division
from __future__ import print_function

# custom
from IO import *
import random
from time import time

def init_seeds(possibilities, tries):

    random.seed(time())
    return [[random.random() for _ in range(possibilities)] for _ in range(tries)]

def compute_possibilities(loaded_input):

    return 42