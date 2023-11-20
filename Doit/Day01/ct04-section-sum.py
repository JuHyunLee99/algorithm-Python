# 입력속도를 개선!/ 단, 주피터 노트북에서는 실행불가/ 
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 5 3
numbers = list(map(int, input().split()))   # 5 4 3 2 1
sums = [0]  # 배열 0번재 인덱스
temp = 0

for i in numbers:
    temp = temp + i # temp 5 9 12 14 15 
    sums.append(temp)   # 합 배열 만들기
    # [0, 5, 9, 12, 14, 15]

for i in range(M):
    x, y = map(int, input().split())
    print(sums[y]-sums[x-1])    # 합 배열에서 구간 합 구하기