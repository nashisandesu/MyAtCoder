import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

N, Q = map(int, input().split())
cnt = 1
call = deque()
go = set()
for _ in range(Q):
    e, *x = map(int, input().split())
    if e == 1:
        call.append(cnt)
        cnt += 1
    elif e == 2:
        go.add(x[0])
    else:
        while True:
            x = call.popleft()
            if x not in go:
                print(x)
                call.appendleft(x)
                break

