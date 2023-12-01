# 이것이 코딩테스트이다
# 2023.12.01
# 1이 될때 까지
# 2. N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식 
import time

n, k = map(int, input().split())

result = 0

while True:
    # N이 K 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # (N이 K로 나누어 떨어지는 수)가 될 때 까지 1씩 빼기
    target = (n // k) *k
    result += n - target
    n = target

    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
result += n - 1

print(result)
