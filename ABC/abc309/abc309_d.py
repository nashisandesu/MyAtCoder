import sys
sys.setrecursionlimit(100000)
from collections import deque

N1, N2, M = map(int, input().split())
edge = [[] for _ in range(N1 + N2)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

def max_edge(node):
    todo = deque()
    todo.append(node)
    group = [-1] * (N1 + N2)
    group[node] = 0
    while todo:
        now = todo.popleft()
        for node in edge[now]:
            if group[node] == -1:
                group[node] = group[now] + 1
                todo.append(node)
    return max(group)
print(max_edge(0) + max_edge(N1 + N2 - 1) + 1)