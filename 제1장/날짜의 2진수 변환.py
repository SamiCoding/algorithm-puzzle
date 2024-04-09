# 연월일을 YYYYMMDD의 8자리 정수로 나타내었을 때 2진수로 변환하여 거꾸로 나열한 다음 다시 10진수로 되돌렸을 때 원래 날짜와 같은 날짜가 되는 것을 찾아보세요.

"""
기간은 지난 도쿄 올림픽(1964년 10월 10일)부터 다음 도쿄 올림픽(2020년 7월 24일 예정)으로 하겠습니다.
"""

# 날짜를 다루는 datetime 클래스 불러오기
from datetime import datetime, timedelta

# 기간 설정
start = datetime.strptime("1964-10-10", "%Y-%m-%d")
end = datetime.strptime("2020-07-24", "%Y-%m-%d")
step = timedelta(days=1)

# 해당하는 날짜 찾아 출력하기
while start <= end:
    day = bin(int(start.strftime("%Y%m%d"))).replace("0b", "")
    if day == day[::-1]:
        print(start.strftime("%Y-%m-%d"))
    start += step