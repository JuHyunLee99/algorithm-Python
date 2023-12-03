# 삼성 SW 역량테스트 기출문제
# 외주 수익 최대화하기 
# 실버3
# 책(다이나믹 프로그래밍으로 풀기)

# 입력
n = int(input())    # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


# 3일이 걸리는 1일차에 상담을 진행하는 경우,
# 최대 이익은 '1일 차의 상담 금액 + 4일부터의 최대 상담 금액'
# dp[i] = dp[i] = max(p[i] + dp[t[i] + i], max_value)
# 이를 이용하여 뒤쪽 날짜부터 거꾸로 계산하여 풀이

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    # 상담이 시간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)