#全探索 15*13*11*9*7*5*3*1=202725
'''
やりたい
'''
#bitDP(動的計画法)
N = int(input())
D = [[0] * N for _ in range(N)]
for i in range(N-1):
    d = list(map(int, input().split()))
    for j in range(i+1 , N):
        D[i][j] = d[j-i-1]
        D[j][i] = d[j-i-1]
b = 1 << N
dp = [0] * b
'''
2^N通りをビットで全て表すと表すと、i番目が1のところは頂点iを使用という扱い
小さい数から全部調べていって最適化していく
動的計画法は最適性の原理に従う
'''
for bit in range(b):
    for i in range(N):
        if not (bit >> i & 1): #i番目が0の時(未使用のとき)にTrue
            for j in range(N):
                if not(bit >> j & 1): #j番目が0の時にTrue
                    new_bit = (1 << i) | (1 << j) | bit
                    dp[new_bit] = max(dp[new_bit], dp[bit] + D[i][j])

print(max(dp))
