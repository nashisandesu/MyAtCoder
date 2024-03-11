import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
D = Li()
data = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
cnt = 0
for i in range(N):
    if (i+1) in data:
        one = (i+1) % 10
        if D[i] >= (one) * 10 + (one):
            cnt += 2
        elif D[i] >= (one):
            cnt += 1
print(cnt)