from itertools import repeat
import multiprocessing as mp
import random
from timeit import timeit


from calc_pi import calc_pi

def submit(ctx, n_procs):
    with ctx.Pool() as pool:
        pool.starmap(calc_pi, repeat((1_000_000//n_procs,), n_procs))


if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    for i in (1, 2, 4, 8, 16): # note true N is 4*this input, but same order of magnitude
        res = timeit(lambda: submit(ctx, i), number=5)
        print(f"Using {i} workers took {res} seconds.")