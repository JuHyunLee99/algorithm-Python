import sys
import math

n, m = map(int, sys.stdin.readline().split())
result = [i for i in range(n+1)]

for _ in range(m):
    i , j = map(int, sys.stdin.readline().split())
    a = math.ceil((j - i)/2)
    for _ in range(a):
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1
        
print(*result[1:])
