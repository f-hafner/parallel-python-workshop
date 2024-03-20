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

Using the original `calc_pi` function, write a program the runs the computation across multiple processes and records the time taken.
First, vary the amount of work and fix the number of processes.
Then, vary the number of processes and fix the amount of work.

By inspecting the running times, investigate the scaling behavior of the programs. What can we learn?

It is recommended to have the programs in separate script and call the scripts from the notebook with `!python myscript.py`.

Hint: you can use [multiprocessing.starmap](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap)


### Dask -- delayed evaluation

#### Exercise: run the workflow

Given this workflow:

```python
x_p = add(1, 2)
y_p = add(x_p, 3)
z_p = add(x_p, -3)
```

Visualize and compute `y_p` and `z_p` separately, how often is `x_p` evaluated?

Now change the workflow:


```python
x_p = add(1, 2)
y_p = add(x_p, 3)
z_p = add(x_p, y_p)
z_p.visualize(rankdir="LR")

```


We pass the yet uncomputed promise x_p to both y_p and z_p. Now, only compute z_p, how often do you expect x_p to be evaluated? Run the workflow to check your answer.


#### Exercise: understanding gather

Can you describe what the `gather` function does in terms of lists and promises? hint: Suppose I have a list of promises, what does `gather` allow me to do?



#### Exercise: Design a `mean` function and calculate pi

Write a `delayed` function that computes the mean of its arguments. Use it to esimates pi several times and returns the mean of the results.

```python
>>> mean(1, 2, 3, 4).compute()
2.5
```
Make sure that the entire computation is contained in a single promise.





### Dask -- Map and reduce

#### Discussion

Open the [Dask documentation](https://docs.dask.org/en/latest/bag-api.html) on bags. Discuss the `map`, `filter`, `flatten` and `reduction` methods

In this set of operations `reduction` is rather special. All other operations on bags could be written in terms of a reduction.

#### Exercise: Difference between `filter` and `map`

Without executing it, try to forecast what would be the output of `bag.map(pred).compute()`.


#### Exercise: Consider `pluck` 

We previously discussed some generic operations on bags. In the documentation, lookup the `pluck` method. How would you implement this if `pluck` wasn’t there?

hint: Try `pluck` on some example data.

```python

from dask import bags as db

data = [
   { "name": "John", "age": 42 },
   { "name": "Mary", "age": 35 },
   { "name": "Paul", "age": 78 },
   { "name": "Julia", "age": 10 }
]

bag = db.from_sequence(data)
````

