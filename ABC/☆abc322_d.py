import sys,bisect
sys.setrecursionlimit(100000)
from collections import deque

def sort_poly(now_poly: list[int]):
    left_min = 4
    down_min = 4
    for p in now_poly:
        left_min = min(left_min, p % 4)
        down_min = min(down_min, p //4)
    for j in range(len(now_poly)):
        now_poly[j] -= left_min + 4 * down_min
    now_poly.sort()

def rotate(now_poly: list[int])->list[int]:
    make_poly = []
    for p in now_poly:
        row, column = p // 4, p % 4
        new_row, new_column = column, 3 - row
        make_poly.append(new_row * 4 + new_column)
    sort_poly(make_poly)
    return make_poly

def check(start: int, next_poly: list[int], target: set):
    plus = start - next_poly[0]
    new_p = []
    for p in next_poly:
        row, column = p // 4, p % 4
        p += plus
        if p // 4 != row + start // 4 or p not in target:
            return False
        new_p.append(p)
    return new_p

if __name__ == '__main__':
    P = [[list(input()) for _ in range(4)] for _ in range(3)]
    poly = [[] for _ in range(3)]
    cnt = 0
    for i in range(3):
        poly[i].append([])
        for j in range(4):
            for k in range(4):
                if P[i][j][k] == '#':
                    cnt += 1
                    poly[i][0].append(j * 4 + k)
    if cnt != 16:
        print('No')
        exit()
    sort_poly(poly[0][0])
    sort_poly(poly[1][0])
    sort_poly(poly[2][0])
    for i in range(3):
        for j in range(3):
            poly[j].append(rotate(poly[j][i]))

    for k in range(4):
        target = set(range(16)) ^ set(poly[0][k])
        for i in range(4):
            ans = check(min(target), poly[1][i], target)
            if ans:
                next_target = target ^ set(ans)
                for j in range(4):
                    if check(min(next_target), poly[2][j], next_target):
                        print('Yes')
                        exit() 
        for i in range(4):
            ans = check(min(target), poly[2][i], target)
            if ans:
                next_target = target ^ set(ans)
                for j in range(4):
                    if check(min(next_target), poly[1][j], next_target):
                        print('Yes')
                        exit() 

    print('No')                   
