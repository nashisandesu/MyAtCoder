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
def create_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row, col = 0, 0
    direction = 0
    for i in range(1, n * n + 1):
        matrix[row][col] = i
        new_row = row + directions[direction][0]
        new_col = col + directions[direction][1]
        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n or matrix[new_row][new_col] != 0:
            direction = (direction + 1) % 4  
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]
        row, col = new_row, new_col

    return matrix
N = I()
spiral_matrix = create_spiral_matrix(N)
spiral_matrix[(N+1)//2 - 1][(N+1)//2 - 1] = 'T'
for i in range(N):
    print(' '.join(map(str,spiral_matrix[i])))