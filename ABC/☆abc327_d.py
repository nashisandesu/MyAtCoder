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
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
#Union-find未完成
N, M = Mi()
A = Li()
B = Li()

uf = UnionFind(N)
todo = deque()
graph = [[] for _ in range(N)]

for i in range(M):
    a, b = A[i] - 1, B[i] - 1
    graph[a].append(b)
    graph[b].append(a)

x, y = A[0] - 1, B[0] - 1
todo.append(x)
todo.append(y)
visit = [0] * N
visit[x] = 1
visit[y] = 1
while todo:
    now = todo.pop()
    for v in graph[now]:
        if uf.same(now, v):
            print('No')
            exit()
        elif uf.same(now, x):
            uf.union(v, y)
        else:
            uf.union(v, x)
        
        if visit[v] == 0:
            visit[v] = 1
            todo.append(v)
print('Yes')
            
#dfs
N, M = Mi() 
graph = [[] for _ in range(N)]
A = Li()
B = Li()
for i in range(M):
    a,b = A[i]-1, B[i]-1

    graph[a].append(b)
    graph[b].append(a)

color = [0] * (N)

def dfs(v,c):
    color[v] = c
    for i in graph[v]:
        if color[i] == c:
            return False
        elif color[i] == 0 and not dfs(i, c * -1):
            return False
    return True

for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print('No')
            break
else:
    print('Yes')