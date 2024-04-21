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
R, C = map(int,input().split())

data = [list(input()) for i in range(R)]

for i in range(R):
    for j in range(C):
        if data[i][j] != "." and data[i][j] != "#":
            x = i
            y = j
            num = int(data[i][j]) + 1

            for k in range(num):
                for l in range(num-k):
                    if x-l >= 0 and y-k >= 0:
                        if not (data[x-l][y-k] != "." and data[x-l][y-k] != "#"):
                            data[x-l][y-k] = "."
                    if x + l < R and y + k < C:
                        if not (data[x+l][y+k] != "." and data[x+l][y+k] != "#"):
                            data[x+l][y+k] = "." 
                    if  x-l >= 0 and y + k < C:
                        if not (data[x-l][y+k] != "." and data[x-l][y+k] != "#"):
                            data[x-l][y+k] = "." 
                    if x + l < R and y-k >= 0:
                        if not (data[x+l][y-k] != "." and data[x+l][y-k] != "#"):
                            data[x+l][y-k] = "."     
            data[i][j] = "."
for i in range(R):
    print("".join(data[i]))
