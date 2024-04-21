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
N, Q = Mi()
first = [(i + 1, 0) for i in range(N)]
head_x, head_y = 1, 0
move = deque()
for _ in range(Q):
    num, key = Ms()
    if num == '1':
        if key =='R':
            head_x += 1
        elif key == 'L':
            head_x -= 1
        elif key =='U':
            head_y += 1
        elif key == 'D':
            head_y -= 1
        move.append((head_x, head_y))
    else:
        if int(key) <= len(move):
            print(move[- int(key)][0], move[- int(key)][1])
        else:
            print(first[int(key) - 1 - len(move)][0], first[int(key) - 1 - len(move)][1])
