import re

lines = open(0).read().splitlines()
input = "".join(lines)

do_list = []

do_start = 0
for i in range(len(input) - 7):
  if input[i:i + 7] == 'don\'t()':
    if do_start == -1:
      continue
    do_list.append(input[do_start:i])
    do_start = -1
  if input[i:i + 4] == 'do()':
    if do_start != -1:
      continue
    do_start = i + 4

if do_start != -1:
  do_list.append(input[do_start:len(input)])

input = "".join(do_list)

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.findall(pattern, input)

res = 0
for match in matches:
  res += int(match[0]) * int(match[1])

print(res)
