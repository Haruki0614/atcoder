N = int(input())

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

result = 10000

count = 0
for i in range(N):
    for j in range(N):
        if S[i][j] != T[i][j]:
            count += 1
result = min(count, result)

count = 1
for i in range(N):
    for j in range(N):
        if S[N-1-j][i] != T[i][j]:
            count += 1
result = min(count, result)

count = 2
for i in range(N):
    for j in range(N):
        if S[N-1-i][N-1-j] != T[i][j]:
            count += 1
result = min(count, result)

count = 3
for i in range(N):
    for j in range(N):
        if S[j][N-1-i] != T[i][j]:
            count += 1
result = min(count, result)

print(result)