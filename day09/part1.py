input = open(0).read().splitlines()[0]


def get_next_empty(disk, index):
  for i in range(index + 1, len(disk)):
    if disk[i]["type"] == "free":
      return i


def get_next_file(disk, index):
  for i in reversed(range(0, index)):
    if disk[i]["type"] == "file":
      return i


disk = []
id = 0
for i in range(0, len(input)):
  size = int(input[i])
  for j in range(0, size):
    if i % 2 == 0:
      disk.append({"id": id, "type": "file"})
    else:
      disk.append({"id": -1, "type": "free"})
  if i % 2 == 0:
    id += 1

i = get_next_empty(disk, -1)
j = get_next_file(disk, len(disk))

while i < j:
  disk[i] = disk[j]
  disk[j] = {"id": -1, "type": "free"}
  i = get_next_empty(disk, i)
  j = get_next_file(disk, j)

res = 0

for i in range(len(disk)):
  block = disk[i]
  if block["type"] == "free":
    break
  res += i * block["id"]

print(res)
