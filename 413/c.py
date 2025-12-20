from collections import deque

A = deque()
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        c, x = query[1], query[2]
        A.append([x, c])
    else:
        k = query[1]
        total = 0
        while k > 0:
            x, c = A[0]
            if c <= k:
                total += x * c
                A.popleft()
                k -= c
            else:
                total += x * k
                A[0][1] -= k
                k = 0
        print(total)
