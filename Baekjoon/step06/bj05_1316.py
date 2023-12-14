# 2023.12.14
# 백준
# 단계별 문제풀이
# 6단계 심화 1
# 그룹 단어 체커

n = int(input())
cnt = n
for _ in range(n):
    s = input()
    array = []
    while s:
        if s[0] not in array:
            array.append(s[0])
            s = s.lstrip(s[0])
        else:
            cnt -= 1
            break
print(cnt)

    



    

    
    



