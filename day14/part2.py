from scipy.spatial import KDTree
import copy

MAP_WIDTH =  101
MAP_HEIGHT = 103

class Robot:
  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
  
  def move(self):
    self.x = (self.x + self.vx) % MAP_WIDTH
    self.y = (self.y + self.vy) % MAP_HEIGHT

def print_map(robots):
  map = []
  for y in range(MAP_HEIGHT):
    row = []
    for x in range(MAP_WIDTH):
      row.append(".")
    map.append(row)
  for r in robots:
    map[r.y][r.x] = "#"
  for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
      print(map[y][x], end="")
    print()

def get_adjacents(robots):
  robot_coords = []
  for r in robots:
    robot_coords.append((r.x, r.y))
  kdtree = KDTree(robot_coords)

  short_dists_amount = 0
  for coord in robot_coords:
    dist, _ = kdtree.query(coord, k=2)
    if dist[1] <= 1.5:
      short_dists_amount += 1
  return short_dists_amount


lines = open(0).read().splitlines()
init_robots = []

for line in lines:
  p = list(map(int, line.split(" ")[0].split("=")[1].split(",")))
  v = list(map(int, line.split(" ")[1].split("=")[1].split(",")))
  init_robots.append(Robot(p[0], p[1], v[0], v[1]))

adjacents = []
robots = copy.deepcopy(init_robots)
for i in range(15000):
  for r in robots:
    r.move()
  adjacents.append((get_adjacents(robots), i))
adjacents.sort(reverse=True)
coord_with_most_adjacents_index = adjacents[0][1]

robots = copy.deepcopy(init_robots)
for i in range(15000):
  for r in robots:
    r.move()
  if i == coord_with_most_adjacents_index:
    print(i + 1)
    print_map(robots)
    break