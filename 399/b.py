N = int(input())
P = list(map(int, input().split()))

rank = [0] * N
r = 1

pre_max = float('inf')

while r <= N:
    max = 0
    for i in range(N):
        if max < P[i] and P[i] < pre_max:
            max = P[i]

    count = 0
    for i in range(N):
        if P[i] == max:
            rank[i] = r
            count += 1

    r += count
    pre_max = max 


for i in range(N):
    print(rank[i])
