S = input()
def check(input):
    if input == input[::-1]:
        return True
    else:
        return False
max_len = 0
for i in range(len(S)):
    for j in range(len(S) - i, 0, -1):
        word = S[i: i + j]
        if max_len >= j:
            break
        if check(word):
            max_len= j

print(max_len)