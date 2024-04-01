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
#遅延セグ
def op(data1, data2):
    return data1 ^ data2

def mapping(lazy_upper, data_lower):
    return data_lower + lazy_upper

def composition(lazy_upper, lazy_lower):
    return lazy_upper + lazy_lower

A = [1,2,3,4,5]
l_st = LazySegTree(op=min, e=float('Inf'), mapping=lambda f, x: f+x, composition= lambda f, g: f + g, id_ = 0, v = A)
#恒等写像 id とは、全ての a に対してmapping(id, a) = a となるものを指します。

#ダイクストラ
N = I()
data = [0]
for _ in range(N-1):
    data.append(Li())
todo = []
heapq.heappush(todo,(data[1][0], 2)) #距離と番号のタプル
heapq.heappush(todo,(data[1][1], data[1][2]))
visit = [0] * (N + 1)
visit[1] = 1
while todo:
    dist, stage = heapq.heappop(todo)
    if visit[stage] == 1:
        continue
    else:
        visit[stage] = 1
    if stage == N:
        print(dist)
        break
    A, B, X = data[stage]
    if not visit[stage + 1]:
        heapq.heappush(todo,(dist+A, stage+1))
    if not visit[X]:
        heapq.heappush(todo,(dist+ B, X))

#メモ化
from functools import cache
@cache
def f(N):
    return 0 if N == 1 else f(N // 2) + f((N + 1) // 2) + N
print(f(int(input())))

#dfs
H, W = Mi()
used = [[False for _ in range(W)] for _ in range(H)]
def dfs(cur) :
    used[cur] = True
    for e in node[cur]:
        if used[e] == False :
            dfs(e)

#bfs
inf = 10**9
dist = [inf for _ in range(N)]
node = [[] for _ in range(N)]

dist[0] = 0
q = deque([0])

while len(q) != 0 :
    cur = q[0]
    q.popleft()
    for e in node[cur]:
        if dist[e] > dist[cur] + 1 :
            dist[e] = dist[cur]+1
            q.append(e)

#素因数分解
"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) 

## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1

#約数の列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]