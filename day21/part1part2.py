from functools import cache

numpad = {"7": (0,0), "8": (1,0), "9": (2,0), "4": (0,1), "5": (1,1), "6": (2,1), "1": (0,2), "2": (1,2), "3": (2,2), "#": (0,3), "0": (1,3), "A": (2,3)}
dirpad = {"#": (0,0), "^": (1,0), "A": (2,0), "<": (0,1), "v": (1,1), ">": (2,1)}

@cache
def get_paths(start, end):
  pad = numpad if start in numpad and end in numpad else dirpad
  dx = pad[end][0] - pad[start][0]
  dy = pad[end][1] - pad[start][1]
  if (pad[start][0], pad[start][1] + dy) == pad["#"]:
    return [">"*dx + "<"*-dx + "v"*dy + "^"*-dy + "A"]
  elif (pad[start][0] + dx, pad[start][1]) == pad["#"]:
    return ["v"*dy + "^"*-dy + ">"*dx + "<"*-dx + "A"]
  return [">"*dx + "<"*-dx + "v"*dy + "^"*-dy + "A", "v"*dy + "^"*-dy + ">"*dx + "<"*-dx + "A"]

@cache
def solve(code, depth):
  if depth == 0:
    return len(code)
  res = 0
  for i in range(len(code)):
    paths = get_paths(code[i - 1], code[i])
    if len(paths) == 1:
      res += solve(paths[0], depth - 1)
    else:
      s1 = solve(paths[0], depth - 1)
      s2 = solve(paths[1], depth - 1)
      res += min(s1, s2)
  return res

inputs = open(0).read().splitlines()
p1, p2 = (0, 0)
for input in inputs:
  p1 += solve(input, 3) * int(input[:-1])
  p2 += solve(input, 26) * int(input[:-1])
print(p1)
print(p2)