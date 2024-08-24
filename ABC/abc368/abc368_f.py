import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
def can_Anna_win(sequence):
    xor_sum = 0
    for num in sequence:
        xor_sum ^= num
    
    return xor_sum != 0

def factorization_cnt(n):
    arr = []
    temp = n
    ans = 0
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            ans += cnt

    if temp!=1:
        arr.append([temp, 1])
        ans += 1

    if arr==[]:
        arr.append([n, 1])
        ans += 1
    return ans

N = I()
A = Li()
for i in range(N):
    A[i] = factorization_cnt(A[i])

if can_Anna_win(A):
    print("Anna")
else:
    print("Bruno")
