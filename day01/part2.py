lines = open(0).read().splitlines()

left_list = []
right_list = []

for line in lines:
  left_item, right_item = map(int, line.split())
  left_list.append(left_item)
  right_list.append(right_item)

res = sum(left_item * right_list.count(left_item) for left_item in left_list)

print(res)
