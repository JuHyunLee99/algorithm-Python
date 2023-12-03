# 이것이 코딩테스트이다
# 2023.12.03
# 개미 전사 (보텀업)

# 입력
n = int(input())    # 식량창고의 개수
array = list(map(int, input().split())) # 각 창고에 식량의 개수

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * n

# 다이나믹 프로그래밍 보텀업
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

# 출력
# 얻을 수 있는 식량의 최대값
print(d[n-1])