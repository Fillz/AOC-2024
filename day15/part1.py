lines = open(0).read().splitlines()

map = []
moves = ""

i = 0
while True:
  line = lines[i]
  if not line:
    break
  if line.find("@") != -1:
    robot_y = i
    robot_x = line.find("@")
  map.append(list(line))
  i += 1

for j in range(i + 1, len(lines)):
  moves += lines[j]


def move_items(map, x, y, dx, dy):
  if map[y][x] == "#":
    return False
  if map[y][x] == ".":
    return True
  able_to_move = move_items(map, x + dx, y + dy, dx, dy)
  if able_to_move:
    map[y + dy][x + dx] = map[y][x]
    map[y][x] = "."
  return able_to_move

for move in moves:
  if move == ">":
    dx, dy = (1, 0)
  elif move == "v":
    dx, dy = (0, 1)
  elif move == "<":
    dx, dy = (-1, 0)
  else:
    dx, dy = (0, -1)

  if move_items(map, robot_x, robot_y, dx, dy):
    robot_x += dx
    robot_y += dy

res = 0

for y in range(len(map)):
  for x in range(len(map[y])):
    if map[y][x] == "O":
      res += 100 * y + x

print(res)
