answer = []
for i in range(3):
  answer.append(input())

guess = []
for i in range(3):
  guess.append(input())

green = 0
yellow = 0

freq = [0] * 26

for i in answer:
  for j in i:
    freq[ord(j) - ord('A')]+=1

for i in range(3):
  for j in range(3):
    if answer[i][j] == guess[i][j]:
      green+=1
      freq[ord(answer[i][j]) - ord('A')]-=1

for i in range(3):
  for j in range(3):
    if guess[i][j] != answer[i][j] and freq[ord(guess[i][j]) - ord('A')] > 0:
      yellow+=1
      freq[ord(guess[i][j]) - ord('A')]-=1

print(green)
print(yellow)