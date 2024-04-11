# 남자 20명, 여자 10명이 도착하였을 때 어디에서 끊더라도 두 그룹 모두 남자와 여자의 수가 달라지게 되는 도착 순서가 몇 가지 있는지 구해 보세요.

boy, girl = 20, 10
boy, girl = boy+1, girl+1

ary = [0] * (boy*girl)
ary[0] = 1

for g in range(0, girl):
    for b in range(0, boy):
        if (b != g) and (boy-b != girl-g):
            if b > 0:
                ary[b + boy*g] += ary[b - 1 + boy*g]
            if g > 0:
                ary[b + boy*g] += ary[b + boy*(g-1)]

print(ary[-2] + ary[-boy - 1])