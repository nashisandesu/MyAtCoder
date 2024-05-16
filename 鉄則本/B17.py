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
h = [0] + Li()
dp = [[0] * 2 for _ in range(N + 1)]
dp[2] = [abs(h[1]-h[2]), 1]
for i in range(3, N + 1):
    if dp[i-1][0] + abs(h[i-1] - h[i]) < dp[i-2][0] + abs(h[i-2] - h[i]):
        dp[i] = [dp[i-1][0] + abs(h[i-1] - h[i]), i - 1]
    else:
        dp[i] = [dp[i-2][0] + abs(h[i-2] - h[i]), i - 2]
now = N
ans = deque()
ans.appendleft(N)
while True:
    before = dp[now][1]
    if before == 0:
        break
    else:
        ans.appendleft(before)
        now = before
print(len(ans))
print(*ans)