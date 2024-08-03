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
N = I()
s = input()
t = input()
if s.count('B') != t.count('B'):
    print(-1)
    exit()

visit = set()
visit.add(s + '..')
todo = deque()
todo.append([list(s + '..'), 0])
while todo:
    state, cnt = todo.popleft()
    # ここに書かないとs=tのケースで出力が2になる
    if state[:N] == list(t):
        print(cnt)
        exit()
    for i in range(N+1):
        if state[i] != '.' and state[i+1] != '.':
            for j in range(N+1):
                if state[j] == '.' and state[j+1] == '.':
                    next = state[:]
                    next[j] = state[i]
                    next[j+1] = state[i+1]
                    next[i] = '.'
                    next[i+1] = '.'
                    next_str = ''.join(next)
                    if next_str not in visit:
                        visit.add(next_str)
                        todo.append([next, cnt+1])   
                    break 
else:
    print(-1)

