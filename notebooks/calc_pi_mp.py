import multiprocessing as mp 
import random 
import argparse 
import math 
from itertools import repeat
from timeit import timeit


parser = argparse.ArgumentParser()
parser.add_argument("--method", type=str, choices=["queue", "pool"])
args = parser.parse_args()


def calc_pi(N, que=None):
    "Calculate for N points, put results to queue"
    M = 0
    for i in range(N):
        # Simulate impact coordinates
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # True if impact happens inside the circle
        if x**2 + y**2 < 1.0:
            M += 1

    result = (4 * M / N, N)
    if que is not None:
        que.put(result)  # result, iterations
    else:
        return result 
    

def submit(ctx, N):
    n_workers = 4 
    batch_size = math.ceil(N/n_workers)
    inputs = repeat(batch_size, n_workers) 
    with ctx.Pool(processes=n_workers) as pool:
        results = pool.map(calc_pi, inputs, 1)

        n_iterations = sum([r[1] for r in results])
        results = [r[0] * r[1] / n_iterations for r in results]
        return results 


if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    n = 10**7
    if args.method == "queue":
        que = ctx.Queue()
        p1 = ctx.Process(target=calc_pi, args=(n, que))
        p2 = ctx.Process(target=calc_pi, args=(n, que))
        p1.start()
        p2.start()

        for i in range(2):
            print(que.get())

        p1.join()
        p2.join()
    elif args.method == "pool":
        for i in (1_000, 100_000, 10_000_000):
            res = timeit(lambda: submit(ctx, i), number=5)
            print(i, res)
