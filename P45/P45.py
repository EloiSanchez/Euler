"""
Triangular, pentagonal and Hexagonal: https://projecteuler.net/problem=45

Brute force.
Eloi 11/03/2021
"""
from time import time

def triangular(n):
    return int(n * (n + 1) / 2)

def pentagonal(n):
    return int(n * (3 * n - 1) / 2)

def hexagonal(n):
    return int(n * (2 * n - 1))

t0 = time()

i, j, k = 143, 165, 285 
p = pentagonal(j)
t = triangular(k)
all_check = False
while not all_check:
    i += 1
    h = hexagonal(i)
    pent_check = False
    while p < h:
        j += 1
        p = pentagonal(j)
        if p == h:
            while t < p:
                k += 1
                t = triangular(k)
                if t == p:
                    all_check = True
                    break

tf = time()

print(t, p, h, tf - t0)