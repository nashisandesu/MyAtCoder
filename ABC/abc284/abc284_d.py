import sys, bisect
sys.setrecursionlimit(10**8)
from collections import deque

T = int(input())

for i in range(T):
    N = int(input())
    for i in range(2, int(N **(1/3)) + 1):
        if N % i == 0:
            if (N // i) % i == 0:
                print(i, N//(i*i))
                break
            else:
                print(int((N//i)**0.5), i)
                break
