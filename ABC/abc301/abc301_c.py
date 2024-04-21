import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
S = list(input())
T = list(input())
dic_S = {}
dic_T = {}
at_list = {"a","t","c","o","d","e","r"}
for i in S:
    if i in dic_S:
        dic_S[i] += 1
    else:
        dic_S.update({i:1})
for i in T:
    if i in dic_T:
        dic_T[i] += 1
    else:
        dic_T.update({i:1})

S_safe = 0
T_safe = 0

if "@" in dic_S:
    S_safe = dic_S["@"]
    S_safe2 = dic_S["@"]
    del dic_S["@"]
if "@" in dic_T:
    T_safe = dic_T["@"]
    T_safe2 = dic_T["@"]
    del dic_T["@"]

for item in dic_S.items():
    if item[0] not in dic_T:
        if item[0] in at_list:
            T_safe -= item[1]
            dic_S[item[0]] = 0
            if T_safe < 0:
                print("No")
                exit()
        else:
            print("No")
            exit()
    elif item[1] == dic_T[item[0]]:
        dic_S[item[0]] = 0
        dic_T[item[0]] = 0
    elif item[1] > dic_T[item[0]]:
        dic_S[item[0]] = 0
        dic_T[item[0]] = 0
        if item[0] in at_list:
            T_safe -= item[1]
            if T_safe < 0:
                print("No")
                exit()
        else:
            print("No")
            exit()
    elif item[1] < dic_T[item[0]]:
        dic_S[item[0]] = 0
        dic_T[item[0]] = 0
        if item[0] in at_list:
            S_safe -= item[1]
            if S_safe < 0:
                print("No")
                exit()
        else:
            print("No")
            exit()
for item in dic_T.items():
    if item[1] != 0:
        if item[0] in at_list:
            S_safe -= item[1]
            if S_safe < 0:
                print("No")
                exit()
        else:
            print("No")
            exit()    
print("Yes")    
