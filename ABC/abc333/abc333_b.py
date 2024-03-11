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
datas = list(input())
s1, s2 = datas
datat = list(input())
t1, t2 = datat

s_ord = abs(ord(s1) - ord(s2))
t_ord = abs(ord(t1) - ord(t2))

s_dis = min(5 - s_ord, s_ord)
t_dis = min(5 - t_ord, t_ord)

print('Yes' if s_dis == t_dis else 'No')
