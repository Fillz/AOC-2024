lines = open(0).read().splitlines()


def find_xmas(lines, current_word, x, y, x_dir, y_dir):
  if current_word == "XMAS":
    return 1
  if len(current_word) == 4:
    return 0
  x += x_dir
  y += y_dir
  if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
    return 0
  return find_xmas(lines, current_word + lines[y][x], x, y, x_dir, y_dir)


count = 0
for y in range(len(lines)):
  for x in range(len(lines[0])):
    count += find_xmas(lines, lines[y][x], x, y, 1, 0)
    count += find_xmas(lines, lines[y][x], x, y, 1, 1)
    count += find_xmas(lines, lines[y][x], x, y, 0, 1)
    count += find_xmas(lines, lines[y][x], x, y, -1, 1)
    count += find_xmas(lines, lines[y][x], x, y, -1, 0)
    count += find_xmas(lines, lines[y][x], x, y, -1, -1)
    count += find_xmas(lines, lines[y][x], x, y, 0, -1)
    count += find_xmas(lines, lines[y][x], x, y, 1, -1)

print(count)
