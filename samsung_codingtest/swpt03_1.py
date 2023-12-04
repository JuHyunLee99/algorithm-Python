# 삼성 SW 역량테스트 기출문제
# 조삼모사
# 실버2
# 백트래킹

# 입력
n = int(input())    # 일의 양
# 업무 간의 상성 인덱스 1부터 ~ n 까지 사용
p = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]

m = n//2    # 오전에 일의 개수    
# morning_works 아침에 하는 일들, 인덱트 1부터 n//2 사용.
m_works = [0] * (m + 1) # 일의 종류는 0으로 초기화
# 오전과 오후에 상생 최소값
min_value = 100*m*m # 일단 대략 최대값으로 초기화

def dfs(depth):
    # 가지치기 조건(백트래킹)
    # 중복 없게 할려면 m_work에 오름차순 수열이 되도록 하면 됨.
    # 이진 트리 그려보면 이해에 도움이 됨. (백준 15650 참고)
    if m_works[depth] > m_works[depth-1] or depth == 0: 
        # 목적에 도착(재귀 종료) 조건
        if depth == m:
            min_finder()  # 팀별 상생힘 계산하고 차이 최소값 찾는 함수
            return
        else:
            for i in range(1, n+1): # 1번 ~ n번 일 
                m_works[depth+1] = i # i번 일을 아침에 하기로 
                dfs(depth+1)
            return
    return


def min_finder():
    global min_value
    m_power = 0 # 아침 업무 간의 상생
    n_power = 0 # 저녁 업무 간의 상생
    for i in range(1, n+1):
        for j in range(2, n+1):
           if i < j:
                if i in m_works and j in m_works: # 아침 업무이라면
                    m_power += p[i][j] + p[j][i]
                elif i not in m_works and j not in m_works:   # 저녁 업무라면
                    n_power += p[i][j] + p[j][i]

    min_value = min(min_value, abs(m_power-n_power))


dfs(0)
print(min_value)
     
