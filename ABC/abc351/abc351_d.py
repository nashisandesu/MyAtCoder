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
def can_move(h,w):
    for dh, dw in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and s[nh][nw] == '#':
            return False
    else:
        return True

H, W = Mi()
visited = [[False] * W for _ in range(H)]
s = [list(input()) for _ in range(H)]
ans = 1
for h in range(H):
    for w in range(W):
        if s[h][w] == '#':
            continue
        elif not can_move(h, w):
            s[h][w] = 'x'
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        elif s[i][j] == '.':
            todo = [(i, j)]
            cnt = 0
            move = set()
            while todo:
                h, w = todo.pop()
                if (h, w) in move:
                    continue
                move.add((h, w))
                visited[h][w] = True
                cnt += 1
                if s[h][w] == '.':
                    for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nh, nw = h + dh, w + dw
                        if 0 <= nh < H and 0 <= nw < W:
                            todo.append((nh, nw))
            ans = max(ans, cnt)
print(ans)