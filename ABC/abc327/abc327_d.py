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
from collections import defaultdict 

N, M = Mi() 
graph = [[] for _ in range(N)]
A = Li()
B = Li()
for i in range(M):
    a,b = A[i]-1, B[i]-1

    graph[a].append(b)
    graph[b].append(a)

color = [0] * (N)

def dfs(v,c):
    color[v] = c
    for i in graph[v]:
        if color[i] == c:
            return False
        elif color[i] == 0 and not dfs(i, c * -1):
            return False
    return True

for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print('No')
            break
else:
    print('Yes')