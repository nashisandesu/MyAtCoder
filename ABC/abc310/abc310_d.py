import sys
sys.setrecursionlimit(100000)

N, T, M = map(int, input().split())
relation = [[1] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    relation[A - 1][B - 1] = 0
    relation[B - 1][A - 1] = 0

team = [[0]]

def solve(now_group, next_mem):
    global cnt
    if next_mem == N:
        if len(now_group) == T:
            cnt += 1
    else:
        for group in now_group:
            if all(relation[next_mem][now_mem] for now_mem in group):
                group.append(next_mem)
                solve(now_group, next_mem + 1)
                group.pop()
        if len(team) < T:
            now_group.append([next_mem])
            solve(now_group, next_mem + 1)
            now_group.pop()

cnt = 0
solve(team, 1)
print(cnt)
