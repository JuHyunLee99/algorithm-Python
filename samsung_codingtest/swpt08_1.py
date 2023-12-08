# 삼성 SW 역량테스트 기출문제
# 토스트 계란틀
# 골드5
# DFS로 품 (근데 코드트리에 유형 BFS라고 되어있음)

# 입력
n, l, r = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))




# 위 아래 왼쪽 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(depth, x, y, num_pre_depth):

    if x < 0 or y < 0 or x > n-1 or y > n-1: # 범위에서 벗어난다면 리턴
        return False 
    if visited[x][y] == 1:  # 방문했다면 리턴
        return False
    
    global group_num

    if depth == 0:
        visited[x][y] = 1
        group_num += 1 
        group.append([array[x][y]])    # 0번째에는 합
    
    elif l <= abs( num_pre_depth[depth-1] - array[x][y]) <= r:
        visited[x][y] = 1
        group[group_num][0] += array[x][y]
    else:
        return False

    num_pre_depth.append(array[x][y])
    group[group_num].append((x, y))

    for i in range(4):
        dfs(depth+1,x+dx[i],y+dy[i], num_pre_depth)
    
    num_pre_depth.pop()
    return True

    
    

answer = 0

while True:
    visited = [[0] * n for _ in range(n)]   # 방문 처리
    group = [] # 계란 분리
    group_num = -1  # 그룹 넘버

    # 계란 그룹핑
    for i in range(n):
        for j in range(n):
            depth = 0
            num_pre_depth = []
            dfs(depth, i, j, num_pre_depth)

    if group_num == n*n-1:
        break

    # 계란 재배치
    for i in range(len(group)):
        for x, y in group[i][1:]:
            array[x][y] =  group[i][0] // len(group[i][1:])
    answer += 1

    # print(array)

print(answer)
              
   