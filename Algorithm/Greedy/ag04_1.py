# 이것이 코딩테스트이다
# 2023.12.01
# 1이 될때 까지
# 1. 단순하게 푸는 방법
    
import time

n, k = map(int, input().split())

result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1

    n /= k
    result += 1

while n > 1:
    n-=1
    result += 1
    
print(result)
