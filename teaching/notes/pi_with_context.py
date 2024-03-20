
import multiprocessing as mp 


from calc_pi import calc_pi

if __name__ == "__main__":
    # n = 10**6
    n=int((10**7)/2)
    ctx = mp.get_context("fork") # spawn fill fail within the notebook 
    # with ctx as c:
    p1 = ctx.Process(target=calc_pi, args=(n, "Process 1"))
    p2 = ctx.Process(target=calc_pi, args=(n, "Process 2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()