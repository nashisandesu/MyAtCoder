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
S = list(input())
now = S[0]

for i in range(1, len(S)):
    if now == 'A':
        if S[i] == 'B':
            now = 'B'
        elif S[i] == 'C':
            now = 'C'
    elif now == 'B':
        if S[i] == 'A':
            print('No')
            break
        elif S[i] == 'C':
            now = 'C'
    else:
        if S[i] != 'C':
            print('No')
            break
else:
    print('Yes')