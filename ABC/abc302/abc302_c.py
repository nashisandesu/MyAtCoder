import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque
import itertools

N, M = map(int, input().split())
p_list = list(itertools.permutations(range(N)))
S = [list(input()) for _ in range(N)]
for p in p_list:
    past = S[p[0]]
    for i in range(N - 1):
        now = S[p[i + 1]]
        cnt = 0
        check = 0
        for j in range(M):
            if past[j] != now[j]:
                if cnt == 1:
                    check = 1
                    break
                else:
                    cnt += 1
        if check:
            break
        past = now
        if i == N - 2:
            print('Yes')
            exit()
print('No')