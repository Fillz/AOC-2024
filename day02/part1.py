lines = open(0).read().splitlines()

count = 0
for line in lines:
  nums = list(map(int, line.split()))
  
  if nums[0] > nums[1]:
    increasing = False
  else:
    increasing = True

  flag = False
  for i in range(len(nums) - 1):
    if (increasing and nums[i] > nums[i+1]) or (not increasing and nums[i] < nums[i+1]) or nums[i] == nums[i+1] or abs(nums[i] - nums[i+1]) > 3:
      flag = True
      break
  if flag is True:
    continue
  count += 1

print(count)
