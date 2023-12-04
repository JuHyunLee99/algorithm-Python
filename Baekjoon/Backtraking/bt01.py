# 백트래킹
# 백준 15649
# 1~m까지의 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split())
answer = []

def dfs(depth):
    if depth == m:
        print(*answer)
        return
    
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            dfs(depth+1)
            answer.pop()
            
dfs(0)