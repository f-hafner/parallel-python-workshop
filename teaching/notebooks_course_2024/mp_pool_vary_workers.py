#mp_pool_vary_workers.py
"""Vary the amount of work"""
import multiprocessing as mp
from itertools import repeat
from timeit import timeit
import random

def calc_pi(N):
    M = 0
    for i in range(N):
        # Simulate impact coordinates
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # True if impact happens inside the circle
        if x**2 + y**2 < 1.0:
            M += 1
    return 4 * M / N


def submit(ctx, n_jobs, n_workers=4):
    with ctx.Pool(n_workers) as pool:
        pool.starmap(calc_pi, repeat((1_000_000//n_jobs, ), n_jobs))

if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    for i in range(6):
        res = timeit(lambda: submit(ctx, 2**i), number=5)
        print(f"using {2**i} jobs took {res} seconds")