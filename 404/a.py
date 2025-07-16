S = input()

alphabet = [0] * 26

for c in S:
    alphabet[ord(c) -ord('a')] += 1

for i in range(26):
    if alphabet[i] == 0:
        print(chr(i + ord('a')))
        break