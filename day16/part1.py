from dijkstar import Graph, find_path

graph = Graph()
map = open(0).read().splitlines()

for y in range(len(map)):
  for x in range(len(map[0])):
    if map[y][x] == "#":
      continue
    if map[y][x] == "S":
      start = (x, y, "right")
    if map[y][x] == "E":
      end = (x, y)
    
    if map[y - 1][x] != "#":
      graph.add_edge((x, y, "up"), (x, y - 1, "up"), 1)
      graph.add_edge((x, y, "left"), (x, y - 1, "up"), 1001)
      graph.add_edge((x, y, "right"), (x, y - 1, "up"), 1001)
    if map[y + 1][x] != "#":
      graph.add_edge((x, y, "down"), (x, y + 1, "down"), 1)
      graph.add_edge((x, y, "left"), (x, y + 1, "down"), 1001)
      graph.add_edge((x, y, "right"), (x, y + 1, "down"), 1001)
    if map[y][x - 1] != "#":
      graph.add_edge((x, y, "left"), (x - 1, y, "left"), 1)
      graph.add_edge((x, y, "up"), (x - 1, y, "left"), 1001)
      graph.add_edge((x, y, "down"), (x - 1, y, "left"), 1001)
    if map[y][x + 1] != "#":
      graph.add_edge((x, y, "right"), (x + 1, y, "right"), 1)
      graph.add_edge((x, y, "up"), (x + 1, y, "right"), 1001)
      graph.add_edge((x, y, "down"), (x + 1, y, "right"), 1001)

try:
  print(find_path(graph, start, (end[0], end[1], "right"))[3])
except:
  print()
try:
  print(find_path(graph, start, (end[0], end[1], "down"))[3])
except:
  print()
try:
  print(find_path(graph, start, (end[0], end[1], "left"))[3])
except:
  print()
try:
  print(find_path(graph, start, (end[0], end[1], "up"))[3])
except:
  print()