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
mod = 998244353
div = pow(N, -1, mod)
p = [0] * (N + 1)
sum_p = [0] * (N + 1)
p[0] = 1 
sum_p[0] = 1
ans = 0
for i in range(1, N + 1):
    p[i] = sum_p[i-1] * div % mod
    sum_p[i] = p[i] + sum_p[i-1]
    ans += A[i-1] * p[i]
    ans %= mod
print(ans)