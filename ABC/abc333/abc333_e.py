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
potion = dict()
dp = [0] * N
pick_cnt = 0
pick = [0] * N 

event = [Li() for _ in range(N)]
for i in range(N):
    t, x = event[i]
    if t == 1:
        potion.setdefault(x, deque())
        potion[x].append((i, pick_cnt))
        pick_cnt += 1
    if t == 2:
        potion.setdefault(x, deque())
        if len(potion[x]):
            p = potion[x].pop()
            dp[p[0]] += 1
            dp[i] -= 1
            pick[p[1]] = 1
        else:
            print(-1)
            exit()
ans = [0] * N
ans_max = 0
for i in range(1, N):
    ans[i] = ans[i-1] + dp[i-1]
    ans_max = max(ans_max, ans[i])
print(ans_max)
print(*pick[:pick_cnt])