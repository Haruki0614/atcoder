Q = int(input())

q = [0] * 100

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q.append(query[1])
    elif query[0] == 2:
        print(q.pop())
