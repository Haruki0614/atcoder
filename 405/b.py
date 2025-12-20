N, M = map(int, input().split())
A = list(map(int, input().split()))

box = [0] * (M + 1)
count = 0

for i in range(N):
    box[A[i]] += 1

for i in range(1, M+1):
    if box[i] == 0:
        print(0)
        break
else:
    for i in range(N-1, -1, -1):
        box[A[i]] -= 1
        count += 1
        if box[A[i]] == 0:
            print(count)
            break