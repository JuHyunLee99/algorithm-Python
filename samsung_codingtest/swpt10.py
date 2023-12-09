# 삼성 SW 역량테스트 기출문제
# 루돌프의 반란
# 골드2

# n: 게임 판 크기 (1,1)부터
# m 게임 횟수
# p: 산타수
# c: 루돌프가 움직여서 충돌일 때 점수
# d: 산타가 움직여서 충돌일 때 점수
N, M, P, C, D = map(int, input().split())
# (r,c): 루돌프 초기 위치 표기  
r, c = map(int, input().split())
# p_info: [0:산타 번호, 1:pr, 2:pc, 3:점수, 4:생사]   살아있음: 1 죽었음:0 기절했음: 2
p_info = [[0, 0, 0, 0, 0]]  # 산타 인덱스 1부터 시작
for i in range(P):
    p_info.append(list(map(int, input().split()))+[0, 1])

p_info.sort(key=lambda x :x[0])
# 이동 8방향 [왼위, 위, 오위, 오, 오아, 아, 왼아, 왼]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


# 행렬 범위안으로 제한
def in_matrix(x, y):
    if 1 <= x <= N and 1 <= y <= N:
        return True
    False

# 루돌프의 타겟 산타 찾기
def find_target():
    target = (2*(N**2), -(N+1), -(N+1))    # 타겟 산타 (거리, r, c)
    for p in p_info:    # 모든 산타
        if p[4] != 0:        # 살아있는 산타, 기절한 산타 고르기
            # 칸 사이의 거리: (r1-r2)**2 + (c1-c2)**2
            distance  = (r-p[1])**2 + (c-p[2])**2 # 루돌프와의 거리 측정
            # 우선순위로 비교: 거리 가장 가까운 산타 > r이 큰 산타 > c가 큰 산타
            if (distance, -p[1], -p[2]) < target:
                target = (distance, -p[1], -p[2])
    return (target[0], -target[1], -target[2])   # (거리, 산타r, 산타c) 좀있다가 산타 번호도 필요하면 target_num, p[0] 하셈...

# 루돌프 이동 법 (8방향), 1칸 이동
def move_rudolph(target):
    global r, c
    direction = (target[0], -1)   # (산타까지 거리, 방향)
    for i in range(8):
        # 루돌프 이동할 위치
        nx = r+dx[i]
        ny = c+dy[i]
        if in_matrix(nx, ny):   # 필요없을 듯
            # 루돌프 이동할 위치에서 타겟 산타 위치까지 거리 측정
            distance  = (target[1] - nx)**2 + (target[2] - ny)**2
            if distance < direction[0]:
                direction = (distance, i)

    # 루돌프 움직임         
    r, c = r+dx[direction[1]], c+dy[direction[1]]
    
    # 루돌프와 산타의 충돌 여부 확인
    for p in p_info:
        if p[4] != 0:        # 살아있는 산타, 기절한 산타 고르기
            if (r, c) == (p[1], p[2]):  # 산타와 루돌프가 같은 칸이면 충돌
                return (p[0], direction[1]) # 충돌한 산타 번호, 이동방향 반환 
    return (0, -1) # 충돌 안함 반환


# 충돌
def crash(whose_moving, p_num, direction):    # (움직인게 루돌프면 1, 산타면 0 / 충돌 산타 번호)
    if whose_moving == 1:   # 루돌프가 움직여서 충돌
        p_info[p_num][3] += C   # 충돌한 산타 +c 점수
        # 산타는 루돌프가 온 방향으로 c만큼 밀려남(그대로)
        p_info[p_num][1] = p_info[p_num][1] + dx[direction]*C 
        p_info[p_num][2] = p_info[p_num][2] + dy[direction]*C
    else:   # 산타가 움직여서 충돌
        p_info[p_num][3] += D  # 충돌한 산타 +D 점수
        # 산타가 온 방향으로 반대로 d만큼 밀려남(그대로)
        p_info[p_num][1] = p_info[p_num][1] - dx[direction]*D 
        p_info[p_num][2] = p_info[p_num][2] - dy[direction]*D

    # 행렬 위치 확인 후 산타 기절 or 탈락
    if in_matrix(p_info[p_num][1],p_info[p_num][2]):
        p_info[p_num][4] = 3    # 기절  # 3으로 해야지 한게임 정지할 수 있음 3-1하면 2임.
    else:
        p_info[p_num][4] = 0    # 탈락
        return (0, -1) # 연쇄작용 없음 

    # 충돌 여부 확인
    for p in p_info:
        if p[0] != p_info[p_num][0] and p[4] != 0:        # 산타 본인이 아니고, 살아있는 산타, 기절한 산타 고르기
            if (p_info[p_num][1], p_info[p_num][2]) == (p[1], p[2]):  # 밀려난 위치에 다른 산타가 있는 경우
                return (p[0], direction) # 연쇄작용 있음 (충돌한 산타 번호, 이동방향 반환) 
    return (0, -1) # 연쇄작용 없음

