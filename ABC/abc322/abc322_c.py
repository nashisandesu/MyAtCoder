import sys,bisect
sys.setrecursionlimit(100000)
from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    date = bisect.bisect_left(A, i+1)
    print(A[date] - i - 1)