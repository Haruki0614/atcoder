N, Q = map(int, input().split())
A = [i+1 for i in range(N)]
off = 0

for i in range(Q):
    query = list(map(int, input().split()))
    t = query[0]

    if t == 1:
        p, x = query[1]-1, query[2]
        A[(p+off)%N] = x

    elif t == 2:
        p = query[1]-1
        print(A[(p+off)%N])

    elif t == 3:
        k = query[1]
        off = (off + k) % N