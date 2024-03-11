import sys
sys.setrecursionlimit(10**8)
from collections import deque

N = int(input())
S = input()
ans = []
d = 0
for s in S:
    if s == '(':
        ans.append(s)
        d += 1
    elif s == ')':
        if d > 0:
            while True:
                p = ans.pop()
                if p == '(':
                    break
            d -= 1
        else:
            ans.append(s)
    else:
        ans.append(s)
print(''.join(ans))