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


lines = open(0).read().splitlines()
robots = []

for line in lines:
  p = list(map(int, line.split(" ")[0].split("=")[1].split(",")))
  v = list(map(int, line.split(" ")[1].split("=")[1].split(",")))
  robots.append(Robot(p[0], p[1], v[0], v[1]))

for i in range(100):
  for r in robots:
    r.move()

q1, q2, q3, q4 = (0, 0, 0, 0)
for r in robots:
  if r.x < MAP_WIDTH // 2 and r.y < MAP_HEIGHT // 2:
    q1 += 1
  elif r.x > MAP_WIDTH // 2 and r.y < MAP_HEIGHT // 2:
    q2 += 1
  elif r.x < MAP_WIDTH // 2 and r.y > MAP_HEIGHT // 2:
    q3 += 1
  elif r.x > MAP_WIDTH // 2 and r.y > MAP_HEIGHT // 2:
    q4 += 1

print(q1 * q2 * q3 * q4)