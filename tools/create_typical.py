import os

# ファイル名のリストを作成
file_names = []
for i in range(90):
    first, second = divmod(i,26)
    if first == 0:
        file_names.append(f"typical90_{chr(97+second)}.py")
    else:
        file_names.append(f"typical90_{chr(97+first)}{chr(97+second)}.py")

print('どこまで？')
alphabet = input()
num = ord(alphabet) - ord('a') + 1

# 書き込む内容
content = """import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
"""

folder_path =  f"/Users/yuri/Atcoder/typ/typical90"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 各ファイルに対して、ファイルを作成し、指定した内容を書き込む
for file_name in file_names[:num]:
    file_path = f"{folder_path}/{file_name}"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(content)
        print(file_name + ' is created!')
    else:
        print(file_name + ' exists!')