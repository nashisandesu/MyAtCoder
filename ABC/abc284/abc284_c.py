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
import numpy as np
N, M = map(int, input().split())
rinsetsu = np.array([[0] * N ] * N)
visit = [False]*N
for i in range(M):
    v1, v2 = map(int, input().split())
    rinsetsu[v1-1][v2-1] = 1
    rinsetsu[v2-1][v1-1] = 1
ans = 0
def tansaku(j):
    for k in range(N):
        if rinsetsu[j][k] == 1:
            visit[k] = True
            if k not in motto:
                motto.add(k)
                tansaku(k)

for j in range(N):
    if visit[j] == False:
        ans += 1
        visit[j] = True
        motto = {j}
        tansaku(j)

print(ans)