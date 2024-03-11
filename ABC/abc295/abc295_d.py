import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

S = input()
cnt = [0] * 1024
cnt[0] = 1
temp = 0
for s in S:
    temp ^= 1 << int(s)
    cnt[temp] += 1 #同じ数列になるものを調べていく。同じ数列になるものはその間で必ず嬉しい数ができる

ans = 0
for c in cnt:
    ans += c * (c - 1) // 2 #cC2を計算する
print(ans)