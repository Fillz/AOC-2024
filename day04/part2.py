lines = open(0).read().splitlines()

count = 0
for y in range(1, len(lines) - 1):
  for x in range(1, len(lines[0]) - 1):
    if lines[y][x] == "A" and \
      (lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S" or lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M") and \
      (lines[y + 1][x - 1] == "M" and lines[y - 1][x + 1] == "S" or lines[y + 1][x - 1] == "S" and lines[y - 1][x + 1] == "M"):
      count += 1

print(count)
