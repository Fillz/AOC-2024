from collections import defaultdict

lines = open(0).read().splitlines()

rules = defaultdict(list)
updates = []
updates_reached = False
for line in lines:
  if line == "":
    updates_reached = True
    continue
  if updates_reached:
    updates.append(line.split(","))
  else:
    rules[line.split("|")[0]].append(line.split("|")[1])

res = 0

for update in updates:
  incorrect_found = False
  for i in range(1, len(update)):
    num = update[i]
    for prev in update[0:i]:
      if prev in rules[num]:
        incorrect_found = True
        break

    if incorrect_found:
      break

  if not incorrect_found:
    res += int(update[len(update) // 2])

print(res)
