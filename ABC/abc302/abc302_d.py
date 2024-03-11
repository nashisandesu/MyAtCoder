import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
value_max = -1
for a in reversed(A):
    ok = a + D
    index = bisect.bisect_right(B, ok)
    if index != 0 and B[index - 1] >= a - D:
        if value_max < a + B[index - 1]:
            value_max = a + B[index - 1]
print(value_max)