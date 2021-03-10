"""
In this version we store all the previous chains in a dictionary named d
and check if our result is in there. If it is, we just add the current chain
to the already calculated.

The improvement relies on
- Ability to store a dictionary of such dimension (maybe add a length 
restriction)
- If finding a number inside the dictionary is faster than calculating the 
chain

Eloi 10/03/2021
"""

def step(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)


N = 1000000
largest = 0
d = {2:2}
for i in range(2,N + 1):
    l = 1
    k = i
    while i not in d:
        i = step(i)
        l += 1
    l += d[i] - 1
    d[k] = l
    if l > largest:
        largest = l
        number = k

print("The largest chain found has legth {} for nº {}.".format(largest, number))
