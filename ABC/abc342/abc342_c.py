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
def transform_string(S, Q, operations):
    char_map = {chr(i + 97): chr(i + 97) for i in range(26)}
    
    for c, d in operations:
        for key, value in char_map.items():
            if value == c:
                char_map[key] = d
    
    transformed_string = ''.join(char_map[c] for c in S)
    
    return transformed_string
N = I()
S = list(input())
Q = I()
operations = [Ls() for _ in range(Q)]
transformed_string = transform_string(S, Q, operations)
print(transformed_string)