import multiprocessing as mp
from IO import *

from score import compute_score

def solve(loaded_input, seeds, number_cpu):
    # Initializing best score and best solution
    # These are shared values between processes
    best_score = mp.Value('i', 0)
    solution = mp.Manager().list([[]])

    # Threads preparation 
    task_queue = mp.Queue()
    done_queue = mp.Queue()
    # Tasks queue
    for seed in seeds:
        task_queue.put(seed)
    lock = mp.Lock() # Prevents race conditions

    
    ###########################
    ## Parallel computing
    ###########################
    """ Do not touch anything
    Change solution.worker to change the solution's generator behavior """
    # We screen through each CPU and dedicate one thread for each
    processes = [mp.Process(target=worker, args=(best_score, solution, lock, loaded_input, task_queue, done_queue)) for _ in range(number_cpu)]
    progress_bar = progress(range(len(seeds)), desc = "Generating solutions")
    for p in processes:
        # Create a process that will race through the execution queue
        p.start()

    # Load loading screen

    refresh_rate = max(1, (len(progress_bar) // 100))
    
    for k in progress_bar:
        done_queue.get()
        if k % refresh_rate == 0:
            progress_bar.set_description("Current best score : " + str(best_score.value))
    
    # Stop all processes
    for p in processes:
        task_queue.put('STOP')
    
    return solution[0]

def worker(best_score, best_solution, l, loaded_input, q, output):
    """General
    q.get() must be a loaded_input with the method generate_solution(int seed)
    """
    # We get the seed that will generate our solution
    # STOP stops the worker
    for seed in iter(q.get, 'STOP'):

        # We calculate a solution from a seed and evaluate its score
        solution = loaded_input.generate_solution(seed)
        score = compute_score(solution)

        # Lock state to prevent race condition
        l.acquire()
        #print(score)
        # If our solution is better we save it in the shared variable
        if score > best_score.value:
            
            best_score.value = score
            
            best_solution[0] = solution
        # End of atomic operation
        l.release()
        output.put(True)