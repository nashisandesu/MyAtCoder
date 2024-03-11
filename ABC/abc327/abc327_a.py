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
S = input()
for s in range(N-1):
    if S[s] == 'a' and S[s+1] == 'b':
        print('Yes')
        break
    elif S[s] == 'b' and S[s+1] == 'a':    
        print('Yes')
        break
else:
    print('No')