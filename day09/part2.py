input = open(0).read().splitlines()[0]

handled_files = dict()


def get_next_file(disk, index):
  for i in reversed(range(0, index + 1)):
    if handled_files.get(disk[i]["id"]):
      continue
    if disk[i]["type"] == "file":
      handled_files[disk[i]["id"]] = True
      return i


def move_file_to_first_free_space(disk, file_index):
  file = disk[file_index]
  for i in range(len(disk)):
    chunk = disk[i]
    if chunk["id"] == file["id"]:
      return 0
    if chunk["type"] == "free" and chunk["size"] >= file["size"]:
      remainder_after_move = chunk["size"] - file["size"]
      new_free_chunk = {"id": -1, "size": file["size"], "type": "free"}
      disk[i] = file
      disk[file_index] = new_free_chunk
      if remainder_after_move > 0:
        disk.insert(
          i + 1, {"id": -1, "size": remainder_after_move, "type": "free"})
      return 1


disk = []
id = 0
for i in range(0, len(input)):
  size = int(input[i])

  if i % 2 == 0:
    disk.append({"id": id, "size": size, "type": "file"})
    id += 1
  else:
    disk.append({"id": -1, "size": size, "type": "free"})
i = len(disk) - 1
while i > 0:
  file_index = get_next_file(disk, i)
  if not file_index:
    break
  i += move_file_to_first_free_space(disk, file_index) - 1
res = 0
index = 0
for chunk in disk:
  if chunk["type"] == "free":
    index += chunk["size"]
    continue
  for i in range(chunk["size"]):
    res += chunk["id"] * (index + i)
  index += chunk["size"]

print(res)
