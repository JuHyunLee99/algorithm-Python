# 삼성 SW 역량테스트 기출문제
# 토스트 계란틀
# 골드5
# BFS로 품
from collections import deque
# 입력
n, l, r = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))




# 위 아래 왼쪽 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    group = []
    group_sum = 0

    while queue:
        x, y = queue.popleft()

        if visited[x][y] == 1:  # 방문했다면 리턴
            continue
        
        visited[x][y] = 1
        group.append((x, y))    # 0번째에는 합
        group_sum += array[x][y]
        
        for i in range(4):
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n: # 범위 안이다
               if visited[x+dx[i]][y+dy[i]] != 1:  # 방문하지 않았다.
                   if l <= abs( array[x+dx[i]][y+dy[i]] - array[x][y]) <= r:
                        queue.append((x+dx[i],y+dy[i]))

    if group:
        groups.append([group_sum]+group)

    
    

answer = 0

while True:
    visited = [[0] * n for _ in range(n)]   # 방문 처리
    groups = [] # 계란 분리

    # 계란 그룹핑
    for x in range(n):
        for y in range(n):
            bfs(x,y)

    if len(groups) == n*n:
        break

    # 계란 재배치
    for i in range(len(groups)):
        for x, y in groups[i][1:]:
            array[x][y] =  groups[i][0] // len(groups[i][1:])
    answer += 1

    # print(array)

print(answer)
              
   