# 끈이 교차하는 지점의 수가 가장 많을 때 그 수를 구해 보세요. 예를 들면 왼쪽 끝의 그림에서는 5개, 중간 그림에서는 9개입니다.

"""
그림 )

구멍\/구멍      구멍\\구멍      구멍ㅡ|구멍
구멍/\구멍      구멍\\구멍      구멍ㅡ|구멍
구멍\/구멍      구멍\\구멍      구멍|ㅡ구멍
구멍/\구멍      구멍\\구멍      구멍|ㅡ구멍
구멍\/구멍      구멍\\구멍      구멍ㅡ|구멍
구멍/\구멍      구멍∠구멍      구멍|ㅡ구멍
"""

from itertools import permutations

N = 6

max_cnt = 0
temp = list(range(1, N))

for l in permutations(temp, N-1): # 왼쪽의 순서
    for r in permutations(temp, N-1): # 오른쪽의 순서
        # 경로를 설정
        path = []
        left = 0
        right = r[0]
        for i in range(0, N-1):
            path.append([left, right])
            left = l[i]
            path.append([left, right])
            if len(r) > i+1:
                right = r[i+1]
        path.append([left, 0])

    # 경로가 교차하는지를 판정
    cnt = 0
    for i in range(0, N*2-1):
        for j in range(i+1, N*2-1):
            if (path[i][0]-path[j][0])*(path[i][1]-path[j][1]) < 0:
                cnt += 1
    
    max_cnt = max([max_cnt, cnt])

print(max_cnt)