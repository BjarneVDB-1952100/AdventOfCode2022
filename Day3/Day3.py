LETTERS = set(chr(i) for i in range(ord('a'), ord('z')+1)) | set(chr(i) for i in range(ord('A'), ord('Z')+1))

with open('input.txt') as f:
  rucksacks = f.readlines()

total_priority = 0
for rucksack in rucksacks:
  comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
  for letter in LETTERS:
    if letter in comp1 and letter in comp2:
      if letter.islower():
        total_priority += ord(letter) - ord('a') + 1
      else:
        total_priority += ord(letter) - ord('A') + 27
print(total_priority)


total_priority = 0
for i in range(0, len(rucksacks), 3):
  comp1_1, comp2_1 = rucksacks[i][:len(rucksacks[i])//2], rucksacks[i][len(rucksacks[i])//2:]
  comp1_2, comp2_2 = rucksacks[i+1][:len(rucksacks[i+1])//2], rucksacks[i+1][len(rucksacks[i+1])//2:]
  comp1_3, comp2_3 = rucksacks[i+2][:len(rucksacks[i+2])//2], rucksacks[i+2][len(rucksacks[i+2])//2:]
  for letter in LETTERS:
    if (letter in comp1_1 or letter in comp2_1) and (letter in comp1_2 or letter in comp2_2) and (letter in comp1_3 or letter in comp2_3):
      if letter.islower():
        total_priority += ord(letter) - ord('a') + 1
      else:
        total_priority += ord(letter) - ord('A') + 27
print(total_priority)

