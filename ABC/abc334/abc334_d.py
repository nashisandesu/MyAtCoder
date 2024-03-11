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
R = Li()
R.sort()
# print(R)
sum_list = [0] * (N + 1)
for i in range(1, N + 1):
    sum_list[i] = sum_list[i - 1] + R[i - 1]
for _ in range(Q):
    q = I()
    print(bisect.bisect_right(sum_list, q) - 1)


