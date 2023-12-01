# 이것이 코딩테스트이다
# 2023.12.01
# 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59뷴 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

# 입력
n = int(input())

count = 0

for i in range(n+1):  # 시
    for j in range(60): # 분
        for k in range(60): # 초
            # 매 시간 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)
    
