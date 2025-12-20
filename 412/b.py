S = str(input())
T = str(input())

count = 1
for i in range(1, len(S), 1):
    if(S[i].isupper()):
        flag = 0
        for j in range(len(T)):
            if(S[i-1] == T[j]):
                flag = 1
        if(flag == 0):
            count = 0

if(count == 1):
    print("Yes")
else:
    print("No")
