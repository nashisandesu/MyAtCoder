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
N = I()
A = [Li() for _ in range(N)]
B = [Li() for _ in range(N)]
def check(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    return

n_A = [[A[N-1-j][i] for j in range(N)] for i in range(N)]
n1_A = [[n_A[N-1-j][i] for j in range(N)] for i in range(N)]
n2_A = [[n1_A[N-1-j][i] for j in range(N)] for i in range(N)]
n3_A = [[n2_A[N-1-j][i] for j in range(N)] for i in range(N)]
check(A, B)
check(n_A, B)
check(n1_A, B)
check(n2_A, B)
print('No')