from itertools import permutations
M = int(input())
S1 = input()
S2 = input()
S3 = input()
S_list = [S1*3, S2*3, S3*3]
ans = 3*M

def solve(p, num):
    time = -1
    for i in range(3):
        time = S_list[p[i]].find(str(num), time + 1)
        if time == -1:
           return 3 * M
    return time

for num in range(10):
    for p in permutations(range(3)):
       result = solve(p,num)
       if ans > result:
           ans = result
print(ans if ans != 3 * M else -1)      