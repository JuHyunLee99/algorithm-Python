# 이것이 코딩테스트이다
# 2023.12.01
# 문자열 재정렬

input_data = input()
result = []
value = 0
for i in input_data:
    if i.isalpha(): # 알파벳이야?
        result.append(i) # 응
    else:   # 숫자야.
        value += int(i) # 그럼 더해

# 알파벳 정렬
result.sort()

# 숫자가 존재하면 리스트에 추가
if value != 0:
    result.append(str(value))

# ''.join 공백없이 문자열 합치기 출력
print(''.join(result))  