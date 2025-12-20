N = int(input())

A = list(map(int, input().split()))

total = 0
for i in range(N):
    if i%2 == 0:
        total += A[i]
    
print(total)