# 삼성 SW 역량테스트 기출문제
# 불안한 무빙워크
# 골드5
# 시뮬레이션

from collections import deque

# 입력
n, k = map(int, input().split())    # n: 무빙워크 길이, 종료조건인 안정성 0인 칸의 개수
safes = list(map(int, input().split()))  # 각 칸의 안정성
movewalk = deque([[safes[i], 0] for i in range(2*n)])
cnt = 0 # 실험 횟수

while True:
    cnt += 1
    movewalk.rotate(1)
    # 마지막칸 사람 있으면 내리기
    if movewalk[n-1][1] == 1:
        movewalk[n-1][1] = 0

    # 마지막 직전 칸부터 사람있으면 앞으로 옮기기
    for i in range(n-2, -1, -1):
        if movewalk[i][1] == 1: # 사람이 있다면
            if movewalk[i+1][0] > 0 and movewalk[i+1][1] == 0: # 안정성이 0이 아니고 사람 없다면
                movewalk[i][1] = 0
                if i + 1 < n - 1:
                    movewalk[i+1][1] = 1
                movewalk[i+1][0] -= 1
    
    if movewalk[0][0] > 0 and movewalk[0][1] == 0:  #첫번째 칸에 사람이 없고 안정하다면
        movewalk[0][1] = 1
        movewalk[0][0] -= 1

    exit_cnt = 0
    for i in movewalk:
        if i[0] < 1:
            exit_cnt += 1
        
    if exit_cnt >= k:
        print(cnt)
        break
                    
