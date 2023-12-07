# 삼성 SW 역량테스트 기출문제
# 나무 타이쿤
# 골드5
# 시뮬레이션

# 입력
n, m = map(int, input().split()) # 격자 크기, 총 년 수
# 각 격자에 식물 높이
array = [list(map(int, input().split())) for _ in range(n)] 
d = [0]*m   # 이동 방향 → ↗ ↑ ↖ ← ↙ ↓ ↘
p = [0]*m   # 이동 칸의 수
for i in range(m):
    d[i], p[i] = map(int, input().split())

# 이동 방향 0 → ↗ ↑ ↖ ← ↙ ↓ ↘
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
# 대각선 인덱스 ↗ ↖ ↙ ↘
dxy = [2, 4, 6, 8]

def set_index(x):
    return x % n

def in_range(x, y):
    if x < n and y < n and x >= 0 and y>=0:
        return True
    return False

def move(vita, d, p):    # 영양제 위치, 이동 방향, 이동수
    new_vita = [] # 새로운 영양제 위치 저장
    for i, j in vita:
        new_vita.append((set_index(i+dx[d]*p),set_index(j+dy[d]*p)))
    return new_vita

def grow_1(vita):   # 높이 1만큼 성장
    for i, j in vita:
        array[i][j] += 1


def grow_dxy(vita): # 대각선에 높이 1이상인 리브로수 수만큼 성장
    for i, j in vita:
        cnt = 0
        for k in dxy:
            if in_range(i+dx[k], j+dy[k]):
                if array[i+dx[k]][j+dy[k]] >= 1:
                    cnt +=1
        array[i][j] += cnt

def put_vita(vita):
    new_vita = []

    for i in range(n):
        for j in range(n):
            if (i,j) not in vita:
                if array[i][j] >= 2:
                    array[i][j] -= 2
                    new_vita.append((i, j))
    return new_vita
                


for year in range(m):
    if year == 0:
        vita = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)]
    
    vita = move(vita, d[year], p[year])
    grow_1(vita)
    grow_dxy(vita)
    vita = put_vita(vita)

answer = 0
for i in range(n):
        for j in range(n):
            answer += array[i][j]

print(answer)
