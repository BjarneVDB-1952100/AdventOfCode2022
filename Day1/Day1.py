file1 = open("txt")
Lines = file1.readlines()

listElfs = [0 for _ in range(257)]
counter = 0
for line in Lines:
    if line == '\n':
        counter += 1
    else:
        listElfs[counter] += int(line)

counter = 0
result = 0
for i in listElfs:
    if counter == 3:
        break
    result += max(listElfs)
    listElfs[listElfs.index(max(listElfs))] = 0
    counter += 1
print(result)