from IO import *
from solution import generate_solution
import numpy as np
from utils import distance

class Ride:
    def __init__(self, depart, arrivee, earliest_start, latest_finish, bonus):
        self.depart = depart
        self.arrivee = arrivee
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.length = distance(depart, arrivee)
        self.bonus = bonus
        # Time when ride is started
        self.time_started = 10**9
        # Timde when ride is over
        self.time_finished = 10**9
    def score(self):
        return (self.time_finished <= self.latest_finish) * (self.length + self.bonus * (self.time_started == self.earliest_start))
    
    def set_schedule(self, time_started):
        self.time_started = time_started
        self.time_finished = self.time_started + self.length
    
    

class Vehicle:
    def __init__(self, rides):
        self.rides = rides
        
    def set_depart_times(self):
        step = 0
        position_car = [0, 0]
        for ride in self.rides:
            # Car is moving
            distance_travel = distance(position_car, ride.depart)
            step += distance_travel
            # Car is waiting
            waiting_time = min(ride.earliest_start - step, 0)
            step += waiting_time
            # We can go now
            depart_time = step
            ride.set_schedule(depart_time)
            # Car is moving
            step += ride.length
            # Car arrived at destination
            position_car = ride.arrivee


    
    

class Loaded_input:
    def __init__(self, params, array):
        self.rows = params[0]
        self.cols = params[1]
        self.number_vehicles = params[2]
        self.rides = params[3]
        self.bonus = params[4]
        self.steps = params[5]
        self.rides = array
        
        self.list_vehicles = []

    def set_rides(self, rides):
        self.list_vehicles.append(Vehicle(rides))

    def set_all_rides_departs(self):
        for vehicle in self.list_vehicles:
            vehicle.set_depart_times()
    




    def compute_score(self, rides):
        s = 0
        for vehicle in self.list_vehicles:
            for ride in vehicle.rides:
                s += ride.score()
                


    def generate_solution(self, seed):
        
        return generate_solution(self, seed)

