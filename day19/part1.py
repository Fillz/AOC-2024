def fits_in_string(main_string, substring, index):
  if len(substring) + index > len(main_string):
    return False
  for i in range(len(substring)):
    if main_string[index + i] != substring[i]:
      return False
  return True


def can_be_created(pattern, pattern_index, towels):
  if pattern_index >= len(pattern):
    return True
  for towel in towels:
    if fits_in_string(pattern, towel, pattern_index) and can_be_created(pattern, pattern_index + len(towel), towels):
      return True
  return False


lines = open(0).read().splitlines()

towels = lines[0].split(", ")
patterns = []
for i in range(2, len(lines)):
  patterns.append(lines[i])

count = 0
for pattern in patterns:
  if can_be_created(pattern, 0, towels):
    count += 1

print(count)
