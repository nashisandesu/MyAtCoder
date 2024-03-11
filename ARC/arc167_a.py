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
N, M = Mi()
A = Li()
two = 2* M - N
A = deque(sorted(A))
ans = 0
for _ in range(two):
    A.appendleft(0)
for i in range(M):
    a = A.popleft()
    b = A.pop()
    ans += (a+b) ** 2
print(ans)