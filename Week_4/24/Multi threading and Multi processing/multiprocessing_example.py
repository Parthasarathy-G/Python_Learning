## Processes that run in parallel
## CPU-Bound Tasks that are heavy on cpu usage
## Parallel execution - Multiple cores of the CPU

import multiprocessing as mp
import time

def square():
    for i in range(5):
        time.sleep(2)
        print(f"Square: {i**i}")

def cubes():
    for i in range(5):
        time.sleep(2)
        print(f"Cubes: {i*i*i}")

if __name__=="__main__":

    p1=mp.Process(target=square)
    p2=mp.Process(target=cubes)

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)