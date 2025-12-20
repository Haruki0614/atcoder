S = input()

count = 0
for i in range(len(S)):
    if S[i] == '#':
        if count%2 == 0:
            print(i + 1, end=',')
        if count%2 == 1:
            print(i + 1, end='')
            print()
        count += 1