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
def prime_factorize(n):
    a = {}
    while n % 2 == 0:
        a.setdefault(2, 0)
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.setdefault(f,0)
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a.setdefault(n,0)
        a[n] += 1
    return a

A, B = Mi()
mod = 998244353
pf = prime_factorize(A)
cnt = 1
print(pf)
for value in pf.values():
    cnt *= (B * value + 1)
print((cnt * B //2)% mod)