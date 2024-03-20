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