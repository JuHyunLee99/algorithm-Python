# 이것이 코딩테스트이다
# 2023.10.19
# 숫자 카드 게임
# min, max 함수 사용하여 풀이

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)   # 한 줄에서 가장 작은 값
    result = max(result, min_value) # 가장 큰 수 찾기

print(result)

