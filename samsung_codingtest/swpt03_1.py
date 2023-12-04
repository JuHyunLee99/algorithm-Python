# 아직 하는 중...

# 입력
n = int(input())    # 일의 양
# 업무 간의 상성 P
p = [list(map(int, input().split())) for _ in range(n)]
m = n//2 # 한 그룹에 업무 양

# 업무 강도 차이의 최소값
min_value = 100*m*m


def dfs(idx, depth):
    if i == n:
        if len(morning_team) == len(night_team):
            min_value = min(min_value, cla(moring))
    dfs(i+1, morning + [i], night_team)# i번째의 업무를 오후에
    dfs(i+1, morning, night_team + [i])# i번째의 업무를 오후에

        
# tmp: 아침 업무 강도
# tmp2: 저녁 업무 강도
# ans: 업무 강도 차이의 최솟값

# res: 업무 강도

# intensity(c) : 업무 강도 구하는 함수
# def(idx, depth) : 업무 강도 차이의 최솟값을 구하는 함수
dfs(0 , 1)
m_work = [0]