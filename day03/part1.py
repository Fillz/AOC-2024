import re

lines = open(0).read().splitlines()
input = "".join(lines)

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

matches = re.findall(pattern, input)

res = 0

for match in matches:
  res += int(match[0]) * int(match[1])

print(res)
