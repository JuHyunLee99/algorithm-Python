# 프로그래머스 탬플릿 소스
# 코딩테스트 입문
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i

    return answer / len(numbers)
