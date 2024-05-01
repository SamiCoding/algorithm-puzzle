# 제곱근을 소수로 나타내었을 때 0 ~ 9의 모든 숫자가 가장 빨리 나타나는 최소 정수를 구해 보세요.
# 단 여기서는 양의 제곱근만을 대상으로 합니다.
# 정수 부분을 포함하는 경우와 소수 부분만 취하는 경우 각각에 대해 모두 구해 보세요.

"""
예 )
2의 제곱근: 1.414213562373095048⋯
(0~9가 모두 나타나려면 19자리가 필요)
"""

from math import sqrt

# 정수 부분을 포함하는 경우
i = 1
while True:
    i += 1
    # 소수점을 제거하고 왼쪽 10문자 추출
    string = '{:10.10f}'.format(sqrt(i)).replace('.', '')[0:10]
    # 중복을 제거해서 10문자라면 종료
    if len(set(string)) == 10:
        break
print(i)

# 소수 부분만 계산하는 경우
i = 1
while True:
    i += 1
    # 소수점으로 분할하여 소수 부분만을 취득
    string = '{:10.10f}'.format(sqrt(i)).split('.')[1]
    # 소수 부분의 중복을 제거하고 10문자라면 종료
    if len(set(string)) == 10:
        break
print(i)