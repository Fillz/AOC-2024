from collections import defaultdict

def get_triple_nodes(edges, current_list):
  if len(current_list) == 3:
    current_list.sort()
    return [(current_list[0], current_list[1], current_list[2])]
  
  common_neighbor_nodes = set(edges[current_list[0]])
  if len(current_list) == 2:
    common_neighbor_nodes = set.intersection(common_neighbor_nodes, set(edges[current_list[1]]))

  res = []
  for other_node in common_neighbor_nodes:
    if other_node in current_list:
      continue
    res += get_triple_nodes(edges, current_list + [other_node])
  return res

inputs = open(0).read().splitlines()
edges = defaultdict(list)
for input in inputs:
  edges[input.split("-")[0]].append(input.split("-")[1])
  edges[input.split("-")[1]].append(input.split("-")[0])

triple_nodes = []
for node in edges:
  triple_nodes += get_triple_nodes(edges, [node])
triple_nodes_set = set(triple_nodes)

count = 0
for triple_node in triple_nodes_set:
  if triple_node[0][0] == "t" or triple_node[1][0] == "t" or triple_node[2][0] == "t":
    count += 1
print(count)