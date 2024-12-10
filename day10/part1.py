import copy


def search_trailhead(x, y, map, visited, prev, found_tops):
  if (x, y) in visited or x < 0 or x >= len(map[0]) or y < 0 or y >= len(map) or prev != int(map[y][x]) - 1 or (x, y) in found_tops:
    return 0
  if map[y][x] == "9":
    found_tops.append((x, y))
    return 1
  return search_trailhead(x - 1, y, map, copy.deepcopy(visited) + [(x, y)], int(map[y][x]), found_tops) + \
         search_trailhead(x + 1, y, map, copy.deepcopy(visited) + [(x, y)], int(map[y][x]), found_tops) + \
         search_trailhead(x, y - 1, map, copy.deepcopy(visited) + [(x, y)], int(map[y][x]), found_tops) + \
         search_trailhead(x, y + 1, map, copy.deepcopy(visited) + [(x, y)], int(map[y][x]), found_tops)


map = open(0).read().splitlines()
trailhead_starts = []

for y in range(len(map)):
  for x in range(len(map[0])):
    if map[y][x] == "0":
      trailhead_starts.append((x, y))

res = 0

for trailhead_start in trailhead_starts:
  res += search_trailhead(trailhead_start[0], trailhead_start[1], map, [], -1, [])

print(res)
