import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

A, B = map(int, input().split())
if A > B:
    big = A
    small = B
else:
    big = B
    small = A
cnt = 0
while True:
    temp_cnt = big // small
    if big % small == 0:
        cnt += temp_cnt - 1
        break
    cnt += temp_cnt

    temp = small
    small = big - small * temp_cnt
    big = temp

print(cnt)

