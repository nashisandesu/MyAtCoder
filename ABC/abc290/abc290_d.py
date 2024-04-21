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
import numpy as np
T = int(input())
for i in range(T):
    N, D, K = map(int,input().split())
    nd_gcd = np.gcd(N, D)
    d = D // nd_gcd
    n = N // nd_gcd
    count = (K - 1) // n
    print(count + (D * (K - 1)) % N)