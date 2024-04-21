import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))
X = int(input())
visit = []
dp = [0] * (X + 1)
dp[0] = 1
moti = [0] * (X + 1)
for i in range(M):
    moti[B_list[i]] = 1

for i in range(1, X + 1):
    if moti[i] == 1:
        continue
    for j in range(N):
        if i - A_list[j] >= 0:
            if dp[i - A_list[j]] == 1:
                dp[i] = 1
                break
if dp[X] == 1:
    print("Yes")
else:
    print("No")