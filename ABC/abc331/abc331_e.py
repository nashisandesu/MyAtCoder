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
N,M,L = Mi()
A = Li()
B = Li()
B_sort = sorted([(p, j) for j, p in enumerate(B)], reverse=True)
ng = set([tuple(map(int, input().split())) for _ in range(L)])
ans = 0
for i in range(N):
    for j in range(M):
        if (i+1, B_sort[j][1]+1) not in ng:
            ans = max(ans, A[i] + B_sort[j][0])
            break
print(ans)
