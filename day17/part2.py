import math

lines = open(0).read().splitlines()

register_a = int(lines[0].split(": ")[1])
register_b = int(lines[1].split(": ")[1])
register_c = int(lines[2].split(": ")[1])
init_register_b = register_b
init_register_c = register_c
program = lines[4].split(": ")[1].split(",")
output = []

def combo_operand(operand):
  global register_a
  if operand >= 0 and operand <= 3:
    return operand
  elif operand == 4:
    return register_a
  elif operand == 5:
    return register_b
  elif operand == 6:
    return register_c

def adv(operand):
  global register_a
  register_a = register_a // int(math.pow(2, combo_operand(operand)))

def bxl(operand):
  global register_b
  register_b = register_b ^ operand

def bst(operand):
  global register_b
  register_b = combo_operand(operand) % 8

def jnz(operand):
  global register_a
  if register_a == 0:
    return -1
  return operand

def bxc(operand):
  global register_b, register_c
  register_b = register_b ^ register_c

def out(operand):
  global output  
  output.append(str(combo_operand(operand) % 8))

def bdv(operand):
  global register_a, register_b
  register_b = register_a // int(math.pow(2, combo_operand(operand)))

def cdv(operand):
  global register_a, register_c
  register_c = register_a // int(math.pow(2, combo_operand(operand)))

def run():
  global output, register_a, register_b, register_c, init_register_b, init_register_c
  output = []
  register_b = init_register_b
  register_c = init_register_c
  instruction_pointer = 0
  while True:
    if instruction_pointer >= len(program):
      break
    opcode = int(program[instruction_pointer])
    operand = int(program[instruction_pointer + 1])
    if opcode == 0:
      adv(operand)
    elif opcode == 1:
      bxl(operand)
    elif opcode == 2:
      bst(operand)
    elif opcode == 3:
      new_instruction_pointer = jnz(operand)
      if new_instruction_pointer != -1:
        instruction_pointer = new_instruction_pointer - 2
    elif opcode == 4:
      bxc(operand)
    elif opcode == 5:
      out(operand)
    elif opcode == 6:
      bdv(operand)
    elif opcode == 7:
      cdv(operand)

    instruction_pointer += 2

prev = 0
for i in reversed(range(1, len(program))):
  num = program[i]
  for j in range(20):
    a = prev * 8 + j
    register_a = a
    run()
    if output[0] == program[i]:
      prev = (prev * 8 + j)
      break

for i in range(prev * 8, prev * 8 + 1000):
  register_a = i
  run()
  if output == program:
    print(i)
    break