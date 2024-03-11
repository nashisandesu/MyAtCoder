n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, x, y))
    g[b].append((a, -x, -y))

q = [0]
ans = [(None, None)] * n
ans[0] = (0, 0)
while q:
    v = q.pop()
    a, b =  ans[v]
    for c, x, y in g[v]:
        if ans[c] == (None, None):
            ans[c] = (a + x, b + y)
            q.append(c)
else:
    for i in range(n):
        if ans[i] == (None, None):
            print('undecidable')
        else:
            print(ans[i][0], ans[i][1])

