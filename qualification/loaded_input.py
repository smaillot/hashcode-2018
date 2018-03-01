from IO import *
from solution import generate_solution

class Loaded_input:
    def __init__(self, params, array):
        self.rows = params[0]
        self.cols = params[1]
        self.vehicules = params[2]
        self.rides = params[3]
        self.bonus = params[4]
        self.steps = params[5]
        self.rides = array

    def generate_solution(self, seed):
        
        return generate_solution(self, seed)

