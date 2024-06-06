# n = 4일 때 앞과 같이 카운트한 값으로 배치를 생각해보고 한 가지 방식으로만 배치할 수 있는 패턴이 몇 가지인지를 구해 보세요.

N = 4

def search(rows):
    # 모든 행을 탐색하면 종료
    if len(rows) == N:
        return 1
    
    count = 0
    for row in range(0, 2**N):
        # 네 모서리에 O와 X가 교대로 되어 있는지 확인
        cross = filter(lambda r: (row & ~r) > 0 and (~row & r) > 0, rows)
        cross = list(cross)
        if len(cross) == 0:
            count += search(rows + [row])
    return count

print(search([]))