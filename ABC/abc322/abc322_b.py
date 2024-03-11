N, M = map(int, input().split())
S = input()
T = input()
if S.startswith(T[:N]) and S.endswith(T[M-N:]):
    print(0)
elif S.startswith(T[:N]):
    print(1)
elif S.endswith(T[M-N:]):
    print(2)
else:
    print(3)
