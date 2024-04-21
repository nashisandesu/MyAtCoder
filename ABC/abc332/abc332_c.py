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
# S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, M = Mi()
S = list(input())
needlogo = 0
useT = 0
uselogo = 0
for day in S:
    if day == '0':
        nowneed = uselogo
        if useT > M:
            uselogo += useT - M
        
        if uselogo > needlogo:
            needlogo = uselogo
        
        useT = 0
        uselogo = 0
    elif day == '1':
        useT += 1
    elif day == '2':
        uselogo += 1
    else:
        print('error')
if day != '0':
    nowneed = uselogo
    if useT > M:
        uselogo += useT - M
    
    if uselogo > needlogo:
        needlogo = uselogo    
print(needlogo)

