# 이것이 코딩테스트이다
# 2023.12.01
# 게임 개발
# 내가 푼 풀이법

# 입력
# N*M 직사각형의 게임 판
n, m = map(int, input().split())
# 현재 위치, 방향 
x, y, d = map(int, input().split())
# 0:북 1:동 2:남 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 맵 정보 (육지 0, 바다 1)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방문한 위치 저장 맵
result_map = [[0] * m for _ in range(n)] 
result_map[x][y] = 1    # 위치 방문 처리
count = 1


# 반시계방향으로 탐색(회전)
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


turn_time = 0   # 회전 횟수
while True:
    turn_left() # 먼저 회전 
    turn_time += 1 # 회전 횟수 기록

    nx = x + dx[d]  # 일단 전진
    ny = y + dy[d]
    
    # 바다이거나, 방문했던 곳이거나, 게임맵 벗어났을 때 전진 취소.
    if array[nx][ny] == 1 or result_map[nx][ny] == 1 \
        or nx < 1 or ny < 1 or nx > n or ny >m:
        if turn_time == 4:  # 이미 4번 회전 했으면
            nx = x - dx[d]  # 일단 뒤로 가기
            ny = y - dy[d]  
            # 뒤로 갔는데 바다이거나, 게임맵 벗어났을 때 뒤로 가기 취소.
            if array[nx][ny] == 1 or nx < 1 or ny < 1 or nx > n or ny >m:
                break   # 게임 끝
            else:   # 뒤로 갈 수 있다면
                x, y = nx, ny   # 현재 위치 변경
                turn_time = 0   # 회전횟수 초기화
        else:   # 아직 4번 회전 안했으면 다시 회전하러 가자~
            continue
    else:   # 방문 안한 곳이라면
        x, y = nx, ny   # 현재 위치 변경
        result_map[x][y] = 1    # 방문 기록
        count += 1              # 방문 칸 횟수 증가
        turn_time = 0           # 회전 수 초기화

print(count)





