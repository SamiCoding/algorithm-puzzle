# 하나의 숫자를 가능하면 적게 사용하여 '1234'를 표현할 때 가장 적은 개수로 표현할 수 있는 숫자를 구하고 그 식을 모두 구해 보세요.

found = False

# 정수 나눗셈을 할 수 있게
# 나눗셈을 //로 지정함
op = ['+', '-', '*', '//', '']

def check(n, expr, num):
    global found
    if n == 0:
        if eval(expr) == 1234:
            print(expr)
            found = True
    else:
        for i in op:
            check(n-1, "{}{}{}".format(expr, i, num), num)

length = 1
while not found:
    for num in range(1, 9+1):
        check(length, num, num)
    length += 1