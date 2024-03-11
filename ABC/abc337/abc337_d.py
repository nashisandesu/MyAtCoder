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
H, W, K = Mi()
data = [list(input()) for _ in range(H)]

ans = float('Inf')

yoko_sum_data = [[{'x':0,'.':0} for _ in range(W+1)] for _ in range(H+1)]

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if data[h-1][w-1] == 'x':
            yoko_sum_data[h][w]['x'] = yoko_sum_data[h][w-1]['x'] + 1
            yoko_sum_data[h][w]['.'] = yoko_sum_data[h][w-1]['.']
        elif data[h-1][w-1] == '.':
            yoko_sum_data[h][w]['x'] = yoko_sum_data[h][w-1]['x']
            yoko_sum_data[h][w]['.'] = yoko_sum_data[h][w-1]['.'] + 1
        else:
            yoko_sum_data[h][w]['x'] = yoko_sum_data[h][w-1]['x']
            yoko_sum_data[h][w]['.'] = yoko_sum_data[h][w-1]['.']         

for h in range(1, H+1):
    now = 1
    while True:
        start, end = now, now + K - 1
        if end > W:
            break
        else:
            x_num = yoko_sum_data[h][end]['x'] - yoko_sum_data[h][start - 1]['x']
            dot_num = yoko_sum_data[h][end]['.'] - yoko_sum_data[h][start - 1]['.']
            if x_num == 0:
                ans = min(ans, dot_num)
        now += 1

tate_sum_data = [[{'x':0,'.':0} for _ in range(W+1)] for _ in range(H+1)]

for w in range(1, W + 1):
    for h in range(1, H + 1):
        if data[h-1][w-1] == 'x':
            tate_sum_data[h][w]['x'] = tate_sum_data[h-1][w]['x'] + 1
            tate_sum_data[h][w]['.'] = tate_sum_data[h-1][w]['.']
        elif data[h-1][w-1] == '.':
            tate_sum_data[h][w]['x'] = tate_sum_data[h-1][w]['x']
            tate_sum_data[h][w]['.'] = tate_sum_data[h-1][w]['.'] + 1
        else:
            tate_sum_data[h][w]['x'] = tate_sum_data[h-1][w]['x']
            tate_sum_data[h][w]['.'] = tate_sum_data[h-1][w]['.']         

for w in range(1, W + 1):
    now = 1
    while True:
        start, end = now, now + K - 1
        if end > H:
            break
        else:
            x_num = tate_sum_data[end][w]['x'] - tate_sum_data[start - 1][w]['x']
            dot_num = tate_sum_data[end][w]['.'] - tate_sum_data[start - 1][w]['.']
            if x_num == 0:
                ans = min(ans, dot_num)
        now += 1
if ans == float('Inf'):
    print(-1)
else:
    print(ans)