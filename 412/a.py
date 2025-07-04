count = 0
N = input()

for i in range(int(N)):
    a, b = map(int, input().split())
    if(a<b):
        count += 1

print(count)