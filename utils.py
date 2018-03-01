# compatibility
from __future__ import division
from __future__ import print_function

# custom
from IO import *
import numpy as np

def distance(depart, arrivee):
    difference = arrivee - depart
    return np.abs(difference[0]) + np.abs(difference[1])

def filter_rides_start_in_time(start, end, rides_array):

    rides = np.copy(rides_array)
    return [r for r in rides if r[4]>=start and r[4]<=end]

def list_possible_rides_bonus(x, y, t, max_steps, rides_array):

    rides = filter_rides_start_in_time(t, t+max_steps, rides_array)
    pose = np.array([x, y])
    return [r for r in rides if distance(pose, np.array([r[0], r[1]])) < r[4] - t]

def list_possible_rides(x, y, t, max_steps, rides_array):

    rides = filter_rides_start_in_time(t, t+max_steps, rides_array)
    pose = np.array([x, y])
    return [r for r in rides if distance(pose, np.array([r[0], r[1]])) + distance(np.array([r[0], r[1]]), np.array([r[2], r[3]])) < r[4] - t - max_steps]
