import copy

lines = open(0).read().splitlines()

count = 0
for line in lines:
  nums = list(map(int, line.split()))
  
  is_safe = False
  for i in range(len(nums)):
    flag = False
    new_nums = copy.deepcopy(nums)
    if i != len(nums):
      del new_nums[i]

    if new_nums[0] > new_nums[1]:
      increasing = False
    else:
      increasing = True

    for i in range(len(new_nums) - 1):
      if (increasing and new_nums[i] > new_nums[i+1]) or (not increasing and new_nums[i] < new_nums[i+1]) or new_nums[i] == new_nums[i+1] or abs(new_nums[i] - new_nums[i+1]) > 3:
        flag = True
        break

    if flag is True:
      continue
    is_safe = True
    break
  if is_safe:
    count += 1

print(count)
