# 삼성 SW 역량테스트 기출문제
# 외주 수익 최대화하기 
# 실버3
# 내가 푼 풀이(DFS)

# 입력
n = int(input())    # 휴가 기간 1≤n≤15

work = [] # 외주 기간 t   1≤t≤5 / 외주 수익 p   1≤p≤1,000
for _ in range(n):
    work.append(list(map(int, input().split())))

# 출력 1초
# 외주 수익의 최대값
total = [0] * n

def dfs(day):
    np = [0] * n
    p = 0
    if day+work[day][0] - 1 < n:         # 휴가기간동안 수행할 수 있다면
        p = work[day][1]            # work 수행, 수익 저장
        next_work_day = day+work[day][0]    # 다음 일을 할 수 있는 최소 날짜
        if  next_work_day < n:                # 휴가가 아직 남았다면           
            for next_day in range(day+work[day][0], n): # 다음 일할 수 있는 날짜들
                np.append(dfs(next_day))
    return (p+max(np))




for i in range(n):  
    total[i] = dfs(i)

print(max(total))
    
    