# 상호작용
def chain(whose_moving, p_num, direction):
    while True:
        chain_result = False    # 다음 연쇄작용 여부
        if whose_moving == 1:   # 루돌프가 움직여서 충돌
            # 산타는 1칸 밀려남
            p_info[p_num][1] = p_info[p_num][1] + dx[direction]
            p_info[p_num][2] = p_info[p_num][2] + dy[direction]
        else:   # 산타가 움직여서 충돌
            # 산타가 반대로 1칸 밀려남
            p_info[p_num][1] = p_info[p_num][1] - dx[direction] 
            p_info[p_num][2] = p_info[p_num][2] - dy[direction]

        # 행렬 위치 확인 후 산타 연쇄 or 탈락
        if not in_matrix(p_info[p_num][1],p_info[p_num][2]):
            p_info[p_num][4] = 0    # 탈락 -> 연쇄 끝
            break   # while 끝
        
        # 충돌 여부 확인
        for p in p_info:
            if p[0] != p_info[p_num][0] and p[4] != 0:        # 산타 본인이 아니고, 살아있는 산타, 기절한 산타 고르기
                if (p_info[p_num][1], p_info[p_num][2]) == (p[1], p[2]):  # 밀려난 위치에 다른 산타가 있는 경우
                    chain_result = True    # 연쇄작용 일어남
                    p_num = p[0] # 충돌한 산타 번호 업데이트.
                    break   # for 끝. 충돌한 산타 찾음.

        if chain_result == False:   # 연쇄작용 안일어남.
            break   # while 끝.

# 산타 이동법 (4방향) 1칸이동
def move_santa():
    # 1~p번 산타 순서로 이동 
    for p in p_info:
        if p[4] == 1:   # 살아있다면(깨어있다면)
            # 이동할 방향 초기화 
            pre_distance = (r - p[1])**2 + (c - p[2])**2
            direction = (pre_distance, 9)   # (이동 전 루돌프와 산타의 거리, 방향)
            for i in range(1, 8, 2):    # 4방향 이동
                # 산타가 이동할 위치
                nx = p[1]+dx[i]
                ny = p[2]+dy[i]
                if in_matrix(nx, ny):   # 행렬 안에서만
                    # 이동할 위치에 산타가 없을 때만 이동 가능
                    exist_result = False    # 이미 산타 있는지 없는 지 체크
                    for exist_p in p_info:    
                        if p[0] != exist_p[0] and exist_p[4] != 0:        # 산타 본인이 아니고, 살아있는 산타, 기절한 산타 고르기
                            if (nx, ny) == (exist_p[1], exist_p[2]):  # 이미 산타가 있으면
                                exist_result = True
                                break   # 다른 산타가 있는 칸은 갈 수 없음.

                    if exist_result == False:   # 이미 산타가 없다면 갈 수 있음. 
                        # 산타, 루돌프 거리 측정
                        distance  = (r - nx)**2 + (c - ny)**2
                        # 거리 작은 순 -> 상1우2하3좌4 순으로 우선순위
                        if (distance, i) < direction:
                            direction = (distance, i)
            
            # 루돌프로 가까워질 방법이 있다면 이동
            if direction[0] != pre_distance:
                p[1], p[2]  = p[1]+dx[direction[1]], p[2]+dy[direction[1]]  # 산타 1칸 이동


                # 루돌프와 충돌 여부 확인
                if (r, c) == (p[1], p[2]):  # 산타와 루돌프가 같은 칸이면 충돌
                    p_num, chain_direction = crash(0, p[0], direction[1]) # 충돌한 산타 번호, 이동방향 반환
                    if p_num != 0:  # 연쇄작용 있다면
                        chain(0, p_num, chain_direction)

                
cnt_game = 0
while True:
    cnt_game += 1

    # 기절 계산
    for p in p_info:
        # 3: 이전 판에서 기절함, 2: 기절 후 게임 1번 쉬었음.
        if p[4] == 3 or p[4] == 2 :
            p[4] -= 1

    # 타겟 산타 찾기
    target = find_target()    # 반환 (거리, 산타r, 산타c)  
    # 루돌프 움직이기    
    p_num, direction = move_rudolph(target)    # 반환: (충돌한 산타 번호 or 0(충돌x), 연쇄 이동 방향)
    if p_num != 0:    # 충돌했다면
        p_num, chain_direction = crash(1, p_num, direction)   # (충돌한 산타 번호, 이동방향 반환) 
        if p_num != 0:  # 연쇄작용 있다면
            chain(1, p_num, chain_direction)

    # 산타 움직이기
    move_santa()
    # 살아남은 산타 체크
    cnt_live = 0
    for p in p_info:
        if p[4] != 0:
            cnt_live += 1   # 살아남은 산타 카운트
            p[3] += 1       # 살아남은 산타 점수 +1

    if cnt_live == 0 or cnt_game >= M:   # 살아남은 산타가 없다면 or 게임 횟수 끝나면
        score = []
        for p in p_info[1:]:
            score.append(p[3])
        print(*score)
        break   # 게임 끝

