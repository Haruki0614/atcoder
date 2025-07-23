N, K = map(int, input().split())

if N > K:
    A = [1]*(N+2)
else:
    A = [1]*(K+2)

A[K] = K
for i in range(K+1, N+1):
    A[i] = 2*A[i-1] - A[i-(K+1)]
    A[i] %= (10**9)
print(A[N])