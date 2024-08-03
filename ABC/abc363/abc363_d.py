import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
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
    
cnt_list = [10, 9]
for i in range(1, 20):
    cnt_list.append(9 * 10 ** i) 
    cnt_list.append(9 * 10 ** i)
sum_cnt_list = [0] * 100
sum_cnt_list[0] = cnt_list[0]
for i in range(1, len(cnt_list)):
    sum_cnt_list[i] = sum_cnt_list[i-1] + cnt_list[i]

N = I()
if N <= 10:
    print(N - 1)
    exit()
for i in range(100):
    if N <= sum_cnt_list[i]:
        break

keta = i + 1
rest = N - sum_cnt_list[i-1] - 1
half = 10 ** ((keta-1)//2) + rest
if keta % 2 == 0:
    ans = str(half) + str(half)[::-1]
else:
    half2 = half // 10
    ans = str(half2) + str(half)[-1] + str(half2)[::-1]
print(ans)