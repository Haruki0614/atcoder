N = int(input())
A = list(map(int, input().split()))

sort_A = sorted(set(A))

print(len(sort_A))
for i in sort_A:
    print(i, end=" ")
print()