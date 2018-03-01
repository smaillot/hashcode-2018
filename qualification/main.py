# compatibility
from __future__ import division
from __future__ import print_function

# standard
from time import time
import numpy as np
#import multiprocessing as mp 

# custom
from IO import *
from loaded_input import Loaded_input
from solver import solve
from score import compute_score
from validation import is_valid_solution
from pre_process import *
from post_process import *

if __name__ == '__main__':

    # Parsing arguments
    args = parsing()
    n_tries = args.n
    number_cpu = args.p

    ''' This is where the fun begins'''
    
    # Loading input
    params, array = read_input(args.input)
    loaded_input = Loaded_input(params, array)

    ###########################
    ## Pre-processing
    ###########################

    seeds = init_seeds(compute_possibilities(loaded_input), n_tries)
    
    ###########################
    ## Find best solution
    ###########################
    
    start = time()
    solution = solve(loaded_input, seeds, number_cpu)
    end = time()
    computing_time = end - start
    
    ###########################
    ## Post-processing
    ###########################
    
    # Improves the solution
    solution = improve_solution(solution, loaded_input)
 
    ###########################
    ## Checks solution and writes it out
    ###########################

    # Check if solution is valid
    valid = is_valid_solution(solution, loaded_input)
    display(solution, loaded_input)

    # Compute score and display
    score = compute_score(solution) * valid
    print_score(score, loaded_input, end - start)
    
    # Writing to output
    write_output(args.input, "algo1", score, solution)