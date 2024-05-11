# 아이들이 16명이라면 만들 수 있는 짝이 몇 가지 있는지 구해 보세요.

n = 16
pair = [None]*(n//2+1)
pair[0] = 1

for i in range(1, n//2+1):
    pair[i] = 0
    for j in range(0, i):
        pair[i] += pair[j]*pair[i-j-1]

print(pair[n//2])