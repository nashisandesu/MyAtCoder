import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

S = list(input())
N = int(input())
now = 0
hatena = []
for i, s in enumerate(reversed(S)):
    if s == '1':
        now += 2 ** i
    elif s == '?':
        hatena.append(i)

if now > N:
    print("-1")
else:
    target = N - now
    while hatena:
        if target == 0:
            break
        bit = hatena.pop()
        if target - 2 ** bit >= 0:
            target -= 2 ** bit
            now += 2 ** bit 
    print(now)


