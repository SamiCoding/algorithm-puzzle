#  1 ~ 7의 7개의 숫자로 만들 수 있는 모든 순열에 대해 작은 쪽부터 순서대로 나열하기 위한 최소 교환 횟수의 합계를 구해 보세요.

def count_swap(n):
    if n == 1:
        return 0
    multi = 1
    for i in range(1, n):
        multi *= i
    return (n-1)*multi + n*count_swap(n-1)

print(count_swap(7))