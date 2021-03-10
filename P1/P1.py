
def check_3(k):
    k_str = str(k)
    s = 0
    for c in k_str:
        s += int(c)
    if s % 3 == 0:
        return True
    else:
        return False

def check_5(k):
    k_str = str(k)
    l = int(k_str[-1])
    if l == 0 or l == 5:
        return True
    else:
        return False

N = 1000
sum_all = 0
for i in range(1,N):
    if check_3(i) or check_5(i):
        sum_all += i
        # print(i)

print(sum_all)
