N = int(input())
A = list(map(int, input().split()))

for i in range(N, -1, -1):
    count = 0
    for j in range(N):
        if i <= A[j]:
            count += 1
    
    if count >= i:
        print(i)
        break
