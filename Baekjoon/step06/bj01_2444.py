# 2023.12.12
# 백준
# 단계별 문제풀이
# 6단계 심화 1
# 별 찍기 -7

n = int(input()) * 2
star = -1
for i in range(n):
    if i >= n//2:
        star -= 2
    else: 
        star += 2
    print(' ' * ((n-1-star)//2) + '*'*star)