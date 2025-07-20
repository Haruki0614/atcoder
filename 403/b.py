T = input()
U = input()

for i in range(len(T) - len(U) + 1):
    match = True
    for j in range(len(U)):
        if T[i + j] != U[j] and T[i + j] != '?':
            match = False
            break
    if match:
        print("Yes")
        exit()

print("No")