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
N = int(input())
if N <= 10 ** 3 - 1:
    print(N)
elif N <= 10 ** 4 - 1:
    print(N - N % 10)
elif N <= 10 ** 5 - 1:
    print(N - N % 100)
elif N <= 10 ** 6 - 1:
    print(N - N % 1000)
elif N <= 10 ** 7 - 1:
    print(N - N % 10000)
elif N <= 10 ** 8 - 1:
    print(N - N % 100000)
elif N <= 10 ** 9 - 1:
    print(N - N % 1000000)