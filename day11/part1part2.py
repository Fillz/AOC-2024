from collections import defaultdict


def blink(stones):
  new_stones = defaultdict(int)
  for stone in stones:
    num = stones[stone]
    stone_str = str(stone)
    if stone == 0:
      new_stones[1] += num
    elif len(stone_str) % 2 == 0:
      s1 = int(stone_str[:len(stone_str) // 2])
      s2 = int(stone_str[len(stone_str) // 2:])
      new_stones[s1] += num
      new_stones[s2] += num
    else:
      new_stones[stone * 2024] += num
  return new_stones


def blink_x_times(stones, x):
  for i in range(x):
    stones = blink(stones)
  return stones


input = list(map(int, open(0).read().splitlines()[0].split(" ")))
stones = defaultdict(int)

for i in range(len(input)):
  stones[input[i]] += 1

print(sum(blink_x_times(stones, 25).values()))
print(sum(blink_x_times(stones, 75).values()))
