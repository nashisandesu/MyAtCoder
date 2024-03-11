import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

X, Y, Z = map(int, input().split())
S = input()

dp = [[0,0] for  _ in range(len(S) + 1)]
dp[0][0] = 0
dp[0][1] = 10 ** 10^9
for i in range(1, len(S) + 1):
    if S[i-1] == 'a':
        dp[i][0] = min(dp[i - 1][0] + X, dp[i - 1][1] + Z + X, dp[i - 1][1] + Y + Z)
        dp[i][1] = min(dp[i - 1][0] + Z + Y, dp[i - 1][0] + X + Z, dp[i - 1][1] + Y)
    else:
        dp[i][0] = min(dp[i - 1][0] + Y, dp[i - 1][1] + Z + Y, dp[i - 1][1] + X + Z)
        dp[i][1] = min(dp[i - 1][0] + Z + X, dp[i - 1][0] + Y + Z, dp[i - 1][1] + X)
print(min(dp[-1]))