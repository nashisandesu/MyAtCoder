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
N, K = Mi()
s = [0] + list(input())
dp = [[0] * (1 << K) for _ in range(N+1)]
dp[0][0] = 1
MOD = 998244353 
for i in range(1, N + 1):
    if i < K:
        for j in range(1 << K):
            next_A = (j << 1) % (1 << (K))
            next_B = (j << 1) % (1 << (K)) + 1
            if s[i] == '?': 
                dp[i][next_A] += dp[i-1][j]
                dp[i][next_B] += dp[i-1][j]
                dp[i][next_A] %= MOD
                dp[i][next_B] %= MOD
            elif s[i] == 'A':
                dp[i][next_A] += dp[i-1][j]
                dp[i][next_A] %= MOD
            else:
                dp[i][next_B] += dp[i-1][j]
                dp[i][next_B] %= MOD
    else:
        for j in range(1 << K):
            next_A = (j << 1) % (1 << (K))
            next_B = (j << 1) % (1 << (K)) + 1
            if s[i] == '?': 
                binary_str = format(next_A, '0{}b'.format(K))
                if binary_str != binary_str[::-1]:
                    dp[i][next_A] += dp[i-1][j]
                    dp[i][next_A] %= MOD
                
                binary_str = format(next_B, '0{}b'.format(K))
                if binary_str != binary_str[::-1]:
                    dp[i][next_B] += dp[i-1][j]
                    dp[i][next_B] %= MOD
                
            elif s[i] == 'A':
                binary_str = format(next_A, '0{}b'.format(K))
                if binary_str == binary_str[::-1]:
                    continue
                else:
                    dp[i][next_A] += dp[i-1][j]
                    dp[i][next_A] %= MOD
            else:
                binary_str = format(next_B, '0{}b'.format(K))
                if binary_str == binary_str[::-1]:
                    continue
                else:
                    dp[i][next_B] += dp[i-1][j]
                    dp[i][next_B] %= MOD
ans = 0
for j in range(1 << K):           
    ans += dp[-1][j]
    ans %= MOD
print(ans)