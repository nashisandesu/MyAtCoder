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
N = I()
A = Li()
Nmax=10**6
dp = [0]*(Nmax+1)
maxsum=0
for i in range(N):
    dp[A[i]] += 1
    maxsum += A[i]
sum = [0] * (Nmax+1)
sum[0] = maxsum
for i in range(1, Nmax):
    sum[i] = sum[i-1] - i * dp[i]
    
ans = [0]* N
for i in range(N):
    ans[i] = sum[A[i]]
print(' '.join(map(str,ans)))