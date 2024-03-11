import sys, bisect
import math
import numpy as np
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
def check(known):
    for i in range(3):
        if check2(known[i][0], known[i][1], known[i][2]) or check2(known[0][i], known[1][i], known[2][i]):
            return True
    if check2(known[0][0], known[1][1], known[2][2]):
        return True
    if check2(known[0][2], known[1][1], known[2][0]):
        return True
    return False

def check2(a,b,c):
    if [a,b,c].count(-1) == 1 and len(set([a,b,c])) == 2:
        return True
    else:
        return False
c = [Li() for _ in range(3)]
cnt = 0
for random in permutations(range(9), 9):
    known = [[-1] * 3 for i in range(3)]
    for now in random:
        h, w = divmod(now, 3)
        known[h][w] = c[h][w]
        if check(known):
            cnt += 1
            break
print(1 - cnt/(9*8*7*6*5*4*3*2))        