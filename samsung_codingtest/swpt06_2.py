EMPTY = 0

# 변수 선언 및 입력:
n = int(input())

target_num = [
    0 for _ in range(n * n + 1)
]
friends = [
    [False for _ in range(n * n + 1)]
    for _ in range(n * n + 1)
]

# 놀이 기구 탑승 번호
rides = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] 


def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# num2가 num1이 좋아하는 친구인지 판단합니다.
def is_friend(num1, num2):
    return friends[num1][num2]


# 우선순위에 따라 쉽게 계산하기 위해
# (좋아하는 친구 수, 빈 칸의 수, -행 번호, -열 번호)
# 순서대로 값을 넣어줍니다.
def get_curr_cell(num, x, y):
    friend_cnt, blank_cnt = 0, 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        
        if rides[nx][ny] == EMPTY:
            blank_cnt += 1
        elif is_friend(num, rides[nx][ny]):
            friend_cnt += 1
    return (friend_cnt, blank_cnt, -x, -y)


def move(num):
    # Step1. 가장 우선순위가 높은 칸을 선택합니다.
    best_cell = (0, 0, -(n + 1), -(n + 1))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if rides[i][j] == EMPTY:
                curr = get_curr_cell(num, i, j)

                if best_cell < curr:
                    best_cell = curr

    # Step2. 해당 위치에 탑승합니다.
    _, _, x, y = best_cell
    rides[-x][-y] = num


# (x, y) 위치에 있는 학생의 점수를 계산합니다.
def get_score(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and \
           is_friend(rides[x][y], rides[nx][ny]):
            cnt += 1

    return int(10 ** (cnt - 1))


# 총 점수를 계산합니다.
def get_total_score():
    return sum([
        get_score(i, j)
        for i in range(1, n + 1)
        for j in range(1, n + 1)
    ])


for i in range(1, n * n + 1):
    student_data = list(map(int, input().split()))
    
    target_num[i] = student_data[0]
    for friend_num in student_data[1:]:
        # 현재 번호에 친구 번호를 표시해줍니다.
        friends[target_num[i]][friend_num] = True

# 순서대로 학생들을 놀이기구에 탑승시킵니다.
for i in range(1, n * n + 1):
    move(target_num[i])

# 총 점수를 계산합니다.
ans = get_total_score()
print(ans)