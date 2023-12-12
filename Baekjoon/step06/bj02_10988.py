# 2023.12.12
# 백준
# 단계별 문제풀이
# 6단계 심화 1
# 팰린드롬인지 확인하기

s = input()
n = len(s)//2
if s[:n] == s[:-n-1:-1]:
    print(1)
else:
    print(0)