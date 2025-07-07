N = int(input())
S = [input() for _ in range(N)]

box = set()

for i in range(N):
  for j in range(N):
    if i==j:
      continue
    box.add(S[i] + S[j])

print(len(box))