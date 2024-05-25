# 반복에 포함되지 않는 수의 개수를 구해보세요.

# 다음 눈을 취득한다
def next_dice(dice):
    top = dice//6**5
    left, right = divmod(dice, 6**(5-top))
    return (right+1)*(6**(top+1)) - (left+1)

count = 0
for i in range(0, 6**6):
    check = []
    # 반복할 때까지 다음 주사위를 찾는다
    while i not in check:
        check.append(i)
        i = next_dice(i)
    # 반복한 위치를 확인하고 반복 대상이 아니라면 카운트
    if check.index(i) != 0:
        count += 1
print(count)