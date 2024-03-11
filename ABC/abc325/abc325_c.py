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
H, W = Mi()
S = [list(input()) for _ in range(H)]
sensor = [[0] * W for _ in range(H)]
visit = [[0] * W for _ in range(H)]
todo = deque()
pos = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
ans = 0
def search(x,y):
    for dx, dy in pos:
        if 0 <= x + dx <= H - 1 and 0 <= y+ dy <= W - 1:
            if visit[x+dx][y+dy]:
                continue
            else:
                visit[x+dx][y+dy] = 1
                if S[x+dx][y+dy] == '#':
                    search(x+dx,y+dy)

for i in range(H):
    for j in range(W):
        if S[i][j]== '#':
            if visit[i][j] == 0:
                visit[i][j] = 1
                search(i,j)
                ans += 1

print(ans)