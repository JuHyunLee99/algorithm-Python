import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())    # N: 원소 개수 / M: 질의 개수
parent =[0] * (N+1) # 대표 노드 저장 리스트

# find 연산
def find(a):
    if a == parent[a]:  # a가 대표면 리턴
        return a
    else:   # 아니면 a의 대표 노드값을 find(parent[a])값으로 저장 -> 재귀 함수 형태 -> 경로압축!!
        parent[a] = find(parent[a])
        return parent[a]

# union 연산
def  union(a,b):    # 대표노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:  return True
    return False

for i in range(0, N+1):
    parent[i] = i  # parent[i] 초기화 [0, 1, 2, 3, 4, ..., N]

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a,b):
            print('Yes')
        else:
            print('No')