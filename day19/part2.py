def fits_in_string(main_string, substring, index):
  if len(substring) + index > len(main_string):
    return False
  for i in range(len(substring)):
    if main_string[index + i] != substring[i]:
      return False
  return True

cache = dict()

def count_arrangements(pattern, pattern_index, towels):
  global cache
  if cache.get((pattern[pattern_index:])):
    return cache[(pattern[pattern_index:])]
  
  if pattern_index >= len(pattern):
    return 1
  count = 0
  for towel in towels:
    if fits_in_string(pattern, towel, pattern_index):
      count += count_arrangements(pattern, pattern_index + len(towel), towels)

  cache[(pattern[pattern_index:])] = count
  return count


lines = open(0).read().splitlines()

towels = lines[0].split(", ")
patterns = []
for i in range(2, len(lines)):
  patterns.append(lines[i])

count = 0
for pattern in patterns:
  count += count_arrangements(pattern, 0, towels)

print(count)