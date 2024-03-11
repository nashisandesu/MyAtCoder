N = int(input())
inf = 10 ** 18
x = [0] * N
y = [0] * N
z = [0] * N
for i in range(N):
    x[i], y[i], z[i] = map(int, input().split())
sum_z = sum(z)
need_cnt = sum_z // 2 + 1
dp = [inf] * (need_cnt + 1)
dp[0] = 0
for i in range(N):
    get = z[i]
    cost = (y[i] - x[i]) // 2 + 1 if x[i] < y[i] else 0
    for j in reversed(range(need_cnt)): #dp[j+get]を更新にはdp[j]を用いるのでdp[j]を先に更新してはいけない(reversedの理由)
        dp[min(need_cnt, j + get)] = min(dp[min(need_cnt, j + get)], dp[j] + cost)
        
print(dp[-1])