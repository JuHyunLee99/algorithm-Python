# 이것이 코딩테스트이다
# 2023.12.01
# 왕실의 나이트 (8*8 좌표 평면)
# 현재의 위치에서 이동할 수 있는 경우의 수

#입력
input_data = input()    # 현재 위치 'a1'
x = int(input_data[1])  # 1
y = int(ord(input_data[0])) - int(ord('a')) + 1 # 'a'를 숫자로 변환 -> 1

# 출력
count = 0

# 말 이동 가능 수: 8가지
dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, -2, -2, -1, 1, 2, 2]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny >8:
        continue
    else:
        count += 1

print(count)

