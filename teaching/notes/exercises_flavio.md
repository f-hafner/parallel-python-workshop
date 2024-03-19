# Exercises

## Computing pi 

### Implement algorithm to compute pi

Compute pi by only using standard python and the `random.uniform` function. The function should have the following structure:
```python
import random
def calc_pi(N):
    """Computes the value of pi using N random samples."""
    ...
    for i in range(N):
        # take a sample
        ...
    return ...
```

Make sure to time your function.


### Daskify 
Write calc_pi_dask to make the Numpy version parallel. Compare speed and memory performance with the Numpy version. Remember that dask.array mimics the numpy API.


### Numbify
Create a numba function of `calc_pi`. Time it.


## Threads and processes

### Threading on a numpy function 

Many numpy functions unlock the GIL. Sort two randomly generated arrays using `numpy.sort` in parallel. Compare the time to the sequential execution.


### Overhead and the gains from multiprocessing

Using the original `calc_pi` function, write a program the runs the computation across multiple processes. 
First, investigate the scaling behavior of the program with respect to the amount of work: you can do that by varying the amount of work and fixing the number of processes.
Second, investigate the scaling behavior of the program with respect to the number of processes, by fixing the amount of work and varying the number of processes.

It is recommended to have the programs in separate script and call the scripts from the notebook with `!python myscript.py`.

Hint: you can use [multiprocessing.starmap](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap)

