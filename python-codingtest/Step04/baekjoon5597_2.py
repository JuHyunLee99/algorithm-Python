import sys

aattendance = [int(sys.stdin.readline()) for _ in range(28)]
absent = sorted(set(range(1, 31)) - set(aattendance)) # 집합의 차집합 이용
for a in absent:
    print(a)