import sys,bisect
sys.setrecursionlimit(100000)
from collections import deque
N, K, P = map(int, input().split())
inf = 10 ** 24
DP =[inf for _ in range((P + 1) ** K)]
DP[0] = 0
for n in range(N):
    C, *A = list(map(int, input().split()))
    for value in reversed(range((P + 1) ** K)):
        cond = []
        temp = value
        for _ in range(K):
            cond.append(temp % (P + 1))
            temp //= (P + 1)
        status = 0
        # print(cond)
        for i in range(K):
            if A[i] + cond[i] > P:
                a = P - cond[i]
            else:
                a = A[i]
            status += (a + cond[i]) * ((P+ 1) ** i)
        # print(status)
        if DP[status] > DP[value] + C:
            DP[status] = DP[value] + C
if DP[-1] == inf:
    print(-1)
else:
    print(DP[-1])