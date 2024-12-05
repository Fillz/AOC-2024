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

incorrect_updates = []

for update in updates:
  incorrect_found = False
  for i in range(1, len(update)):
    num = update[i]
    for prev in update[0:i]:
      if prev in rules[num]:
        incorrect_updates.append(update)
        incorrect_found = True
        break

    if incorrect_found:
      break


def modify_if_incorrect(update):
  for i in range(1, len(update)):
    num = update[i]
    for j in range(len(update[0:i])):
      prev = update[j]
      if prev in rules[num]:
        del update[i]
        update.insert(j, num)
        return True

  return False


res = 0

for incorrect_update in incorrect_updates:
  while (True):
    if not modify_if_incorrect(incorrect_update):
      res += int(incorrect_update[len(incorrect_update) // 2])
      break


print(res)
