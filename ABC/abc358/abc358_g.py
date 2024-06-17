I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
H, W, K = Mi()
Si, Sj = Mi()
Si -= 1
Sj -= 1
A = [Li() for _ in range(H)]
dp = [[[-float('Inf')] * W for _ in range(H)] for _ in range(min(K, 2501)+1)]
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
dp[0][Si][Sj] = 0
ans = -float('inf')
for i in range(1, min(K+1, 2501)):
    for h in range(H):
        for w in range(W):
            if dp[i-1][h][w] == -float('Inf'):
                continue
            for dx, dy in dxdy:
                ni, nj = h + dx, w + dy
                if 0 <= ni < H and 0 <= nj < W:
                    dp[i][ni][nj] = max(dp[i][ni][nj], dp[i-1][h][w] + A[ni][nj]) 

            ans = max(ans, dp[i][h][w] + A[h][w] * (K-i))  
print(ans)