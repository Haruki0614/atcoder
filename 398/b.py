A = list(map(int, input().split()))

buket = [0] * 14

for i in range(7):
    buket[A[i]] += 1

two = 0
three = 0

for i in range(14):

    if buket[i] >= 3 and three == 0:
        three = 1
    elif buket[i] >= 2:
        two = 1

if two == 1 and three == 1:
    print('Yes')
else:
    print('No')
