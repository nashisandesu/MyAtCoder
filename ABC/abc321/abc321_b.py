N, X = map(int, input().split())
A = list(map(int, input().split()))
min_A = min(A)
max_A = max(A)
now_sum = sum(A) - min_A - max_A
if now_sum >= X:
    print('0')
elif now_sum + min_A >= X:
    print('0')
elif X - now_sum <= max_A:
    print(X - now_sum)
else:
    print('-1')
