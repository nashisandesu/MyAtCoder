import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
I_M = lambda: map(int, input().split())
S_M = lambda: map(str, input().split())
I_L = lambda: list(map(int, input().split()))
S_L = lambda: list(map(int, input().split()))

#########################################################3

N, K = I_M()
A = I_L()
Q = I()
sum_K =[[0] * K for _ in range((N // K) + 2)]
for i in range(N):
    sum_K[i // K + 1][i % K] = A[i] + sum_K[i // K][i % K]

for _ in range(Q):
    l, r = I_M()
    sum_now = set()
    l_sho, l_amari = (l - 1) // K, (l - 1) % K
    r_sho, r_amari = (r - 1) // K, (r - 1) % K
    for i in range(K):
        if l_amari <= i:
            start = l_sho
        else:
            start = l_sho + 1
        if r_amari >= i:
            end = r_sho + 1
        else:
            end = r_sho
        sum_now.add(sum_K[end][i] - sum_K[start][i])
    print('Yes' if len(sum_now) == 1 else 'No')