import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

W, H = map(int, input().split())
N = int(input())
pq = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))
ichigo = {}
for p, q in pq:
    left = bisect.bisect_left(a, p)
    down = bisect.bisect_left(b, q)
    ichigo.setdefault((left, down), 0)
    ichigo[(left, down)] += 1
print(min(ichigo.values()) if len(ichigo) == (A+1)*(B+1) else 0, max(ichigo.values()))
