"""
Goldbach''s other conjecture: https://projecteuler.net/problem=46

Brute force and horrible method
Eloi 11/03/2021
"""
from time import time

def get_prime_list(n, p=[2, 3]):
    p.sort()
    while p[-1] < n:
        is_prime = False
        m = p[-1]
        while not is_prime:
            m += 2
            passed = True
            for prime in p:
                if m % prime == 0:
                    passed = False
                    break
            if passed:
                p.append(m)
                is_prime = True
    return p

t0 = time()
i = 33
primes = get_prime_list(i)
is_gold = True
while is_gold:
    i += 2

    # Get primes if needed
    if i > primes[-1]:
        primes = get_prime_list(i, primes)

    # If i is not composite get another i
    if i in primes:
        continue
    
    # Else check if goldbach's other conjecture works
    check = False
    for p in primes:
        n = 0
        j = 0
        while n < i:
            j += 1
            n = p + 2 * j * j
        if i == n:
            check = True
            break
    # This is just to finish
    if not check:
        is_gold = False
tf = time()

print("The smallest odd composite number that does not fulfil Godlbach's other conjecture is {}.".format(i))
print("Found in {} seconds.".format(tf - t0))



