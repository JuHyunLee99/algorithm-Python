# 그래프 구현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS 알고리즘
visited = set() # 방문한 노드를 저장할 set
# set (집합(set)자료형)
# set()은 파이썬 내장 자료형 중 하나로, 순서 없이 원소를 담고 중복된 값을 허용하진 않음.


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
            

# 시작 노드 'A'에서 DFS 알고리즘 실행
dfs(visited, graph, 'A')


