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
from functools import cache
@cache
def f(h,w):
    if h == -1 or h == H or w == -1 or w == W:
        return False
    elif h != 0 and s[h-1][w] == '#':
        return False
    elif h != H-1 and s[h+1][w] == '#':
        return False
    elif w != 0 and s[h][w-1] == '#':
        return False
    elif w != W -1 and s[h][w+1] == '#':
        return False
    else:
        return True

H, W = Mi()
s = [input() for _ in range(H)]
check = [[1] * (W + 1) for _ in range(H + 1)]
check = [[0 if h != H and w != W else 1 for w in range(W+1)] for h in range(H+1)]
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            check[i][j] = 1
ans = 0
for i in range(H):
    for j in range(W):
        visit = [[1] * (W + 1) for _ in range(H + 1)]
        visit = [[0 if h != H and w != W else 1 for w in range(W+1)] for h in range(H+1)]
        if check[i][j] == 0:
            todo = deque()
            todo.append((i, j))
            cnt = 1
            visit[i][j] = 1

            while todo:
                h, w = todo.pop()
                if f(h,w):
                    if visit[h + 1][w] == 0:
                        cnt += 1
                        visit[h + 1][w] = 1
                        check[h + 1][w] = 1
                        todo.append((h+1, w))
                    if visit[h - 1][w] == 0:
                        cnt += 1
                        visit[h - 1][w] = 1
                        check[h - 1][w] = 1
                        todo.append((h-1, w))
                    if visit[h][w+1] == 0:
                        cnt += 1
                        visit[h][w + 1] = 1
                        check[h][w + 1] = 1
                        todo.append((h, w+1))
                    if visit[h][w-1] == 0:
                        cnt += 1
                        visit[h][w - 1] = 1
                        check[h][w - 1] = 1
                        todo.append((h, w-1))
            ans = max(ans, cnt)
print(ans)