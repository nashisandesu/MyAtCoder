import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
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

#######################################################
N, M = Mi()
A = Li()
B = Li()

#遅延セグ
def mapping(lazy_upper, data_lower):
    return data_lower + lazy_upper

def composition(lazy_upper, lazy_lower):
    return lazy_upper + lazy_lower

l_st = LazySegTree(op=min, e=float('Inf'), mapping=lambda f, x: f+x, composition= lambda f, g: f + g, id_ = 0, v = A)
for i in range(M):
    cnt =  l_st.get(B[i])
    l_st.set(B[i],0)
    if cnt != 0:
        sho, amari = cnt // N, cnt % N
        if sho > 0:
            l_st.apply(0, N, sho)
        if B[i] + 1 + amari > N:
            l_st.apply(B[i] + 1, N, 1)
            l_st.apply(0, B[i] + 1 + amari - N, 1)
        else:
            l_st.apply(B[i] + 1, B[i] + 1 + amari, 1)

ans = []
for j in range(N):
    ans.append(l_st.get(j))
print(' '.join(map(str,ans)))

#セグ＋imos
sa_A = [0] * (N+1)
sa_A[0] = A[0]
for i in range(1, N):
    sa_A[i] = A[i] -A[i-1]
def op(a,b):
    return a+b
st = SegTree(op=op, e=0, v=sa_A) 
for b in B:
    ball = st.prod(0, b + 1)
    sho, amari = divmod(ball, N)
    st.set(b, st.get(b) - ball)
    st.set(b + 1, st.get(b+1) + ball)
    if sho > 0:
        st.set(0, st.get(0) + sho)
    if amari > 0:
        if amari + b > N - 1:
            st.set(b + 1, st.get(b + 1) + 1)
            st.set(0, st.get(0) + 1)
            st.set(b + amari + 1 - N, st.get(b + amari + 1 - N) - 1)
            pass
        else:
            st.set(b + 1, st.get(b + 1) + 1)
            st.set(b + amari + 1, st.get(b + amari + 1) - 1)
for i in range(N):
    print(st.prod(0,i+1), end=' ')
print()
    