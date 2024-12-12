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
    return 1
  return 0


def calculate_perimiter(map, region):
  res = 0
  for plot in region:
    x, y = plot
    res += has_perimiter_to_other(map, (x, y), (x + 1, y))
    res += has_perimiter_to_other(map, (x, y), (x - 1, y))
    res += has_perimiter_to_other(map, (x, y), (x, y + 1))
    res += has_perimiter_to_other(map, (x, y), (x, y - 1))
  return res


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
  res += len(region) * calculate_perimiter(map, region)
print(res)
