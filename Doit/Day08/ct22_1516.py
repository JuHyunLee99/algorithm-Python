from collections import deque

N = int(input())    # N: 건물 수
A = [[] for _ in range(N+1)]    # A: 건물 데이터 저장 인접 리스트
indegree = [0] * (N+1)  # 진입 차수 리스트
selfBuild = [0] * (N+1) # 자기 자신을 짓는 데 걸리는 시간 리스트

for i in range (1, N+1):
    inputList = list(map(int, input().split()))     # 10 -1   # 10 1 -1 # 4 1 -1  # 4 3 1 -1
    selfBuild[i] = (inputList[0])   # 건물 빌드 시간 데이터 저장
    index = 1
    while True: # 인접리스트
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:   break   # while문 탈출
        A[preTemp].append(i)
        indegree[i] += 1    # 진입 차수 데이터 저장


queue = deque() # 큐 생성
for i in range(1, N+1): # 진입 차수 리스트이 값이 0인 건물(노드)을 큐에 삽입
    if indegree[i] == 0:
        queue.append(i) # 1부터 시작

result = [0] * (N+1)

# 위상 정렬 수행
while queue:    # 큐가 빌 때까지
    now = queue.popleft()   # 큐에서 노드를 현재노드로 가져옴.
    for next in A[now]: # 현재 노드에서 갈 수 있는 노드 탐색(인접리스트) 1 --> 2, 3, 4
        indegree[next] -= 1 # 방문했으니까 -1 
        # 시간 업데이트
        result[next] = max(result[next], result[now]+selfBuild[now])    # max(현재 저장된 값, 현재 출발 노드 + 비용) result[next]가 큰경우가 언제임?
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N+1):
    print(result[i] + selfBuild[i])
