from collections import defaultdict

handled_plots = dict()


def find_unhandled_plot(map):
  for y in range(len(map)):
    for x in range(len(map[0])):
      if (x, y) not in handled_plots:
        return (x, y)
  return None


def find_region(map, x, y, sought_plot_type, region):
  if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map) or map[y][x] != sought_plot_type or (x, y) in region:
    return
  region.append((x, y))
  handled_plots[(x, y)] = True
  find_region(map, x + 1, y, sought_plot_type, region)
  find_region(map, x - 1, y, sought_plot_type, region)
  find_region(map, x, y + 1, sought_plot_type, region)
  find_region(map, x, y - 1, sought_plot_type, region)


def has_perimiter_to_other(map, plot, other_plot):
  x, y = other_plot
  if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map) or map[y][x] != map[plot[1]][plot[0]]:
    return True
  return False


def calculate_corners(map, region):
  corners = 0
  for plot in region:
    x, y = plot
    plot_type = map[y][x]
    if has_perimiter_to_other(map, (x, y), (x - 1, y)) and has_perimiter_to_other(map, (x, y), (x, y - 1)):
      corners += 1
    if has_perimiter_to_other(map, (x, y), (x + 1, y)) and has_perimiter_to_other(map, (x, y), (x, y - 1)):
      corners += 1
    if has_perimiter_to_other(map, (x, y), (x + 1, y)) and has_perimiter_to_other(map, (x, y), (x, y + 1)):
      corners += 1
    if has_perimiter_to_other(map, (x, y), (x - 1, y)) and has_perimiter_to_other(map, (x, y), (x, y + 1)):
      corners += 1
    if x + 1 < len(map[0]) and y + 1 < len(map) and map[y][x + 1] == plot_type and map[y + 1][x] == plot_type and map[y + 1][x + 1] != plot_type:
      corners += 1
    if x - 1 >= 0 and y + 1 < len(map) and map[y][x - 1] == plot_type and map[y + 1][x] == plot_type and map[y + 1][x - 1] != plot_type:
      corners += 1
    if x + 1 < len(map[0]) and y - 1 >= 0 and map[y][x + 1] == plot_type and map[y - 1][x] == plot_type and map[y - 1][x + 1] != plot_type:
      corners += 1
    if x - 1 >= 0 and y - 1 >= 0 and map[y][x - 1] == plot_type and map[y - 1][x] == plot_type and map[y - 1][x - 1] != plot_type:
      corners += 1
  return corners


map = open(0).read().splitlines()

regions = []

while True:
  plot = find_unhandled_plot(map)
  if not plot:
    break
  x, y = plot
  region = []
  find_region(map, x, y, map[y][x], region)
  regions.append(region)

res = 0
for region in regions:
  res += len(region) * calculate_corners(map, region)
print(res)
