linreg = lambda x, y, z: sum([i*j for i, j in zip(x,y)]) + z
from time import time

if __name__ == "__main__":
    start = time() * 1000
    for i in range(0,1000000):
        linreg([2.4,6.9], [2.9, 4.4], 2)
    print("miliseconds: ", time() *1000 - start)
