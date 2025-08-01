S = input()

count = 0
for i in range(len(S)):
    if (i+count)%2 == 0 and S[i] != 'i':
        count += 1
    elif (i+count)%2 == 1 and S[i] != 'o':
        count += 1


if (len(S)+count) % 2 == 1:
    count += 1
print(count)