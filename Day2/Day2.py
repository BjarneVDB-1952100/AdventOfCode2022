file1 = open("input.txt")
Lines = file1.readlines()
score = 0
for line in Lines:
    if line.split()[0] == 'A':
        if line.split()[1] == 'Y':
            score += 2
            score += 6
        if line.split()[1] == 'X':
            score += 1
            score += 3
        if line.split()[1] == 'Z':
            score += 3
            score += 0
    if line.split()[0] == 'B':
        if line.split()[1] == 'Y':
            score += 2
            score += 3
        if line.split()[1] == 'X':
            score += 1
            score += 0
        if line.split()[1] == 'Z':
            score += 3
            score += 6
    if line.split()[0] == 'C':
        if line.split()[1] == 'Y':
            score += 2
            score += 0
        if line.split()[1] == 'X':
            score += 1
            score += 6
        if line.split()[1] == 'Z':
            score += 3
            score += 3

print("Challenge 1:" + str(score))
score = 0
for line in Lines:
    if line.split()[0] == 'A':
        if line.split()[1] == 'Y':
            score += 1
            score += 3
        if line.split()[1] == 'X':
            score += 3
            score += 0
        if line.split()[1] == 'Z':
            score += 2
            score += 6
    if line.split()[0] == 'B':
        if line.split()[1] == 'Y':
            score += 2
            score += 3
        if line.split()[1] == 'X':
            score += 1
            score += 0
        if line.split()[1] == 'Z':
            score += 3
            score += 6
    if line.split()[0] == 'C':
        if line.split()[1] == 'Y':
            score += 3
            score += 3
        if line.split()[1] == 'X':
            score += 2
            score += 0
        if line.split()[1] == 'Z':
            score += 1
            score += 6

print("Challenge 2:" + str(score))
file1.close()