S = input()

count = 0
prev = 0
for i in range(len(S)-1, -1, -1):
    current = int(S[i])
    count += 1 + (current - prev) % 10
    prev = current

print(count)