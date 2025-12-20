N, Q = map(int, (input().split()))
A = list(map(int, input().split()))

box = [0] * (N+2)

count = 0

for i in range(Q):
    current = A[i]
    if box[current]:
        if box[current-1] and box[current+1]:
            count += 1
        elif not(box[current-1]) and not(box[current+1]):
            count -= 1

        box[current] = 0

    else:
        if box[current-1] and box[current+1]:
            count -= 1
        elif not(box[current-1]) and not(box[current+1]):
            count += 1
        
        box[current] = 1
    
    print(count)