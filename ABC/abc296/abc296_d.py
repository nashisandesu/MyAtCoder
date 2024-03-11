import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

N, M = map(int, input().split())
now = 10 ** 24
if N * N < M:
    print(-1)
else:
    for a in range(1, N + 1):
        if M % a == 0:
            b = M // a
        else:
            b = M // a + 1
        if b < a:
            break
        elif b <= N:
            if now > a * b:
                now = a * b
    print(now)
