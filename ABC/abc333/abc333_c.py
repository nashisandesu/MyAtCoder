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
N = I()
ans = set()
for i in range(12):
    for j in range(12):
        for k in range(12):
            value_i = int(''.join(['1'] * (i+1)))
            value_j = int(''.join(['1'] * (j+1)))
            value_k = int(''.join(['1'] * (k+1)))
            ans.add(value_i+value_j+value_k)
ans_list = list(ans)
ans_list.sort()
print(ans_list[N-1])