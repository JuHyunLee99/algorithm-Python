# 백트레킹
# 백준 9663 N-Queen 
# 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 퀸을 놓는 방법의 수

n = int(input())

count = 0
col = [0] * (n+1)

def dfs(depth):
    global count
    # 가지치기 조건
    if  col[depth] not in col[1:depth]:    # 같은 열이 존재하지 않고 대각선이 아니어야함.
        for k in range(1, depth):   
             if abs(col[k]-col[depth]) == abs(k-depth): # 대각선이야?
                  return 
                              
        # 깊이 n까지 도착    
        if depth == n:
            count += 1
            return
        
        for i in range(1, n+1):
                col[depth+1] = i       
                dfs(depth + 1)
    else: 
         return

dfs(0)
print(count)