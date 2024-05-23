# 한 변의 길이가 6cm의 정사각형이라면 '운명적 만남'이 일어나는 것은 몇 가지인지 구해보세요.

N = 6
cnt = 0
def search(man_x, man_y, woman_x, woman_y, meet):
    global cnt

    if man_x <= N and man_y <= N and woman_x >= 0 and woman_y >= 0:
        if man_x == N and man_y == N and meet >= 2:
            cnt += 1
        if man_x == woman_x:
            meet += 1
        if man_y == woman_y:
            meet += 1
        search(man_x+1, man_y, woman_x-1, woman_y, meet)
        search(man_x+1, man_y, woman_x, woman_y-1, meet)
        search(man_x, man_y+1, woman_x-1, woman_y, meet)
        search(man_x, man_y+1, woman_x, woman_y-1, meet)

search(0, 0, N, N, 0)
print(cnt)