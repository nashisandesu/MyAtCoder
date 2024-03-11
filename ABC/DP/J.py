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
def f(one, two, three):
    if dp[one][two][three] != -1:
        return dp[one][two][three]
    ans = 1 / (float(one + two + three) / N)
    if one:
        ans += f(one - 1, two, three) * float(one) / N / (float(one + two + three) / N)
    if two:
        ans += f(one + 1, two - 1, three) * float(two) / N / (float(one + two + three) / N)
    if three:
        ans += f(one, two + 1, three - 1) * float(three) / N / (float(one + two + three) / N)
    dp[one][two][three] = ans
    return ans

N = I()
a = Li()
data = {1:0, 2:0, 3:0}
for i in range(N):
    data[a[i]] += 1

dp=[[[-1] * 301 for _ in range(301)]for _ in range(301)]
dp[0][0][0]=0

one, two, three = data[1], data[2], data[3]
print(f(one, two, three))