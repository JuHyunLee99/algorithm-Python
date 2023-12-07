# 삼성 SW 역량테스트 기출문제
# 놀이기구 탑승
# 골드5
# 시뮬레이션

# n = 3
# students = [[3, 5, 8, 9, 2],
#            [6, 1, 2, 3, 4],
#            [1, 5, 8, 7, 6],
#            [8, 2, 5, 3, 1],
#            [9, 4, 8, 2, 1],
#            [4, 6, 5, 7, 8],
#            [7, 3, 4, 2, 9],
#            [2, 1, 6, 3, 5],
#            [5, 4, 3, 8, 6]]

# 입력
n = int(input())    # 격자 크기
students = []
for i in range(n*n):
    students.append(list(map(int, input().split())))


array = [[0] * n for _ in range(n)] # 탑승한 학생 저장 

# 격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 갑니다.
# 그중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 갑니다. 단 이때 격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다.
# 그 중 행 번호가 가장 작은 위치로 갑니다.
# 그 중 열 번호가 가장 작은 위치로 갑니다.

# 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]
def search(r, c, student):
    empty_cnt = 0
    like_cnt = 0
    if array[r][c] == 0:
        for i in range(4):
            if (r+dx[i]) >= 0 and (c+dy[i]) >= 0 and (r+dx[i])<n and (c+dy[i])<n:
                if array[r+dx[i]][c+dy[i]] == 0:
                    empty_cnt += 1
                elif array[r+dx[i]][c+dy[i]] in student:
                    like_cnt += 1
        return like_cnt, empty_cnt
    else:
        return -1, -1
        


    
for student in students:
    like_temp = []   # 친구가 가장 많이 인접한 칸의 인덱스,  
    max_like_cnt = 0
    empty_array = [[0] * n for _ in range(n)] # 인접한 비어있는 칸의 수
    for r in range(n):
        for c in range(n):
            like_cnt, empty_cnt = search(r, c, student[1:])
            if empty_cnt == -1:
                continue 

            if like_cnt > max_like_cnt:
                max_like_cnt = like_cnt
                like_temp = [(r, c)]
            elif like_cnt == max_like_cnt:
                like_temp.append((r, c))
        
            empty_array[r][c] = empty_cnt

            

    if len(like_temp) == 1: # 친구 인접 가장 많은게 있으면
        array[like_temp[0][0]][like_temp[0][1]] = student[0]   # 이 위치에 탑승
    else:    # 친구 인접 수 같은게 여러개면
        empty_temp = []
        max_empty_cnt = 0 
        for i in like_temp:     # 그 중 
            r, c = i[0], i[1]
            if empty_array[r][c] > max_empty_cnt:     # 빈칸인접이 많은거
                max_empty_cnt = empty_array[r][c]
                empty_temp = [(r, c)]
            elif empty_array[r][c] == max_empty_cnt:
                empty_temp.append((r, c))
        
        if len(empty_temp) == 1:
            array[empty_temp[0][0]][empty_temp[0][1]] = student[0]
        else:
            min_r = n
            r_temp = []
            for i in empty_temp:
                r, c = i[0], i[1]
                if r < min_r:
                    min_r = r
                    r_temp = [(r,c)]
                elif r == min_r:
                    r_temp.append((r,c))
            
            if len(r_temp) == 1:
                array[r_temp[0][0]][r_temp[0][1]] = student[0]
            else:
                min_c = n
                c_tmep = []
                for i in r_temp:
                    r, c = i[0], i[1]
                    if c < min_c:
                        min_c = c
                        c_tmep = [(r, c)]

                array[c_tmep[0][0]][c_tmep[0][1]] = student[0]

                
                    
point = 0
point_list = [0, 1, 10, 100, 1000]
for r in range(n):
    for c in range(n):
            for student in students:
                if array[r][c] == student[0]:
                    like_cnt = 0
                    for i in range(4):
                        if (r+dx[i]) >= 0 and (c+dy[i]) >= 0 and (r+dx[i])<n and (c+dy[i])<n:
                            if array[r+dx[i]][c+dy[i]] in student:
                                like_cnt += 1
                    point += point_list[like_cnt]
                    break



print(point)




    


