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
S = input()
data = {}
for s in S:
    data.setdefault(s,0)
    data[s] += 1

now = 0
ans = 'z'

for key, value in data.items():
    if value > now:
        ans = key
        now = value
    elif value == now:
        if key < ans:
            ans = key
print(ans)
