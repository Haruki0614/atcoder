N = int(input())

for i in range(int((N-1)/2)):
    print('-', end='')

if N%2 == 0:
    print('==', end='')
else:
    print('=', end='')

for i in range(int((N-1)/2)):
    print('-', end='')
print()