import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations
import heapq

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, K = Mi()
a = Li()
dp = [-1] * (K + 1) #i番目の石を取った人が勝てるか
for i in range(1, K + 1):
    if dp[i] == -1:
        dp[i] = True
        for j in range(N):
            if i + a[j] <= K:
                dp[i + a[j]] = False
for i in range(N):
    if K - a[i] + 1 > 0 and dp[K - a[i] + 1]:
        print("First")
        break
else:
    print('Second')
