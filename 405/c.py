N = int(input())
A = list(map(int, input().split()))

S = 0
result = 0
for i in range(1, N):
    S += A[i - 1]
    result += A[i] * S

print(result)