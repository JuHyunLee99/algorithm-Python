# 삼성 SW 역량테스트 기출문제
# 나무박멸
# 골드4

# 1. 인접한 나무의 개수 만큼 성장
# 2. 인접한 빈칸에 (나무의 개수 // 인접한 빈칸의 개수) 만큼 성장    
#    - 주의 인접겹치는 부분
# 3. 제조제는 뿌린 위치, K까지의 대각선 4방향 영향줌.
# 4. 가장 많은 나무를 죽이는 곳에 제초제 뿌림.
# 5. 제초제가 남아있는 년 수 만큼 제초제가 영향을 미친 곳에는 나무가 못자람.

# 격자 크기 / 반복 년수 / 제초제 확산 범위 / 제초제 유지 년수
n, m, k, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 제초제 기록용
medicine_map = [[0]*n for _ in range(n)]

# [인접] 위 아래 왼쪽 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# [대각선] 왼위 오위 왼아 오아
ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]

# 해당 좌표가 지도 안이 맞는 지 확인
def in_map(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

# 1. x,y에 인접한 나무 개수 만큼 성장, x,y에 인접한 빈칸 인덱스 반환
def growth():
    empty_info = []
    for x in range(n):
        for y in range(n):
            empty_pos = []
            if array[x][y] > 0: # 나무가 존재한다면
                cnt_tree = 0 
                for i in range(4):  # 상하좌우
                    if in_map(x+dx[i], y+dy[i]):    # 인덱스 유효하다면
                        if array[x+dx[i]][y+dy[i]] > 0: # 나무가 존재하다면
                            cnt_tree += 1
                        elif array[x+dx[i]][y+dy[i]] == 0 and medicine_map[x+dx[i]][y+dy[i]] == 0:  # 빈칸이라면
                            empty_pos.append((x+dx[i], y+dy[i]))

                array[x][y] += cnt_tree # 1. 인접한 나무 개수 만큼 성장
                empty_info.append([array[x][y]] + empty_pos)
    return empty_info

# 2. 인접한 빈칸에 (나무의 개수 // 인접한 빈칸의 개수) 만큼 성장
def birth(empty_pos):
    for i in range(len(empty_pos)):
        for x, y in empty_pos[i][1:]:
            array[x][y] += empty_pos[i][0]//len(empty_pos[i][1:])


# x,y에 해초제를 놓았을 때, 죽이는 나무 수와 죽는 나무의 인덱스
# 3. 제조제는 뿌린 위치, K까지의 대각선 4방향 영향줌.
# 4. 가장 많은 나무를 죽이는 곳에 제초제 뿌림.
# 5. 제초제가 남아있는 년 수 만큼 제초제가 영향을 미친 곳에는 나무가 못자람.
def kill():   
    max_kill = (0, -(n-1), -(n-1)) # 제초제 위치 결정  
    max_kill_pos = []
    for x in range(n):
        for y in range(n):
            kill_pos = [(x, y)]  
            cnt_kill = 0             
            if array[x][y] > 0: # 제초제 뿌린 위치가 나무일 경우 
                cnt_kill += array[x][y]   # 해당위치의 나무수
                for i in range(4):  # 대각선 방향
                    for j in range(1,k+1): 
                        if in_map(x+ddx[i]*j, y+ddy[i]*j):    # 인덱스 유효하다면
                            if array[x+ddx[i]*j][y+ddy[i]*j] > 0: # 나무가 존재하다면
                                cnt_kill += array[x+ddx[i]*j][y+ddy[i]*j] # 죽이는 나무 더함
                                kill_pos.append((x+ddx[i]*j, y+ddy[i]*j))
                            else:  # 빈칸이거나, 해초제 뿌려져있거나, 벽일경우
                                kill_pos.append((x+ddx[i]*j, y+ddy[i]*j))
                                break
                        else: break
            
            if (cnt_kill, -x,  -y) > max_kill:
                max_kill = (cnt_kill, -x,  -y)
                max_kill_pos = kill_pos

    for x in range(n):
        for y in range(n):
            if array[x][y] == -1:    # 벽인경우 제초제 계산안함.
                continue
            if (x,y) in max_kill_pos:   # 방금 뿌린 제초제 영향을 받은 땅
                medicine_map[x][y] = c
                array[x][y] = 0 # 제초제 영향 미친 땅에 나무 0으로
            else:
                # 전에 제초제 뿌려진 땅들은 이제 효력 -1 해야함.
                if medicine_map[x][y] > 0:
                    medicine_map[x][y] -= 1

    return max_kill[0]


year = 0
total = 0
while True:
    empty_pos = growth()
    birth(empty_pos)
    total += kill()


    year += 1
    if year == m:
        print(total)
        break





