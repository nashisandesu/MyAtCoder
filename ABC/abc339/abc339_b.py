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
data = [['.'] * W for _ in range(H)]
yoko = 0
tate = 0
d_list = [(-1, 0),(0,1),(1,0),(0,-1)]
d = 0
for i in range(N):
    if data[yoko][tate] == '.':
        data[yoko][tate] = '#'
        d += 1
    else:
        data[yoko][tate] = '.'
        d -= 1

    d %= 4
    yoko += d_list[d][0]
    tate += d_list[d][1]
    yoko %= H
    tate %= W
for i in range(H):
    print(''.join(data[i]))
