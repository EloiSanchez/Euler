
def step(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)


N = 20
largest = 0
for i in range(2,N + 1):
    l = 1
    k = i
    while i != 1:
        i = step(i)
        l += 1
    if l > largest:
        largest = l
        number = k

print("The largest chain found has legth {} for nº {}.".format(largest, number))
