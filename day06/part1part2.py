import copy

def get_guard_path(map, guard_x, guard_y, guard_x_dir, guard_y_dir):
  visited = dict()
  found_loop = False

  while True:
    if not visited.get((guard_x, guard_y, guard_x_dir, guard_y_dir)):
      visited[(guard_x, guard_y, guard_x_dir, guard_y_dir)] = True
    else:
      found_loop = True
      break

    if guard_x == 0 and guard_x_dir == -1 or guard_x == len(map[0]) - 1 and guard_x_dir == 1 or \
            guard_y == 0 and guard_y_dir == -1 or guard_y == len(map) - 1 and guard_y_dir == 1:
      break

    if map[guard_y + guard_y_dir][guard_x + guard_x_dir] == "#":
      old_x_dir = guard_x_dir
      old_y_dir = guard_y_dir
      guard_x_dir = -old_y_dir
      guard_y_dir = old_x_dir
    else:
      guard_x += guard_x_dir
      guard_y += guard_y_dir
  
  return (visited, found_loop)

map = open(0).read().splitlines()

# Part 1

for i in range(len(map)):
  if "^" in map[i]:
    guard_x_start = map[i].index("^")
    guard_y_start = i
    break

p1_visited, _ = get_guard_path(map, guard_x_start, guard_y_start, 0, -1)
p1_visited_set = set()
for v in p1_visited.keys():
  p1_visited_set.add((v[0], v[1]))
print(f"Part1: {len(p1_visited_set)}")

# Part 2

count = 0

for tile in p1_visited_set:
  new_wall_x = tile[0]
  new_wall_y = tile[1]

  new_map = copy.deepcopy(map)
  new_map[new_wall_y] = new_map[new_wall_y][:new_wall_x] + "#" + new_map[new_wall_y][new_wall_x + 1:]

  _, found_loop = get_guard_path(new_map, guard_x_start, guard_y_start, 0, -1)
  if found_loop:
    count += 1

print(f"Part2: {count}")