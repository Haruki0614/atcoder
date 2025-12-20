S = []
N = int(input())

count = 0
for i in range(N):
    c, l = input().split()
    l = int(l)
    count += l

    if count > 100:
        print("Too Long")
        break

    for j in range(l):
        S += c

else:
    print(''.join(S))