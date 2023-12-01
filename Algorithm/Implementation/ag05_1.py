# 이것이 코딩테스트이다
# 2023.12.01
# 구현, 시뮬레이션
# 상하좌우

# 입력
n = int(input())    # n*n 지도 행렬 크기
plans = input().split() # 이동 명령 L, R, U, D

# 왼쪽, 오른쪽, 위쪽, 아래쪽 이동
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 출발 위치
x, y = 1, 1

for plan in plans: # 이동 명령 순차적으로 
    for i in range(len(move_types)):    # 이동 타입 확인
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    # N*N 범위에 벗어나면 이동 결과 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue   
    else:
        x, y = nx, ny

print(x, y)
            

    