import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
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
N = int(input())
S = list(input())

x = 0
y = 0
visit = {"0,0"}
for i in range(len(S)):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1    
    elif S[i] == "D":
        y -= 1  
    result = str(x) +","+ str(y) 
    if result in visit:
        print("Yes")
        exit()
    else:
        visit.add(result)
print("No")
