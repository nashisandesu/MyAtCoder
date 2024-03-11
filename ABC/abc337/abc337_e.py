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
data = [2 ,4, 8, 16, 32, 64]
M = bisect.bisect_left(data,N) + 1
print(M)
drink = []
for i in range(N):
    drink.append(int(bin(i)[2:]))
drink_list = [[] for _ in range(M)]
for i in range(N):
    now = drink[i]
    for j in range(M):
        if now % 10 == 1:
            drink_list[M-j-1].append(i+1)
        now //= 10

for i in range(M):
    drink_list[i].insert(0,len(drink_list[i]))
    print(' '.join(map(str,drink_list[i])))
S = input()
print(int(S,2) + 1)