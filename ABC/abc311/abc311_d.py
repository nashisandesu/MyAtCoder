import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
data = [input() for _ in range(N)]

visit = [[0] * M for _ in range(N)]
visit[1][1] = 1
pass_ice = set()
pass_ice.add((1,1))
todo = [(1,1)]

dxdy = [[1,0], [-1, 0], [0,1],[0,-1]]

while todo:
    x, y = todo.pop()
    for dx, dy in dxdy:
        cntx, cnty = x, y
        while data[cntx + dx][cnty + dy] == '.':
            cntx += dx
            cnty += dy
            pass_ice.add((cntx, cnty))
        if not visit[cntx][cnty]:
            todo.append((cntx, cnty))
            visit[cntx][cnty] = 1
print(len(pass_ice)) 



# 解法その2
'''
def search_right(point):
    x, y = point
    for i in range(y + 1, M):
        if data[x][i] == '.':
            pass_ice.add((x, i))
        else:
            y = i - 1
            break
    if (x, y) not in visit:
        visit.add((x, y))
        search_ice((x, y))
    
def search_left(point):
    x, y = point
    for i in reversed(range(0, y)):
        if data[x][i] == '.':
            pass_ice.add((x, i))
        else:
            y = i + 1
            break
    if (x, y) not in visit:
        visit.add((x, y))
        search_ice((x, y))
    
def search_down(point):
    x, y = point
    for i in range(x + 1, N):
        if data[i][y] == '.':
            pass_ice.add((i, y))
        else:
            x = i - 1
            break
    if (x, y) not in visit:
        visit.add((x, y))
        search_ice((x, y))
    
def search_top(point):
    x, y = point
    for i in reversed(range(0, x)):
        if data[i][y] == '.':
            pass_ice.add((i, y))
        else:
            x = i + 1
            break
    if (x, y) not in visit:
        visit.add((x, y))
        search_ice((x, y))

def search_ice(point):
    x, y = point

    search_right(point)
    search_left(point)
    search_top(point)
    search_down(point)
    
start = (1, 1)
pass_ice.add(start)
visit.add(start)
search_ice(start)
print(len(pass_ice))
'''