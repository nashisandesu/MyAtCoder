T = int(input())
for i in range(T):
  N = int(input())
  ok = 1
  cnt = 0
  for j in range(2, int(N** 0.5) + 1):
    if N % j == 0:
      cnt = 1
      N //= j
      while N != 1:
        if N % j != 0:
          break
        else:
          N //= j
      else:
        ok = 0
      break
  if ok and cnt:
    print('Yes')
  else:
    print('No')