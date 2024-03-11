import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
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
N, D = Mi()
A = Li()
NUM = 5 * 10 ** 5 + 1
dp = [0] * NUM #
st = SegTree(max, 0, dp)
for i in range(N):
    num = st.prod(max(A[i] - D, 0), min(A[i] + D + 1, NUM)) #A[i]番目の数字を既にA[i-1]までで作った部分列にくっつけようとする
    st.set(A[i], num + 1) #A[i]自身

print(st.prod(0, NUM))