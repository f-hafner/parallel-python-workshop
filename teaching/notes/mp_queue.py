import multiprocessing as mp
import random


def calc_pi(N, que):
    M = 0
    for i in range(N):
        # Simulate impact coordinates
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # True if impact happens inside the circle
        if x**2 + y**2 < 1.0:
            M += 1
    que.put((4 * M / N, N))  # result, iterations


if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    que = ctx.Queue()
    n = int((10**7)/2)
    p1 = ctx.Process(target=calc_pi, args=(n, que))
    p2 = ctx.Process(target=calc_pi, args=(n, que))
    p1.start()
    p2.start()

    for i in range(2):
        print(que.get())

    p1.join()
    p2.join()