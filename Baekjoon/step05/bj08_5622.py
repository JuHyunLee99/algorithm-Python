# 2023.12.11
# 백준
# 단계별 문제풀이
# 5단계: 문자열
# 다이얼

array = []
c = ord('A')
for i in range(8):
    if i == 7 or i == 5:
        array.append((chr(c), chr(c+1), chr(c+2), chr(c+3)))    
        c += 4
    else:
        array.append((chr(c), chr(c+1), chr(c+2)))
        c += 3

s = input()
time = 0
for i in s:
    for j in range(len(array)):
        if i in array[j]:
            time += j+3

print(time)