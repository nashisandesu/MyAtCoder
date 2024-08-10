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
s = list(input())
if not s[0].isupper() or not s[-1].isupper() or len(s) != 8:
    print('No')
else:
    num = ''.join(s[1:-1])
    try:
        num = int(num)
    except:
        print('No')
        exit()
    if 100000 <= num <= 999999:
        print('Yes')
    else:
        print('No')