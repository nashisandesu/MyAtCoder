N = int(input())
S = list(input())
Q = int(input())
up = 0
low = 0
updata = set()
for i in range(Q):
    t, x ,c = input().split()
    if t == '1':
        S[int(x) - 1] = c
        updata.add(int(x)-1)
    elif t == '2':
        up, low = 0, 1
        updata.clear()
    else:
        up, low = 1, 0
        updata.clear()
if up == 1:
    for i in range(len(S)):
        if i not in updata:
            S[i] = S[i].upper()
elif low == 1:
    for i in range(len(S)):
        if i not in updata:
            S[i] = S[i].lower()
print(''.join(S))
# print(''.join(S) == 'TEEQUICKBROWMFiXJUGPFOVERTBELAZYDOG')