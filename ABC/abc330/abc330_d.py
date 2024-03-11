import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
mas = [[0] * 2 for _ in range(N)]
databox = []
for i in range(N):
    data = list(input())
    for j in range(N):
        if data[j] == 'o':
            mas[i][0] += 1
            mas[j][1] += 1
    databox.append(data)

ans = 0 

for i in range(N):
    for j in range(N):
        if databox[i][j] == 'o':
            ans += (mas[i][0] - 1) * (mas[j][1] - 1)

print(ans)
