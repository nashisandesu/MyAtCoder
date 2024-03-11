import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
gen = [Li() for _ in range(N)]
check = [-1] * (2*N+1)
pair = dict()
for l, r in gen:
    l,r = min(l,r), max(l,r)
    check[l] = 1
    check[r] = 0
    pair[l] = r
    pair[r] = l

cnt = 0
start = 1
deq = deque()

while True:
    if check[start]:
        break
    else:
        start += 1

flag = 0
for i in range(start, start + 2 * N):
    idx = i - 2 * N if i > 2 * N else i
    if check[idx]:
        deq.append(pair[idx])
    else:
        if deq[-1] == idx:
            deq.pop()
        else:
            print('Yes')
            break
else:   
    print('No')

