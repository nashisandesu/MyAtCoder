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
people = [0] * (N + 1)
nowmax = 0
nowpeople = N + 2
for i in range(M):
    people[A[i]] += 1
    if nowmax == people[A[i]]:
        if nowpeople >= A[i]:
            nowmax = people[A[i]]
            nowpeople = A[i]
    elif nowmax < people[A[i]]:
        nowmax = people[A[i]]
        nowpeople = A[i]
    print(nowpeople)

