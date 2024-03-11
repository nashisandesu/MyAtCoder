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
Ls = lambda: list(map(str, input().split()))

########################################################
def gcd(x,y):
    r = x % y 
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

def lcm(x, y):
	return (x * y)//gcd(x, y)

N, a, b, c = Mi()
ab = lcm(a,b)
ca = lcm(a,c)
bc = lcm(b, c)
abc = lcm(ab, c)
abc_list = [a, b, c, ab, bc, ca, abc]
abc_list.sort()
A=deque(sorted(Li()))
inf = 3* 10**18
min_abc = [[(0, inf)] * 7 for _ in range(3)]
while A:
    data = A.popleft()
    for i in range(7):
        if data % abc_list[i] == 0:
            result = 0
        else:
            result = abc_list[i] - data % abc_list[i]
        if min_abc[0][i][1] > result:
            min_abc[2][i] = (min_abc[1][i][0], min_abc[1][i][1])
            min_abc[1][i] = (min_abc[0][i][0], min_abc[0][i][1])
            min_abc[0][i] = (data, result)
        elif min_abc[1][i][1] > result:
            min_abc[2][i] = (min_abc[1][i][0], min_abc[1][i][1])
            min_abc[1][i] = (data, result)
        elif min_abc[2][i][1] > result:
            min_abc[2][i] = (data, result)
used =[]
a_b_c = []
a_b_c_r = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            p, q, r = min_abc[i][0][0],min_abc[j][1][0],min_abc[k][2][0]
            p1, q1, r1 = min_abc[i][0][1],min_abc[j][1][1],min_abc[k][2][1]
            if p!=q and q!=r and r!=p:
                a_b_c.append(p1+q1+r1)
                a_b_c_r.append((p,q,r))
for i in range(3):
    for j in range(3):
            p, q = min_abc[i][2][0],min_abc[j][3][0]
            p1, q1 = min_abc[i][2][1],min_abc[j][3][1]
            if p!=q:
                a_b_c.append(p1+q1)
                a_b_c_r.append((p,q))
for i in range(3):
    for j in range(3):
            p, q = min_abc[i][0][0],min_abc[j][4][0]
            p1, q1 = min_abc[i][0][1],min_abc[j][4][1]
            if p!=q:
                a_b_c.append(p1+q1)
                a_b_c_r.append((p,q))   
for i in range(3):
    for j in range(3):
            p, q = min_abc[i][1][0],min_abc[j][5][0]
            p1, q1 = min_abc[i][1][1],min_abc[j][5][1]
            if p!=q:
                a_b_c.append(p1+q1)
                a_b_c_r.append((p,q))
a_b_c.append(min_abc[0][6][1])
print(min(a_b_c))
    # if zero_abc[i]:
    #     used.append(zero_abc[i])
    # else:
    #     value, cnt = min_abc[i]
    #     if value
        
