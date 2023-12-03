# 삼성 SW 역량테스트 기출문제
# 바이러스 검사 
# 브론즈2

# 입력
n = int(input())    # 식당 수
customers = list(map(int, input().split()))    # 각 식당에 손님 수
leader, follower = map(int, input().split())    # 팀장, 팀장 검사  최대 가능 수

# 출력: 검사를 위해 필요한 검사자의 최소의 수
total = n   # 팀장은 식당 당 오직 1명

for customer in customers:  # 순서대로 각 식당에 방문하며 손님 검사

    customer -= leader  # 팀장 검사 수 빼기
    if customer <= 0:   # 팀장 검사 후 남은 손님 없으면 
        continue        # 다음 식당으로..
    
    total += customer // follower   # 최대 검사 가능 수에 대한 팀원 수
    customer = customer % follower  # 아직 검사 안한 남은 손님들
    if customer:                    # 남은 손님이 있다면
        total += 1                  # 팀원 한명 더 추가

print(total)