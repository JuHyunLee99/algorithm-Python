import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())    # V(노드 개수), E(에지 개수)
K = int(input())    # K(출발 노드)
distance = [sys.maxsize] * (V+1)    # 충분히 큰 수로 초기화(무한대)
visited = [False] * (V + 1) # 방문 여부 저장 리스트
myList = [[] for _ in range(V+1)]   # 에지 데이터 저장 인접 리스트
q = PriorityQueue() # 다익스트라를 위한 우선순위 큐

# 인접 리스트
for _ in range(E):  # 엣지 개수만큼 반복
    u, v, w = map (int, input().split())    # u --> v 엣지 w 가중치
    myList[u].append((v,w))

# 다익스트라 수행
# 출발노드K 우선순위 큐에 넣고 시작 
q.put((0, K))   # queue 넣을때는 가중치, 노드 순
distance[K] = 0 # 거리 리스트에 출발 노드의 값을 0으로 설정

while q.qsize() > 0:    # 큐가 빌때 까지
    current = q.get()   # 자동으로 거리가 최소인 노드를 선택
    c_v = current[1]    # 노드
    if visited[c_v]:    # 현재 노드 방문 여부 확인
        continue        
    visited[c_v] = True # 현재 노드를 방문 노드로 업데이트
    for tmp in myList[c_v]: # 현재 선택 노드의 에지 개수
        next = tmp[0]   # 현재 노드와 연결된 노드
        value = tmp[1]  # 가중치
        if distance[next] > distance[c_v] + value:  # 최소 거리로 업데이트
            distance[next] = distance[c_v] + value
            # 가중치가 정렬 기준이므로 순서를 가중치, 목표 노드 순으로 우선순위 큐 설정
            q.put((distance[next],next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")    # 방문한적 없는 노드는 연결X
        