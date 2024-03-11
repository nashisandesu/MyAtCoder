import sys
sys.setrecursionlimit(100000)
K = int(input())
todo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if K <= 9:
    print(K)
else:
    cnt = 9
    while todo:
        now = todo.pop(0)
        for i in range(now % 10):
            cnt += 1
            if cnt == K:
                print(now * 10 + i)
                exit()
            if i != 0:
                todo.append(now * 10 + i)


