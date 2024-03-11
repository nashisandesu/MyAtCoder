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
'''
N = I()
visit = {}
for _ in range(N):
    S, C = M()
    c = bin(C)[2:]
    for j in range(len(c)):
        num = c[j]
        if num == '1':
            temp = len(c) - j - 1
            while visit.get(S * (2 ** temp), 0) == 1:
                visit[S * (2 ** temp)] = 0
                temp += 1
            else:
                visit[S * (2 ** temp)] = 1
print(visit)
print(sum(visit.values()))
'''
import heapq
N = I()
Q = [tuple(map(int, input().split())) for _ in range(N)]
heapq.heapify(Q)
print(Q)