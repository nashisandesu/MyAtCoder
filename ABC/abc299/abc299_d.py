import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

N = int(input())
start = 1
end = N
while end - start != 1:
    center = (start + end) //2
    print('? ' + str(center))
    s = int(input())
    if s == 0:
        start = center 
    elif s == 1:
        end = center
print('! ' + str(start))
