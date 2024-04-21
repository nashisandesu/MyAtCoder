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
import sys
input = sys.stdin.readline

N = int(input())
ST = {}
visit = set()
for i in range(N):
    S, T = input().split()
    ST[S] = T
for i in ST:
    loop=set()
    start_s = i
    start_t = ST[i]
    if start_t not in visit:
        next_s = start_s
        next_t = start_t        
        while True:
            if next_t not in ST: #next_tはそもそもSの中にないか、あるけどvisit済か、サイクル内か、サイクル外か
                visit |= loop
                break
            elif next_t in visit:
                visit |= loop
                break
            elif next_t in loop:
                print("No")
                exit()
            else:
                loop.add(next_s)
                next_s = next_t
                next_t = ST[next_s]
print("Yes")
