import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
from atcoder.scc import SCCGraph
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
from collections import defaultdict
N = I()
a = list(map(lambda x: x-1, Li()))
graph = SCCGraph(N)
for i in range(N):
    graph.add_edge(i, a[i])
matome = graph.scc()
idx = defaultdict()
for i in range(len(matome)):
    for x in matome[i]:
        idx[x] = i 
ans = 0
for nodes in matome:
    if len(nodes) != 1:
        ans += len(nodes) * (len(nodes) - 1)
    else:
        cnt = 0
        now = nodes[0]
        while True:
            to = a[now]
            if to == now:
                break
            elif len(matome[idx[to]]) == 1:
                cnt += 1
                now = to
            else:
                cnt += len(matome[idx[to]])
                break
        ans += cnt
print(ans+N)