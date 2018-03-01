from IO import *
from solution import generate_solution
import numpy as np

def distance(depart, arrivee):
    difference = arrivee - depart
    return np.abs(difference[0]) + np.abs(difference[1])

class Ride:
    def __init__(self, depart, arrivee, earliest_start, latest_finish, B):
        self.depart = depart
        self.arrivee = arrivee
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.length = distance(depart, arivee)
        self.bonus = bonus
        # Time when ride is started
        self.time_started = 10**9
        # Timde when ride is over
        self.time_finished = 10**9
    def score(self):
        return (self.time_finished <= self.latest_finish) * (self.length + self.B * (self.time_started == self.earliest_start))
    
    def set_schedule(self, time_started):
        self.time_started = time_started
        self.time_finished = self.time_started + self.length
    
    

class Vehicle:
    def __init__(self, rides):
        self.rides = rides
        
    def set_arrival_rides(self):
        position_car = [0, 0]
        for ride in rides:


    
    

class Loaded_input:
    def __init__(self, params, array):
        self.rows = params[0]
        self.cols = params[1]
        self.number_vehicles = params[2]
        self.rides = params[3]
        self.bonus = params[4]
        self.steps = params[5]
        self.rides = array
        self.list_vehicles = self.number_vehicles * [[0, 0]]

    def compute_score(self, rides):



    def generate_solution(self, seed):
        
        return generate_solution(self, seed)

