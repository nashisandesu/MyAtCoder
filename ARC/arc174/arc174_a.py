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
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
def max_sum_after_operation(A, C, N):
    initial_sum = sum(A)
    
    max_diff = 0
    current_diff = 0
    
    for i in range(N):
        current_diff += (A[i] * C - A[i])

        if current_diff < 0:
            current_diff = 0
        
        max_diff = max(max_diff, current_diff)
    
    final_max_sum = initial_sum + max_diff
    return final_max_sum

N, C = Mi()
A = Li()
print(max_sum_after_operation(A, C, N))