import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

N = int(input())
B = int((N // 12)**0.5) + 1
temp = [True] * B
temp[0] = False
temp[1] = False
for i, tmp in enumerate(temp):
    if tmp:
        for j in range(i * i, B, i):
            temp[j] = False

primes = [ i for i in range(B) if temp[i]]
sosuu =len(primes)
cnt = 0
for i in range(sosuu):
    a = primes[i]
    if N < a ** 5:
        break
    for j in range(i + 1, sosuu):
        b = primes[j]
        if N < a * a * b ** 3:
            break
        for k in range(j + 1, sosuu):
            c = primes[k]
            if N < a * a * b * c * c:
                break
            cnt += 1
print(cnt)