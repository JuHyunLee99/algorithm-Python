# 이것이 코딩테스트이다
# 2023.10.19
# 큰 수의 법칙
# 책 풀이

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 반복되는 수열을 파악하여 수학적으로 계산함.
# 가장 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second    # 두번째로 큰 수 더하기

print(result)