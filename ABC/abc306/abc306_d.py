import sys
sys.setrecursionlimit(10**8)
from collections import deque

N = int(input())
deli = 0
dp = [[0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    x, y = map(int, input().split())
    if x == 0:
        dp[i][0] = max([dp[i-1][0] + y, dp[i-1][1] + y, dp[i-1][0]])
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max([dp[i-1][0] + y, dp[i-1][1]])
print(max(dp[-1]))