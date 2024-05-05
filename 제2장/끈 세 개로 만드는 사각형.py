# 끈의 길이를 1부터 500까지 변화시킨다고 할 때 두 개의 직사각형의 면적의 합과 정사각형의 면적이 같아지는 조합이 몇 가지 있는지 구해 보세요.

from itertools import combinations

MAX = 500

answer = []
for c in range(1, MAX//4+1): # 정사각형의 한 변
    edge = map(lambda x: x*(2*c-x), range(1, c))
    for a, b in combinations(edge, 2):
        if a + b == c*c:
            answer.append([1, b/a, c*c/a])

# 중복 제거
print(len(set(frozenset(i) for i in answer))) # 정수배 제외