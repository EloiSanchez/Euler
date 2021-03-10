"""
Pandigital products: https://projecteuler.net/problem=32

Brute force way.
Eloi 10/03/2021
"""
import time

def is_pandigital(s, d):
    d = [str(c) for c in range(1, d + 1)]
    for char in d:
        if s.count(char) != 1:
            return False
    return True

t0 = time.time()
pand_list = []
suma = 0
for j in range(5000):
    i = 1
    s = ""
    while len(s) <= 9 and i<j:
        i += 1
        t = i * j
        s = str(j) + str(i) + str(t)
        if len(s) < 9:
            continue
        if is_pandigital(s, 9) and t not in pand_list:
            pand_list.append(t)
            suma += i * j
            print(j, i, i * j)
tf = time.time()

print("The total sum is {} and it took {:f} seconds to find".format(suma, tf - t0))
