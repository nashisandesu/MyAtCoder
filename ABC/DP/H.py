import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
# def go_right(h,w):
#     h += 1
#     w = w 
#     if h == H:
#         return False
#     if a[h][w] == '#':
#         return False
#     else:
#         dp[h][w] += dp[h-1][w]
#         return True

# def go_down(h, w):
#     h = h
#     w += 1 
#     if w == W:
#         return False
#     if a[h][w] == '#':
#         return False
#     else:
#         dp[h][w] += dp[h][w-1]
#         return True
    
# H, W = Mi()
# a = [list(input()) for _ in range(H)]
# dp = [[0] * W for _ in range(H)]
# dp[0][0] = 1
# visit = [[0] * W for _ in range(H)]
# todo = deque()
# todo.append((0,0))

# while todo:
#     h, w = todo.popleft()
#     if visit[h][w]:
#         continue
#     else:
#         visit[h][w] = 1
#     if go_right(h, w):
#         todo.append((h + 1, w))
#     if go_down(h, w):
#         todo.append((h, w + 1))
# mod = 10**9 + 7
# print(dp[-1][-1] % mod)

#単に和でdpできる
H, W = Mi()
a = [list(input()) for _ in range(H)]
dp = [[0] * (W + 1) for _ in range(H + 1)]
dp[1][1] = 1
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if h + w == 2:
            continue
        else:
            if a[h-1][w-1] == '#':
                dp[h][w] = 0
            else:
                dp[h][w] = dp[h-1][w] + dp[h][w-1]
mod = 10**9 + 7
print(dp[-1][-1] % mod)