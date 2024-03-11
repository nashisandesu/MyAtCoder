import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

def distance(A, B):
    return (A[0]-B[0]) ** 2 + (A[1]-B[1]) ** 2

N, D = map(int, input().split())
visit = [0] * N
visit[0] = 1
person = [tuple(map(int,input().split())) for _ in range(N)]
todo = deque()
todo.append(person[0])
while todo:
    virus = todo.pop()
    for i, v in enumerate(visit):
        if v == 0:
            if distance(person[i], virus) <= D**2:
                visit[i] = 1
                todo.append(person[i])
for v in visit:
    if v:
        print('Yes')
    else:
        print('No')
