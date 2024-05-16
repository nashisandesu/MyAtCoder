import heapq

I = lambda: int(input())

N = I()
c = [list(input()) for _ in range(N)]

dp = [[float('Inf')] * N for _ in range(N)]
todo = []
if c[0][0] == 'R':
    heapq.heappush(todo, (0, (0,0)))
else:
    heapq.heappush(todo, (1, (0,0)))

xy = [(1,0), (0, 1), (-1, 0), (0, -1)]
while todo:
    cost, (x, y) = heapq.heappop(todo)
    x = -x
    y = -y
    if dp[x][y] != float('Inf'):
        continue
    else:
        dp[x][y] = cost
        if x == N -1 and y ==N-1:
            break
    for dx, dy in xy:
        nowx, nowy = x+dx, y+dy
        if 0 <= nowx < N and 0 <= nowy < N and dp[nowx][nowy] == float('Inf'):
            if c[nowx][nowy] == 'R':
                heapq.heappush(todo, (cost, (-nowx, -nowy)))
            else:
                heapq.heappush(todo, (cost + 1, (-nowx, -nowy)))

ans = dp[-1][-1]
dp = [[float('Inf')] * N for _ in range(N)]
todo = []
if c[0][N-1] == 'B':
    heapq.heappush(todo, (0, (N-1,0)))
else:
    heapq.heappush(todo, (1, (N-1,0)))

xy = [(1,0), (0, -1), (-1, 0), (0, 1)]
while todo:
    cost, (y, x) = heapq.heappop(todo)
    if dp[x][y] != float('Inf'):
        continue
    else:
        dp[x][y] = cost
        if x == N -1 and y ==0:
            break
    for dx, dy in xy:
        nowx, nowy = x+dx, y+dy
        if 0 <= nowx < N and 0 <= nowy < N and dp[nowx][nowy] == float('Inf'):
            if c[nowx][nowy] == 'B':
                heapq.heappush(todo, (cost, (nowy, nowx)))
            else:
                heapq.heappush(todo, (cost + 1, (nowy, nowx)))

ans += dp[-1][0]
print(ans)