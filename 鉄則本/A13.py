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
N, K = Mi()
A = Li()
#二分探索
ans = 0
for i in range(N):
    max_A = A[i] + K
    index = bisect.bisect_right(A, max_A)
    ans += index - i - 1
print(ans)

#しゃくとり法
ans = 0
now = 0
for i in range(N):
    while now < N - 1 and A[now + 1] - A[i] <= K:
        now += 1
    ans += now - i 

print(ans)