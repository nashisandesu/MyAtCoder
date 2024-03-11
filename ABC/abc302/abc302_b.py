import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
snuke = list('snuke')
search = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
for dx, dy in search:
    for i in range(H):
        for j in range(W):
            h, w = i, j
            cnt = 0
            ans = []
            while True:
                if h == H or h == -1 or w == W or w == -1:
                    break
                if S[h][w] == snuke[cnt]:
                    cnt += 1
                    ans.append((h,w))
                    if cnt == 5:
                        for x, y in ans:
                            print(x + 1, y+ 1)
                        exit()
                else:
                    cnt = 0
                    ans = []
                h += dx
                w += dy
