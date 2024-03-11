import sys, bisect
import math
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
cnt = 0
for i in combinations(range(H + W - 2), H - 1):
    now = set()
    now.add(A[0][0])
    h, w = 0, 0
    for j in range(H + W - 2):
        if j in i:
            h += 1
        else:
            w += 1
        if A[h][w] not in now:
            if j == H + W - 3:
                cnt += 1
            else:
                now.add(A[h][w])
        else:
            break
print(cnt)
