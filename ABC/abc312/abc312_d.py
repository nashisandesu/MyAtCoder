S = input()
n = len(S)
mod = 998244353
dp = [[0 for j in range(i + 1)] for i in range(n + 1)]
dp[0][0]  = 1
#dp[i][j]: i文字目までに(がj個多い組み合わせの数
for i in range(n):
    for j in range(i + 1):
        dp[i][j] %= mod
        if S[i] == '(':
            dp[i + 1][j + 1] += dp[i][j]
        elif S[i] == ')' and j > 0:
            dp[i + 1][j - 1] += dp[i][j]
        elif S[i] == '?':
            dp[i + 1][j + 1] += dp[i][j]
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
print(dp[n][0] % mod)