import sys

number = set([int(sys.stdin.readline())%42 for _ in range(10)])
answer = len(number)

print(answer)