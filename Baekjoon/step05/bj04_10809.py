# 2023.12.11
# 백준
# 단계별 문제풀이
# 5단계: 문자열
# 알파벳 찾기

s = input()

array=[chr(i) for i in range(ord('a'),ord('z')+1)]

for i in array:
    print(s.find(i), end=' ')