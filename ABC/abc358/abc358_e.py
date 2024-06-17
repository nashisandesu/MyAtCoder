import math
I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
K = I()
C = [0] + Li()
# dp[i][j]がaiまでがj個存在する
dp = [[0] * (K + 1) for _ in range(26 + 1)]
dp[0][0] = 1

mod=998244353
# 組み合わせ高速化
n1=[1]*(K+1)
for i in range(2,K+1):
    n1[i]=(n1[i-1]*i)%mod
n2=[1]*(K+1)
for i in range(2,K+1):
    n2[i]=pow(n1[i],mod-2,mod)
def comb(N,R,mod=mod):
    return (n1[N]*(n2[N-R]*n2[R])%mod)%mod

for i in range(1, 26 + 1):
    for j in range(K + 1):
        for k in range(min(C[i], K - j) + 1):
            dp[i][j + k] += dp[i - 1][j] * comb(j + k, k)
            dp[i][j + k] %= mod
ans = 0
for i in range(1, K+1):
    ans += dp[-1][i]
    ans %= mod
print(ans)