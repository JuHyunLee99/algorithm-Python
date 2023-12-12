# 2023.12.11
# 백준
# 단계별 문제풀이
# 5단계: 문자열
# 문자열 반복

t = int(input())

for _ in range(t):
    n, s = input().split()
    n = int(n)
    for i in s:
        print(i*n, end='')
    print()