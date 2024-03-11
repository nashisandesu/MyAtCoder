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
H, W = Mi()
A = np.array([Li() for _ in range(H)])
B = np.array([Li() for _ in range(H)])
Hlist = []
Wlist = []
Huse = set()
Wuse = set()
for i in range(H):
    first = A[i, 0]
    for j in range(H):
        if first in B[j]:
            if sorted(A[i]) == sorted(B[j]) and j not in Huse:
                Hlist.append(j)
                Huse.add(j)
                break
    else:
        print(-1)
        exit()

for i in range(W):
    first = A[0, i]
    for j in range(W):
        if first in B[:, j]:
            if sorted(A[:, i]) == sorted(B[:, j]) and j not in Wuse:
                Wlist.append(j)
                Wuse.add(j)
                break
    else:
        print(-1)
        exit()

swap = 0

for i in range(H):
    swap += Hlist.index(i) - i
    Hlist.remove(i)
    Hlist.insert(i,i)

for i in range(W):
    swap += Wlist.index(i) - i
    Wlist.remove(i)
    Wlist.insert(i,i)

print(swap)
