import sys

n, m = map(int, sys.stdin.readline().split())
result = [i for i in range(n+1)]

for _ in range(m):
    i , j = map(int, sys.stdin.readline().split())
    result = result[:i] + result[i:j+1][::-1] + result[j+1:]
    # a = result[:i]
    # b = result[i:j+1][::-1]
    # c = result[j+1:]

print(*result[1:])