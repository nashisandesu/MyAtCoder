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
N = I()
A = Li()
right = A[0]
right_idx = 0
flag = 0
# for i in range(1, N):
#     if flag == 0:
#         if right < A[i]:
#             pass
#         elif right == A[i]:
#             middle = A[i]
#             cnt = 1
#     elif flag == 1:

#     elif flag == 2:
    