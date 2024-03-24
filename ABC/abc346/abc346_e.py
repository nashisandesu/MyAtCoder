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
H, W , M = Mi()
paint = [Li() for _ in range(M)]
past_1 = set()
past_2 = set()
ans = {0: H * W}
for t, a, x in reversed(paint):
    if t == 1 and a not in past_1:
        ans.setdefault(x, 0)
        ans[x] += W - len(past_2)
        ans[0] -= W - len(past_2)
        past_1.add(a)
    elif t == 2 and a not in past_2:
        ans.setdefault(x, 0)
        ans[x] += H - len(past_1)
        ans[0] -= H - len(past_1)
        past_2.add(a)
ans = sorted(ans.items())
last_ans = []

for i in range(len(ans)):
    if ans[i][1] == 0:
        continue
    else:
        last_ans.append(ans[i])

print(len(last_ans))
for i in last_ans:
    print(*i)
