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
N = I()
S = list(input())
past = S[0]
cnt = 1
ans = 0
strdic = {}
if N == 1:
    print(1)
    exit()
for i in range(1, N):
    if past == S[i]:
        cnt += 1
        if i == N-1:
            if strdic.get(past, 0) < cnt:
                ans += cnt - strdic.get(past, 0)
                strdic.setdefault(past, 0)
                strdic[past] = cnt   
        else:         
            continue
    else:
        if strdic.get(past, 0) < cnt:
            ans += cnt - strdic.get(past, 0)
            strdic.setdefault(past, 0)
            strdic[past] = cnt
        cnt = 1
        past = S[i]
print(ans)