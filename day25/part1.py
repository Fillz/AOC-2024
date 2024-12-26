lines = open(0).read().splitlines()

keys = []
locks = []

i = 0
while i < len(lines):
  current = []
  for x in range(len(lines[0])):
    val = 0
    for y in range(i + 1, i + 6):
      if lines[y][x] == "#":
        val += 1
    current.append(val)
      
  if lines[i][0] == "#":
    locks.append(current)
  else:
    keys.append(current)
  i += 8

count = 0
for lock in locks:
  for key in keys:
    overlaps = False
    for i in range(len(key)):
      if lock[i] + key[i] > 5:
        overlaps = True
        break
    if not overlaps:
      count += 1
print(count)