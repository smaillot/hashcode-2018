from IO import *
from solution import generate_solution

class Loaded_input:
    def __init__(self, args):
        self.args = args
        self.list_vehicles = self.F * [[0, 0]]

    def generate_solution(self, seed):
        
        return generate_solution(self, seed)

