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
N, K = Mi()
A = Li()
half = N // 2

def bit_all_search(L: list):
    sum_list = []
    for i in range(2**len(L)):
        sum = 0
        for j in range(len(L)):
            bit = (i // (2**j)) % 2
            sum += bit * L[j]
        sum_list.append(sum)
    return sum_list

L1 = A[:half]
L2 = A[half:]
L1_sum = bit_all_search(L1)
L2_sum = set(bit_all_search(L2))

for h in L1_sum:
    if K - h in L2_sum:
        print('Yes')
        break
else:
    print('No')