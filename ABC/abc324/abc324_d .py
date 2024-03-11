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
N = I()
S = list(input())
S.sort(reverse=True)
s_dic = {}
for i in range(N):
    s_dic.setdefault(S[i], 0)
    s_dic[S[i]] += 1
max_s = int(''.join(S))
cnt = 0
ans = 0
while (cnt * cnt <= max_s):
    now = cnt * cnt
    new_dic = s_dic.copy()
    for i in range(N):
        s = now % 10
        num = new_dic.get(str(s), 0)      
        if num != 0:
            new_dic[str(s)] -= 1
            now //= 10
        else:
            break
    else:
        ans += 1
    cnt += 1
print(ans)