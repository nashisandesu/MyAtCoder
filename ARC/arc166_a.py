import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(int, input().split()))

########################################################
T = I()
for _ in range(T):
    N, X, Y = Ms()
    X = deque(X)
    Y = deque(Y)
    x = X.popleft()
    y = Y.popleft()
    try1 = 0
    if x == y:
        bx, by = x, y
    elif y == 'C' or x == 'B':
        print("No")
        continue 
    elif x == 'C':
        bx, by = x, y
    elif x == 'A' and y == 'B':
        try1 = 1
        bx, by = x, y
    else:
        print('case漏れ')
    for i in range(1, int(N)):
        x = X.popleft()
        y = Y.popleft()
        if try1:
            if y =='A' and (x == 'B' or x=='C'):
                bx, by = y, y
                try1 = 0         
                continue       
            elif y == 'C':
                print('No')
                break
            elif x=='B' and y=='B':
                continue
            # elif 
            else:

                continue
            
        if x == y:
            bx, by = x, y
        elif y == 'C':
            print("No")
            break
        elif x == 'C':
            bx, by = x, y
        elif x == 'A' and y == 'B':
            try1 = 1
            bx, by = x, y
        elif x == 'B' and y == 'A':
            if bx == 'C' and by == 'B':
                bx, by = y, y
            else:
                print("No")
                break
        else:
            print('case漏れ')
    else:
        if try1:
            print('No')
        else:
            print('Yes')
