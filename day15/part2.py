lines = open(0).read().splitlines()

map = []
moves = ""

i = 0
while True:
  line = lines[i]
  if not line:
    break
  map.append([])
  for j in range(len(line)):
    coord = line[j]
    if coord == "#":
      map[i] += ["#", "#"]
    elif coord == "O":
      map[i] += ["[", "]"]
    elif coord == ".":
      map[i] += [".", "."]
    else:
      map[i] += ["@", "."]
      robot_y = i
      robot_x = len(map[i]) - 2
  i += 1

for j in range(i + 1, len(lines)):
  moves += lines[j]


def move_items(map, x, y, dx, dy):
  if map[y][x] == "#":
    return (False, [])
  if map[y][x] == ".":
    return (True, [])
  if dy != 0:
    if map[y + dy][x + dx] == "[":
      left_able_to_move, left_list_to_move = move_items(map, x, y + dy, dx, dy)
      right_able_to_move, right_list_to_move = move_items(map, x + 1, y + dy, dx, dy)
      able_to_move = left_able_to_move and right_able_to_move
      list_to_move = left_list_to_move + right_list_to_move
    elif map[y + dy][x + dx] == "]":
      left_able_to_move, left_list_to_move = move_items(map, x - 1, y + dy, dx, dy)
      right_able_to_move, right_list_to_move = move_items(map, x, y + dy, dx, dy)
      able_to_move = left_able_to_move and right_able_to_move
      list_to_move = left_list_to_move + right_list_to_move
    else:
      able_to_move, list_to_move = move_items(map, x, y + dy, dx, dy)
  else:
    able_to_move, list_to_move = move_items(map, x + dx, y + dy, dx, dy)
  return (able_to_move, list_to_move + [(x, y)])

for move in moves:
  if move == ">":
    dx, dy = (1, 0)
  elif move == "v":
    dx, dy = (0, 1)
  elif move == "<":
    dx, dy = (-1, 0)
  else:
    dx, dy = (0, -1)

  able_to_move, list_to_move = move_items(map, robot_x, robot_y, dx, dy)
  if able_to_move:
    already_moved = dict()
    for coord in list_to_move:
      x, y = coord
      if already_moved.get((x, y)):
        continue
      map[y + dy][x + dx] = map[y][x]
      map[y][x] = "."
      already_moved[(x, y)] = True
    robot_x += dx
    robot_y += dy

res = 0

for y in range(len(map)):
  for x in range(len(map[y])):
    if map[y][x] == "[":
      res += x + 100 * y

print(res)