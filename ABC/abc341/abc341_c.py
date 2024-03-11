import sys, bisect
import math
import numpy as np
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
H, W, N = Mi()
T = list(input())
mapS = [list(input()) for _ in range(H)]
cnt = 0
for w in range(1, W-1):
    for h in range(1, H-1):
        noww, nowh = w, h
        if mapS[nowh][noww] == '#':
            continue
        for i in range(N):
            if T[i] == 'L':
                noww -= 1
            elif T[i] == 'R':
                noww += 1
            elif T[i] == 'U':
                nowh -= 1
            else:
                nowh += 1
            if mapS[nowh][noww] == '#':
                break
        else:
            cnt += 1

print(cnt)
