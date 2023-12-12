# 2023.12.11
# 백준
# 단계별 문제풀이
# 5단계: 문자열
# 상수

a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

print(max(a,b))