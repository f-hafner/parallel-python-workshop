"Vary the amount of work"

from itertools import repeat
import multiprocessing as mp 
from timeit import timeit 

import random 

def calc_pi(N, name=None):
    printing = name is not None 
    if printing:
        print(f"{name}: starting")
    M = 0 
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            M += 1
    
    if printing:
        print(f"{name}: Done")
            
    return 4*M/N


def submit(ctx, N):
    with ctx.Pool() as pool:
        pool.starmap(calc_pi, repeat((N,), 4)) # repeat((N,), 4) = (N, N, N, N)


if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    for i in (100, 1000, 10_000, 1_000_000, 10_000_000):
        res = timeit(lambda: submit(ctx, i), number=5)
        print(f"Using {i} samples took {res} seconds")
        

