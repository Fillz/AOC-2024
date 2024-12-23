from collections import defaultdict

already_found = defaultdict(bool)

tot = 0

def get_all_connected(edges, current_list):
  global already_found
  current_list.sort()

  if already_found[tuple(current_list)]:
    return current_list
  already_found[tuple(current_list)] = True

  res = current_list
  for node in edges:
    if node in current_list:
      continue
    node_neighbors = edges[node]
    all_connected = True
    for n in current_list:
      if n not in node_neighbors:
        all_connected = False
        break
    
    if all_connected:
      list_of_connected_nodes = get_all_connected(edges, current_list + [node])
      if len(list_of_connected_nodes) > len(res):
        res = list_of_connected_nodes
  return res

inputs = open(0).read().splitlines()
edges = defaultdict(list)
for input in inputs:
  edges[input.split("-")[0]].append(input.split("-")[1])
  edges[input.split("-")[1]].append(input.split("-")[0])

all_connected_nodes = get_all_connected(edges, [])
all_connected_nodes.sort()
print(",".join(all_connected_nodes))