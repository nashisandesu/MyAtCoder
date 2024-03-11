N, M = map(int, input().split())
L = list(map(int, input().split()))
left = max(L)
right = sum(L) + N

def satisfy_condition(W):
    rem = W
    cnt = 1 # 行数カウント
    for Li in L:
        if rem >= Li:
            rem -= Li +1
        else:
            cnt += 1
            rem = W - Li - 1
    if cnt > M: # 行数オーバー
        return False
    else:
        return True


while left < right:
    center = (left + right) // 2
    if satisfy_condition(center):
        right = center
    else:
        left = center + 1
    # print(left, right)
print(left)

