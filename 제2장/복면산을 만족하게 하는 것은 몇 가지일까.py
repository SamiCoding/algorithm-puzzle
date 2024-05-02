# 다음의 식을 만족하는 숫자 대입 방법은 몇 가지 있는지 구해 보세요.

"""
READ + WRITE + TALK = SKILL
"""

from itertools import permutations

count = 0
for (r, e, a, d, w, i, t, l, k, s) in permutations(range(0, 10)):
    if r == 0 or w == 0 or t == 0 or s == 0:
        continue
    read = r*1000 + e*100 + a*10 + d
    write = w*10000 + r*1000 + i*100 + t*10 + e
    talk = t*1000 + a*100 + l*10 + k
    skill = s*10000 + k*1000 + i*100 + l*10 + l
    if read + write + talk == skill:
        count += 1
        print("{} + {} + {} = {}".format(read, write, talk, skill))

print(count)