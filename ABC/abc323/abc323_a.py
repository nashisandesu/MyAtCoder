import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
M = lambda: map(int, input().split())
I_L = lambda: list(map(int, input().split()))
S_L = lambda: list(map(int, input().split()))

########################################################
S = list(input())
for i in range(16):
    if i % 2:
        if int(S[i]) % 2 == 1:
            print('No')
            break
else:
    print('Yes')