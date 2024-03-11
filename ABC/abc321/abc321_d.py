import sys,bisect
sys.setrecursionlimit(100000)
from collections import deque
N, M, P = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()
cnt = 0

def search_bound(price):
    left = 0
    right = M
    while left < right:
        center = (left + right) // 2
        if B[center] >= price:
            right = center
        else:
            left = center + 1
    return left

S = [0] * (M + 1)
S[0] = 0
for i in range(M):
    S[i+1] = S[i] + B[i]
# print(S)
for priceA in A:
    bound = search_bound(P- priceA)
    cnt += S[bound] + priceA * bound
    cnt += P * (M - bound)

print(cnt)