import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
s = list(input())
t = list(input())
s_len = len(s)
t_len = len(t)
s.insert(0,0)
t.insert(0,0)
dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

for i in range(1, s_len + 1):
    for j in range(1, t_len + 1):
        if s[i] == t[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

s_now = s_len
t_now = t_len
ans_len = dp[s_now][t_now]
ans = [0] * (ans_len + 1)
while (ans_len > 0):
    if s[s_now] == t[t_now]:
        ans[ans_len] = s[s_now]
        s_now -= 1
        t_now -= 1
        ans_len -= 1
    elif dp[s_now][t_now] == dp[s_now - 1][t_now]:
        s_now -= 1
    else:
        t_now -= 1

print(''.join(ans[1:]))