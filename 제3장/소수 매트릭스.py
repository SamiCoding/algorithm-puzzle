# n = 3일 때 이러한 패턴이 몇 가지 있는지 구해 보세요. 예를 들어 113, 127, 131, 211, 313, 733의 여섯 가지 요소를 사용하면 앞과 같은 패턴을 만들 수 있습니다.
# 또한, 대각선으로 반전하여 같아지는 경우라 하더라도 각각 다른 것으로 카운트합니다.

# 범위 내의 소수를 추출하는 함수
def prime_range(a, b):
    primes = []
    for i in range(a, b):
        flag = True
        j = 2
        while j*j <= i:
            if i % j == 0:
                flag = False
                break
            j += 1
        if flag:
            primes.append(i)
    return primes

# 3자리의 소수 추출하기
primes = prime_range(100, 1000)

# 맨 앞의 자리를 사용해서 해시 만들기
prime_h = { 0: [] }
for prime in primes:
    try:
        # 있는지 확인
        prime_h[prime // 100]
    except:
        # 없으면
        prime_h[prime // 100] = []
    finally:
        # 최종적으로
        prime_h[prime // 100].append(prime)

cnt = 0
for r1 in primes: # 첫 번째 행
    for c1 in prime_h[r1 // 100]: # 첫 번째 열
        for r2 in prime_h[(c1 % 100) // 10]: # 두 번째 행
            for c2 in prime_h[(r1 % 100) // 10]: # 두 번째 열
                if (r2 % 100) // 10 == (c2 % 100) // 10: # 중앙의 점
                    for r3 in prime_h[c1 % 10]: # 세 번째 행
                        if c2 % 10 == (r3 % 100) // 10:
                            c3 = (r1 % 10) * 100 + (r2 % 10) * 10 + (r3 % 10)
                            if c3 in primes:
                                if len(set([r1, r2, r3, c1, c2, c3])) == 6:
                                    cnt += 1
print(cnt)