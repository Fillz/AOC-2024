from collections import defaultdict

lines = open(0).read().splitlines()


def get_antinode_location(p1, p2):
  return (2 * p2[0] - p1[0], 2 * p2[1] - p1[1])


antennas = defaultdict(list)
map_x_size = len(lines[0])
map_y_size = len(lines)

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
      antinode = get_antinode_location(antenna, other_antenna)
      if antinode[0] >= 0 and antinode[0] < map_x_size and antinode[1] >= 0 and antinode[1] < map_y_size:
        antinodes.add(antinode)

print(len(antinodes))
