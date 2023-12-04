# 백트레킹
# 백준 15650
# 1~m까지의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
n, m = map(int, input().split())
answer = []

def dfs(depth):
    if depth == m:
        print(*answer)
        return
    
    for i in range(1, n+1):
        if depth == 0 or i > answer[len(answer)-1]:
            answer.append(i)
            dfs(depth+1)
            answer.pop()
            
            
dfs(0)