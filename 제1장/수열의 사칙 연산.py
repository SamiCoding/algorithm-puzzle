# 1,000 ~ 9,999 중에서 앞의 조건을 만족하는 수를 구해 보세요.

"""
앞의 조건 )
나열된 각 숫자 사이에 사칙연산의 연산자를 넣어 계산해 보기
완성된 식을 계산한 결과 '원래 수를 거꾸로 나열한 숫자'가 되는 것
"""

import re

op = ["*", ""]
for i in range(1000, 10000):
    c = str(i)
    for j in range(0, len(op)):
        for k in range(0, len(op)):
            for l in range(0, len(op)):
                val = c[3] + op[j] + c[2] + op[k] + c[1] + op[l] + c[0]

                # 0으로 시작하는 숫자가 있는지 확인하고 있는 경우 제거
                val = re.sub(r"0(\d+)", r"\1", val)
                
                # 연산자를 하나는 넣는 경우
                if len(val) > 4:
                    if i == eval(val):
                        print(val, "=", i)
