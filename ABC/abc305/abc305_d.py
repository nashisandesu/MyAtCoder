import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
S = [0] * N
for i in range(1, N):
    if i % 2:
        S[i] = S[i - 1]
    else:
        S[i] = S[i - 1] + A[i] - A[i-1]
ans = []
for _ in range(Q):
    cnt = 0
    l, r = map(int, input().split())
    j = bisect.bisect_left(A, l)
    k = bisect.bisect_left(A, r)
    cnt = S[k-1] - S[j]
    if not j % 2:
        cnt += A[j] - l
    if not k % 2:
        cnt += r - A[k-1]
    ans.append(cnt)
for v in ans:
    print(v)