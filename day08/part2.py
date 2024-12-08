from collections import defaultdict

lines = open(0).read().splitlines()
map_x_size = len(lines[0])
map_y_size = len(lines)


def get_antinode_locations(p1, p2):
  res = []
  x_diff = p2[0] - p1[0]
  y_diff = p2[1] - p1[1]
  mul = 1
  while True:
    antinode = (p2[0] + x_diff * mul, p2[1] + y_diff * mul)
    if antinode[0] < 0 or antinode[0] >= map_x_size or antinode[1] < 0 or antinode[1] >= map_y_size:
      break
    res.append(antinode)
    mul += 1
  return res


antennas = defaultdict(list)

for y in range(len(lines)):
  for x in range(len(lines[y])):
    if lines[y][x] != ".":
      antennas[lines[y][x]].append((x, y))

antinodes = set()

for key in antennas.keys():
  for antenna in antennas[key]:
    for other_antenna in antennas[key]:
      if antenna[0] == other_antenna[0] and antenna[1] == other_antenna[1]:
        continue
      found_antinodes = get_antinode_locations(antenna, other_antenna)
      antinodes.update(found_antinodes)
      antinodes.update([antenna, other_antenna])

print(len(antinodes))
