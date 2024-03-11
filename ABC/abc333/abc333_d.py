import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations
from atcoder.dsu import DSU

I = lambda: int(input())
# S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
uf = DSU(N)
data = []
for i in range(N - 1):
    L, R = Mi()
    L -= 1
    R -= 1
    if L == 0 or R == 0:
        data.append(max(L, R))
    else:
        uf.merge(L, R)

ans = 0
ans_max = 0
for num in data:
    value = uf.size(num)
    ans += value
    ans_max = max(value, ans_max)
print(ans - ans_max + 1)