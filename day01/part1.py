lines = open(0).read().splitlines()

left_list = []
right_list = []

for line in lines:
  left_item, right_item = map(int, line.split())
  left_list.append(left_item)
  right_list.append(right_item)

left_list.sort()
right_list.sort()

total_distance = 0

for left, right in zip(left_list, right_list):
  total_distance += abs(left - right)

print(total_distance)