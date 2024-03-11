import sys, bisect
import math
import numpy as np
from atcoder.lazysegtree import LazySegTree
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, M = Mi()
X = Li()

'''
#imos法

#d[i]は(dのiまでの累積和を取れば)橋iを封鎖した時の距離
d = [0] * (N + 1)
for i in range(M-1):
    l, r = min(X[i],X[i+1]),max(X[i],X[i+1])
    # l〜rで橋が封鎖されていない場合の距離
    dist = r - l
    #1~lとr~Nは距離k, l~rは距離Nーk
    d[1] += dist
    d[l] += N - 2 * dist
    d[r] -= N - 2 * dist

ans = float('INF')
for i in range(1, N + 1):
    d[i] += d[i-1]
    ans = min(d[i], ans)

print(ans)

'''

#遅延セグ
def op(data1, data2):
    return min(data1, data2)

e = float('Inf')

def mapping(lazy_upper, data_lower):
    return data_lower + lazy_upper

def composition(lazy_upper, lazy_lower):
    return lazy_upper + lazy_lower

_id = 0

dist = [0] * (N + 1)

l_st = LazySegTree(op, e, mapping, composition, _id, dist)
for i in range(M-1):
    left, right = min(X[i], X[i+1]), max(X[i], X[i+1])
    l_st.apply(1, left, right - left)
    l_st.apply(left, right, N - (right - left))
    l_st.apply(right, N + 1, right - left)      
print(l_st.prod(1, N + 1))