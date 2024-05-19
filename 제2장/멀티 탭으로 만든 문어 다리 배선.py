# n = 20일 때 몇 가지의 멀티 탭 배치를 생각할 수 있는지 구해보세요(단, 전원 용량은 생각하지 않기로 합니다).

N = 20

memo = {1: 1}
def set_tap(remain):
    if remain in memo:
        return memo[remain]    
    cnt = 0
    # 2구
    for i in range(1, remain//2+1):
        if remain-i == i:
            cnt += set_tap(i)*(set_tap(i)+1)//2
        else:
            cnt += set_tap(remain-i)*set_tap(i)
    # 3구
    for i in range(1, remain//3+1):
        for j in range(i, (remain-i)//2+1):
            if (remain-(i+j) == i) and (i == j):
                cnt += set_tap(i)*(set_tap(i)+1)*(set_tap(i)+2)//6
            elif remain-(i+j) == i:
                cnt += set_tap(i)*(set_tap(i)+1)*set_tap(j)//2
            elif i == j:
                cnt += set_tap(remain-(i+j))*set_tap(i)*(set_tap(i)+1)//2
            elif remain-(i+j) == j:
                cnt += set_tap(j)*(set_tap(j)+1)*set_tap(i)//2
            else:
                cnt += set_tap(remain-(i+j))*set_tap(j)*set_tap(i)
    memo[remain] = cnt
    return cnt

print(set_tap(N))