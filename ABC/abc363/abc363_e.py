import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
H, W, Y = Mi()
A = [Li() for _ in range(H)]
sea = []
visited = [[False] * W for _ in range(H)]
rest = H * W
for h in range(H):
    for w in range(W):
        if h == 0 or h == H - 1 or w == 0 or w == W - 1:
            heapq.heappush(sea, (A[h][w], h * W + w))
            visited[h][w] = True

for i in range(1, Y + 1):
    while sea and sea[0][0] <= i:
        _, v = heapq.heappop(sea)
        h, w = divmod(v, W)
        rest -= 1
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and visited[nh][nw] == False:
                heapq.heappush(sea, (A[nh][nw], nh * W + nw))
                visited[nh][nw] = True
    
    print(rest)