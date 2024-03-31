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
a, b, C = Mi()
c = list(bin(C)[2:])
c = ['0'] * (60 - len(c)) + c
# x = c ^ y
c_popcount = c.count('1')
y = ['0'] * 60
    
max_one =  min(120 - (c_popcount + b), c_popcount + b)
min_one = abs(c_popcount - b)
if min_one <= a <= max_one and a % 2 == min_one % 2:
    kaburi_cnt = 0
    b_cnt = 0
    kaburi = (c_popcount + b - a) // 2
    for i in reversed(range(60)):
        if kaburi_cnt < kaburi and c[i] == '1':
            y[i] = '1'
            kaburi_cnt += 1
            b_cnt += 1
    for i in reversed(range(60)):
        if b_cnt < b and c[i] == '0':
            y[i] = '1'
            b_cnt += 1
    
    ans_y = int(''.join(y), 2)
    ans_x = C ^ ans_y
    print(ans_x, ans_y)
else:
    print('-1')