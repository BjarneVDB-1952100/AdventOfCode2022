def fully_contains(range1, range2):
  lower1, upper1 = map(int, range1.split('-'))
  lower2, upper2 = map(int, range2.split('-'))

  return lower2 >= lower1 and upper2 <= upper1

def overlaps(range1, range2):
  lower1, upper1 = map(int, range1.split('-'))
  lower2, upper2 = map(int, range2.split('-'))

  return lower1 <= upper2 and upper1 >= lower2


with open('input.txt') as f:
  lines = f.readlines()

count = 0

for line in lines:
  range1, range2 = line.split(',')

  if fully_contains(range1, range2) or fully_contains(range2, range1):
    count += 1
print(count)


count = 0

for line in lines:
  range1, range2 = line.split(',')
  if overlaps(range1, range2):
    count += 1
print(count)