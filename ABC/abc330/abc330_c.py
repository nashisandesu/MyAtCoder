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
D = I()
maxd = int((D)**0.5) + 1
xy = [0] * (maxd+1)
for i in range(1, maxd + 1):
    xy[i] = i * i

now = D

for i in range(1, maxd + 1):
    x = xy[i]
    yidx = bisect.bisect_left(xy, D-x)
    ans1 = abs(D - x - xy[yidx])
    ans2 = abs(D - x - xy[yidx - 1])
    if ans1 < now:
        now = ans1
    if ans2 < now:
        now = ans2
    if yidx < i:
        break
print(now)