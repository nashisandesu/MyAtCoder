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
# 共通
N, M = Mi()
A = Li()
A.sort()

# 二分探索
def is_ok(arg):
    idx = bisect.bisect_left(A, arg) 
    money = sum_A[idx] + arg * (N - idx)
    return money <= M

def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

if M >= sum(A):
    print('infinite')
else:
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    ok, ng = 0, 10 ** 15
    ans = meguru_bisect(ng, ok)
    print(ans)


# 線形探索
if M >= sum(A):
    print('infinite')
else:
    ans = 0 
    sum_A = 0
    for i in range(N):
        ans = max(ans, (M - sum_A) // (N - i))
        sum_A += A[i]
    print(ans)