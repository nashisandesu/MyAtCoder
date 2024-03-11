import os

# 基本となるファイル名（数字）を設定
print('ABCのナンバーは？')
base_name = input()

# ファイル名のリストを作成
file_names = [f"abc{base_name}_a.py", f"abc{base_name}_b.py", f"abc{base_name}_c.py", 
              f"abc{base_name}_d.py", f"abc{base_name}_e.py", f"abc{base_name}_f.py",
              f"abc{base_name}_g.py", f"abc{base_name}_h.py"]
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

folder_path =  f"/Users/yuri/research2023/Atcoder/ABC/abc{base_name}"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 各ファイルに対して、ファイルを作成し、指定した内容を書き込む
for file_name in file_names[:num]:
    file_path = f"/Users/yuri/research2023/Atcoder/ABC/abc{base_name}/{file_name}"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(content)
        print(file_name + ' is created!')
    else:
        print(file_name + ' exists!')
# 