from IO import *
from solution import generate_solution
import numpy as np

class Vehicle:
    def __init__(self, depart, arrivee):
        self.depart = depart
        self.arrivee = arrivee
        self.time_left = distance(depart, arrivee)
    def maj(self):
        if self.time_left != 0:
            self.time_left -= 1
    

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

    def generate_solution(self, seed):
        
        return generate_solution(self, seed)

