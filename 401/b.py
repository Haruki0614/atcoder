N = int(input())

count = 0
status = 0
for _ in range(N):
    S = input()
    if S == 'login':
        status = 1
    elif S == 'logout':
        status = 0
    elif S == 'private':
        if status == 0:
            count += 1

print(count)