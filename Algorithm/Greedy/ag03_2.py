# 이것이 코딩테스트이다
# 2023.10.19
# 숫자 카드 게임
# 2중 반복문 구조를 이용

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)