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
A = Li()
B = Li()
dp = [{'cost':0, 'pre':0} for _ in range(N+1)]
dp[2]['cost'] = A[0]
dp[2]['pre'] = 1
for i in range(3, N+1):
    if dp[i-1]['cost']+A[i-2] < dp[i-2]['cost']+ B[i-3]:
        dp[i]['cost'] = dp[i-1]['cost']+A[i-2] 
        dp[i]['pre'] = i-1
    else:
        dp[i]['cost'] = dp[i-2]['cost']+B[i-3] 
        dp[i]['pre'] = i-2
ans = deque()
ans.appendleft(N)
now = N
while True:
    before = dp[now]['pre']
    if before == 0:
        break
    else:
        ans.appendleft(before)
        now = before
print(len(ans))
print(*ans)