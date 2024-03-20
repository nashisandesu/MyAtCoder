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
def operation(x):
    num = 0
    for i in range(20):
        num += (8 ** i) * x[i]
    for j in range(20):
        sho, amari = divmod(num, 9)
        if amari == 8:
            amari = 5
        data[j] = amari
        num = sho

N, K = Mi()
data = [0] * 20
for i in range(20):
    data[i] = N % 10
    N //= 10

for _ in range(K):
    operation(data)

for i in reversed(range(20)):
    if data[i]:
        print(''.join(map(str, reversed(data[:i+1]))))
        break
else:
    print(0)