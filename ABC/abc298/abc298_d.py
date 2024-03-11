import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

S = 1
d = deque()
d.append(1)
Q = int(input())
mod = 998244353
for i in range(Q):
    num, *x = map(int, input().split())
    if num == 1:
        S = S * 10 + x[0]
        S %= mod
        d.append(x[0])
    elif num == 2:
        S -= d[0] * pow(10, len(d) - 1, mod)
        S %= mod
        d.popleft()
    else:
        print(S)