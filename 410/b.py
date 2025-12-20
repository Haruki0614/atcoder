N, Q = map(int, input().split())
X = list(map(int, input().split()))

box = [0] * N

for i in range(Q):
    if X[i] >= 1:
        box[X[i]-1] += 1
        print(X[i], end=' ')
    else:
        c = min(box)
        for j in range(N):
            if box[j] == c:
                box[j] += 1
                break
        print(j+1, end=' ')

print()