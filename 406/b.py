N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 1
for i in range(N):
    result = result * A[i]
    if result >= 10**K:
        result = 1

print(result)