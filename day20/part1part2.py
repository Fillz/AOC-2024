from dijkstar import Graph, find_path
from collections import defaultdict

def manhattan_dist(n1, n2):
  return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

graph = Graph()
map = open(0).read().splitlines()

for y in range(1,len(map) - 1):
  for x in range(1, len(map[0]) - 1):
    if map[y][x] == "#":
      continue
    if map[y][x] == "S":
      start = (x, y)
    if map[y][x] == "E":
      end = (x, y)
    
    if map[y - 1][x] != "#":
      graph.add_edge((x, y), (x, y - 1), 1)
    if map[y + 1][x] != "#":
      graph.add_edge((x, y), (x, y + 1), 1)
    if map[y][x - 1] != "#":
      graph.add_edge((x, y), (x - 1, y), 1)
    if map[y][x + 1] != "#":
      graph.add_edge((x, y), (x + 1, y), 1)

path, _, _, initial_cost = find_path(graph, start, end)


def calc_time_saved_amounts(max_cheat_amount):
  time_saved_amounts = defaultdict(int)
  for i in range(len(path) - 2):
    node = path[i]
    for j in range(i + 1, len(path)):
      other_node = path[j]
      time_to_other_node = manhattan_dist(node, other_node)
      if time_to_other_node > max_cheat_amount:
        continue
      tot_time = i + time_to_other_node + (len(path) - j - 1)
      if initial_cost - tot_time >= 100:
        time_saved_amounts[initial_cost - tot_time] = time_saved_amounts[initial_cost - tot_time] + 1
  return time_saved_amounts

p1_time_saved_amounts = calc_time_saved_amounts(2)
p2_time_saved_amounts = calc_time_saved_amounts(20)

res = 0
for time_saved in p1_time_saved_amounts:
  res += p1_time_saved_amounts[time_saved]
print(f"Part 1: {res}")
res = 0
for time_saved in p2_time_saved_amounts:
  res += p2_time_saved_amounts[time_saved]
print(f"Part 2: {res}")