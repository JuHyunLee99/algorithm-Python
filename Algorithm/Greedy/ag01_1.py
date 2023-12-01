# 이것이 코딩테스트이다
# 2023.10.19
# 큰 수의 법칙
# 내 풀이

# n: 자연수 갯수 / m: 연산 횟수 / k: 같은 인덱스 연속 반복 가능 횟수
n, m, k = map(int, input().split()) 
data = list(map(int,input().split()))

data.sort() # 리스트 정렬
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두 번째로 큰수

count = 0
temp = first
result = 0

for i in range(m):
    if count == k:
        result += second 
        count = 0
    else:
        result += first
        count += 1

print(result)