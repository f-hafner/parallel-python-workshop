"Vary the amount of work"


from itertools import repeat
import multiprocessing as mp
from timeit import timeit


from calc_pi import calc_pi


def submit(ctx, N):
    with ctx.Pool() as pool:
        pool.starmap(calc_pi, repeat((N,), 4))


if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    for i in (100, 1_000, 10_000, 1_000_000, 10_000_000): # note true N is 4*this input, but same order of magnitude
        res = timeit(lambda: submit(ctx, i), number=5)
        print(f"Using {i} samples took {res} seconds.")