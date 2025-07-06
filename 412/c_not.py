T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    
    start = S[0]
    end = S[-1]
    middle = sorted(S[1:-1])

    current = start
    count = 2

    if current * 2 >= end:
        print(count)
        continue

    found = False
    for m in middle:
        if m <= current * 2:
            current = m
            count += 1
            if current * 2 >= end:
                print(count)
                found = True
                break
        else:
            break

    if not found:
        if current * 2 >= end:
            print(count)
        else:
            print(-1)
