# 2023.12.12
# 백준
# 단계별 문제풀이
# 6단계 심화 1
# 단어공부

s = input().upper()

d = {k:s.count(k) for k in set(s)}
answer = []

for k, v in d.items():
    if v == max(d.values()):
        answer.append(k)
    
if len(answer) > 1:
    print('?')
else:
    print(answer[0])


    
    



