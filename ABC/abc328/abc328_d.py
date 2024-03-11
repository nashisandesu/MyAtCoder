import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
S = list(input())

q = deque(S)
ans = deque()
length = 0
while q:
    q3 = q.popleft()
    if len(ans) >= 2 and q3 == 'C':
        q2 = ans.pop()
        q1 = ans.pop()
        if q1 == "A" and q2 == "B" and q3 == "C":
            continue
        ans.append(q1)
        ans.append(q2)
        ans.append(q3)
    else:
        ans.append(q3)
print(''.join(ans))