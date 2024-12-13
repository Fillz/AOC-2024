def solve_equation(a, b, c, d, r1, r2):
  det = a*d - b*c
  return ((d*r1 - b*r2) / det, (a*r2 - c*r1) / det)

def calc(machines):
  res = 0
  for m in machines:
    a, b = solve_equation(m["a"]["x"], m["b"]["x"], m["a"]["y"], m["b"]["y"], m["price"]["x"], m["price"]["y"])
    if a == int(a) and b == int(b):
      res += 3 * int(a) + int(b)
  return res


lines = open(0).read().splitlines()

machines_p1 = []
machines_p2 = []

i = 0
while(i < len(lines)):
  button_a_x, button_a_y = list(map(lambda a: int(a.split("+")[1]), lines[i].split(": ")[1].split(", ")))
  button_b_x, button_b_y = list(map(lambda a: int(a.split("+")[1]), lines[i + 1].split(": ")[1].split(", ")))
  price_x, price_y = list(map(lambda a: int(a.split("=")[1]), lines[i + 2].split(": ")[1].split(", ")))
  machines_p1.append({"a": {"x": button_a_x, "y": button_a_y}, "b": {"x": button_b_x, "y": button_b_y}, "price": {"x": price_x, "y": price_y}})
  machines_p2.append({"a": {"x": button_a_x, "y": button_a_y}, "b": {"x": button_b_x, "y": button_b_y}, "price": {"x": price_x + 10000000000000, "y": price_y + 10000000000000}})
  i += 4

print(f"part 1: {calc(machines_p1)}")
print(f"part 2: {calc(machines_p2)}")