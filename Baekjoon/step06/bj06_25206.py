# 2023.12.14
# 백준
# 단계별 문제풀이
# 6단계 심화 1
# 너의 평점은


grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
         'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,
         'F':0.0}

total_sum = 0
cnt_subject = 0
for _ in range(20):
    subject = list(input().split())[1:]
    if subject[1] != 'P': 
        total_sum += float(subject[0])*grade[subject[1]]
        cnt_subject += float(subject[0])
print(total_sum/cnt_subject)
    
    



