N, K = map(int, input().split())
A = [-1] * N
ans = []
for i in range(K + 1):
    print('?', end = '')
    for j in range(K):
        print(' ' + str((i + j) % (K + 1) + 1), end ='')
    print()
    ans.append(int(input()))
wa = sum(ans)
for index, k in enumerate(ans):
    A[(index - 1) % (K + 1)] = (wa - k) % 2

sum_K_1 = sum(A[:K-1])
for i in range(N - K - 1):
    print('?', end = '')
    for j in range(K - 1):
        print(' ' + str((j) % N + 1), end ='')
    print(' ' + str((K + 1 + i) % N + 1), end ='')
    print()
    A[K + i + 1] = (sum_K_1 - int(input()))  % 2
print('!', end = '')

for a in A:
    print(' ' + str(a), end ='')
print()