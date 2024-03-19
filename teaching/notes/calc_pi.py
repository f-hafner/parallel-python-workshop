import random

def calc_pi(N, name=None):
    "Compute pi using N random samples"
    printing = name is not None
    if printing:
        print(f"{name}: starting")  
    M = 0 
    for i in range(N):
        # Simulate random coordinates
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1: # don't need sqrt b/c 1**2 = 1
            M += 1

    if printing:
        print(f"{name}: Done")
    return 4*M/N