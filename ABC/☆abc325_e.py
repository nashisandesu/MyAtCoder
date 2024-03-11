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
N, A, B, C = Mi()
D = [Mi() for _ in range(N)]
dp = [0] * N
todo = deque([0])
visit = [0] * N
while todo:
    now = todo.popleft()
    visit[now] = 1
    
