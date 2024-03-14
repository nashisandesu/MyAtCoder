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
N, M = Mi()
data = [0] + [[0] + list(input()) for _ in range(N)]

def check(i, j):
    for a in range(3):
        for b in range(3):
            if data[i+a][j+b] == '.':
                return False
            if data[i+a+6][j+b+6] == '.':
                return False
    for c in range(4):
        if data[i+3][j+c] == '#':
            return False
        if data[i+c][j+3] == '#':
            return False
        if data[i+5][j+5+c] == '#':
            return False
        if data[i+5+c][j+5] == '#':
            return False        
    return True

for i in range(1, N - 8 + 1):
    for j in range(1, M - 8 + 1):
        if check(i, j):
            print(i,j)
