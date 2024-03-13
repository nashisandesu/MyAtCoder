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
A = [0] + Li()
l, r = [0] * (N + 2), [0] * (N + 2) #l[i]はi番目を頂上とした時の左側ピラミッドの最長
for i in range(1, N + 1):
    l[i] = min(A[i], l[i-1] + 1)
for i in reversed(range(1, N + 1)):
    r[i] = min(A[i], r[i+1] + 1)

print(max(min(l[i], r[i]) for i in range(1, N+1)))