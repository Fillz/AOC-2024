from heapq import heappop, heappush
from collections import defaultdict


class Graph:
  def __init__(self):
    self.edges = defaultdict(list)

  def add_edge(self, from_node, to_node, weight):
    self.edges[from_node].append((to_node, weight))


def find_all_shortest_paths(graph, start, ends):
  priority_queue = []
  heappush(priority_queue, (0, start, [start]))

  min_cost = defaultdict(lambda: float('inf'))
  min_cost[start] = 0
  shortest_paths = defaultdict(list)

  shortest_paths[start].append([start])

  while priority_queue:
    current_cost, current_node, current_path = heappop(priority_queue)

    if current_cost > min_cost[current_node]:
      continue

    for neighbor, weight in graph.edges[current_node]:
      new_cost = current_cost + weight

      if new_cost < min_cost[neighbor]:
        min_cost[neighbor] = new_cost
        shortest_paths[neighbor] = [current_path + [neighbor]]
        heappush(priority_queue, (new_cost, neighbor,
                 current_path + [neighbor]))

      elif new_cost == min_cost[neighbor]:
        shortest_paths[neighbor].append(current_path + [neighbor])
        heappush(priority_queue, (new_cost, neighbor,
                 current_path + [neighbor]))

  all_paths = []
  for end in ends:
    if end in shortest_paths:
      all_paths.extend(shortest_paths[end])

  return all_paths, min_cost


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

end_states = [
    (end[0], end[1], "right"),
    (end[0], end[1], "down"),
    (end[0], end[1], "left"),
    (end[0], end[1], "up"),
]

all_paths, costs = find_all_shortest_paths(graph, start, end_states)

res = set()

for path in all_paths:
  for coord in path:
    res.add((coord[0], coord[1]))
print(len(res))