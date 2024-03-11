import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
now = N
ans = 0
cnt = 0
big = N
while True:
    if big ==1 or big == 2:
        down = 2 ** cnt
        one = 2 * down - N
        two = down - one
        ans += 2* two
        break
    ans += N
    cnt += 1
    small = now // 2
    big = now-small
    now = big
print(ans)            
