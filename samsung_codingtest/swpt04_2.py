# 삼성 SW 역량테스트 기출문제
# 연산자 배치하기
# 백준에는 나누기 추가 / 음수 나누기도 고려해야함.
# 실버1
# 백트래킹

# 입력
n = int(input())    # 자연수의 개수
nums = list(map(int, input().split()))  # 숫자들
# + - * // 연산자 개수,  oper[0]: '+'의 개수
oper = list(map(int, input().split()))

# 출력
min_value = 1000000000  # 최소값 초기화
max_value = -100000000 # 초대값 초기화

# 연산 결과 저장 앗...  연산결과를 깊이별로 저장해야겠네...
# result = 0 # 리스트로 변경
# 리스트 크기는 자연수 개수 / 인덱스0은 첫번째 자연수
result = [nums[0]] + ([0] * (n-1))
# 연산자의 남은 갯수 표현도 리스트로 변경
depth_oper = [[oper[0], oper[1], oper[2], oper[3]]] + ([[0]*len(oper)] * (n-1))

def dfs(depth):
    global min_value, max_value
    # if result[depth] > 1000000000 or result[depth] < -1000000000:
    #     return
    
    if depth == n - 1:  # 연산자 다 사용
        max_value = max(max_value, result[depth])
        min_value = min(min_value, result[depth])
        return


    for i in range(len(oper)):  # 연산자 종류별로
        if depth_oper[depth][i]:         # 연사자의 사용가능 갯수가 남아있다면
            # depth_oper[depth + 1] = depth_oper[depth]   # 연산자의 사용가능 갯수 부모노트에서 복사
            # 위에처럼하면 얕은 복사됨... 파이썬에서 리스트 복사는 얕은 복사를 기본으로 함.
            # -> 깊은 복사 모듈 쓰던지 따로따로 값형식을 복사 하면 될듯..
            a, b, c, d = depth_oper[depth][0], depth_oper[depth][1], depth_oper[depth][2], depth_oper[depth][3] 
            depth_oper[depth + 1] = [a, b, c, d]       
            depth_oper[depth + 1][i] -= 1 # 해당 연산자 개수 삭감
            if i == 0:              # 연산자 종류별 계산
                result[depth+1] = result[depth] + nums[depth + 1]
            elif i == 1:
                result[depth+1] = result[depth] - nums[depth + 1]
            elif i == 2:
                result[depth+1] = result[depth] * nums[depth + 1]
            else:
                if result[depth] < 0:   # 음수를 양수로 나눌때 c++기준
                    result[depth+1] = -((-result[depth]) // nums[depth + 1])
                else:
                    result[depth+1] = result[depth] // nums[depth + 1]         
            dfs(depth+1)

dfs(0)
print(max_value)
print(min_value)