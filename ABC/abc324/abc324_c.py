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

N, T = Ms()
T = list(T)
t_len = len(T)
ans = []
for n in range(int(N)):
    S = list(input())
    s_len = len(S)
    if s_len == t_len:
        cnt = 0
        for i in range(t_len):
            if S[i] != T[i]:
                if cnt == 1:
                    break
                else:
                    cnt += 1
        else:
            ans.append(n+1)
    elif s_len + 1 == t_len:
        cnt = 0
        for i in range(s_len):
            if S[i] != T[i + cnt]:
                if cnt == 1:
                    break
                else:
                    cnt += 1
                    if S[i] != T[i + cnt]:
                        break
        else:
            ans.append(n+1)

    elif s_len == t_len + 1:
        cnt = 0
        for i in range(t_len):
            if S[i + cnt] != T[i]:
                if cnt == 1:
                    break
                else:
                    cnt += 1
                    if S[i + cnt] != T[i]:
                        break
        else:
            ans.append(n+1)
print(len(ans))
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i])
    else:
        print(ans[i], end = " ")
if len(ans) == 0:
    print()


