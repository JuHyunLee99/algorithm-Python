# 이것이 코딩테스트이다
# 2023.12.03
# 효율적인 화폐 구성

# 입력
n, m = map(int, input().split())    # 화폐 종류의 개수 , 목표 금액
money_types = []        # 화폐 종류
for _ in range(n):  
    money_types.append(int(input()))


# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

d[0] = 0
# 첫번째 화폐단위부터 만들수 있는 금액 확인
for money in money_types:  # 화폐단위 
    for j in range(money, m+1):  # 화폐단위~금액 범위 확인
        if d[j-money] != 10001:
            d[j] = min(d[j], d[j-money] + 1)
        
# 출력
# 최소한의 화폐 구성
if d[m] == 10001:
    print(-1)
else:
    print(d[m])