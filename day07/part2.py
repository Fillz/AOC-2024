lines = open(0).read().splitlines()

equations = []

for line in lines:
  equations.append((int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split(" ")))))

def equation_valid(numbers, index, current_value, result):
  if index == len(numbers):
    return current_value == result
  return equation_valid(numbers, index + 1, current_value + numbers[index], result) or \
         equation_valid(numbers, index + 1, current_value * numbers[index], result) or \
         equation_valid(numbers, index + 1, int(str(current_value) + str(numbers[index])), result)

sum = 0

for equation in equations:
  if equation_valid(equation[1], 1, equation[1][0], equation[0]):
    sum += equation[0]

print(sum)