import sys
sys.setrecursionlimit(100000)
from collections import deque

N, K = map(int, input().split())
data = {}
for i in range(N):
    a, b = map(int, input().split())
    data.setdefault(a, [])
    data[a].append(b)

sort_data =sorted(data.items(), reverse=True)
cnt = 0
for i in sort_data:
    day, num = i
    cnt += sum(num)
    if cnt > K:
        print(day + 1)
        sys.exit()
print(1)