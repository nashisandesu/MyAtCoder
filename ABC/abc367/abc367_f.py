import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
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
# Zobrist Hash 
import random
mod = (1 << 61) - 1
N, Q = Mi()
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

# 各要素にハッシュ値を割り当てる i番目の要素xはx+hash[i]だったことにする
hash = [random.randint(1, mod - 1) for _ in range(N)]
cumA = [0] * (N + 1)
cumB = [0] * (N + 1)
for i in range(N):
    cumA[i + 1] = (cumA[i] + hash[A[i]]) % mod
    cumB[i + 1] = (cumB[i] + hash[B[i]]) % mod
    
for i in range(Q):
    l, r, L, R = Mi()
    if (cumA[r] - cumA[l - 1]) % mod == (cumB[R] - cumB[L - 1]) % mod:
        print("Yes")
    else:
        print("No")