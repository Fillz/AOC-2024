from collections import defaultdict
from dijkstar import Graph, find_path

map_size = 71
start = (0, 0)
end = (70, 70)

lines = open(0).read().splitlines()
coords = defaultdict(bool)

map = []
for y in range(map_size):
  map.append([])
  for x in range(map_size):
    map[y].append(".")

def create_graph(map):
  graph = Graph()

  for y in range(len(map)):
    for x in range(len(map[0])):
      if map[y][x] == "#":
        continue
      if x - 1 >= 0 and map[y][x - 1] == ".":
        graph.add_edge((x, y), (x - 1, y), 1)
      if x + 1 < len(map[0]) and map[y][x + 1] == ".":
        graph.add_edge((x, y), (x + 1, y), 1)
      if y - 1 >= 0 and map[y - 1][x] == ".":
        graph.add_edge((x, y), (x, y - 1), 1)
      if y + 1 < len(map) and map[y + 1][x] == ".":
        graph.add_edge((x, y), (x, y + 1), 1)
  return graph

i = 0
for line in lines:
  i = i + 1
  x, y = line.split(",")
  map[int(y)][int(x)] = "#"
  graph = create_graph(map)
  try:
    find_path(graph, start, end)
  except:
    print(f"{x},{y}")
    break