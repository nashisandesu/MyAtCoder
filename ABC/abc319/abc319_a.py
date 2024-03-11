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
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
ans = {'tourist': '3858', 'ksun48': '3679', 'Benq': '3658', 'Um_nik': '3648', 'apiad': '3638', 'Stonefeang': '3630', 'ecnerwala': '3613', 'mnbvmar': '3555', 'newbiedmy': '3516', 'semiexp': '3481'}

S = input()
print(ans[S])