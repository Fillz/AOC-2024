from collections import defaultdict, deque

class Gate:
  def __init__(self, input_wires, gate_type, output_wire):
    self.input_wires = input_wires
    self.gate_type = gate_type
    self.output_wire = output_wire

  def set_input_wire_value(self, input_wire_name, value):
    for input_wire in self.input_wires:
      if input_wire.wire_name == input_wire_name:
        input_wire.value = value
        return

  def all_inputs_active(self):
    for input_wire in self.input_wires:
      if input_wire.value not in [0,1]:
        return False
    return True
    
  def calculate_output(self):
    i1, i2 = self.input_wires
    if self.gate_type == "AND":
      return i1.value and i2.value
    elif self.gate_type == "OR":
      return i1.value or i2.value
    else:
      return 1 if i1.value != i2.value else 0

class Wire:
  def __init__(self, wire_name, value):
    self.wire_name = wire_name
    self.value = value

def get_wire(wires, sought_wire_name):
  for wire in wires:
    if wire.wire_name == sought_wire_name:
      return wire
  return None

lines = open(0).read().splitlines()

wires = []
wire_to_gates = defaultdict(list)
z_wires = []

i = 0
while len(lines[i]) != 0:
  wires.append(Wire(lines[i].split(": ")[0], int(lines[i].split(": ")[1])))
  i += 1

wires_queue = deque(wires)

i += 1
while i < len(lines):
  input_wire_name_1 = lines[i].split(" ")[0]
  gate_type = lines[i].split(" ")[1]
  input_wire_name_2 = lines[i].split(" ")[2]
  output_wire_name = lines[i].split("> ")[1]

  input_wire_1 = get_wire(wires, input_wire_name_1)
  input_wire_2 = get_wire(wires, input_wire_name_2)
  if not input_wire_1:
    input_wire_1 = Wire(input_wire_name_1, None)
    wires.append(input_wire_1)
  if not input_wire_2:
    input_wire_2 = Wire(input_wire_name_2, None)
    wires.append(input_wire_2)
  output_wire = Wire(output_wire_name, None)
  wires.append(output_wire)

  if output_wire.wire_name[0] == "z":
    z_wires.append(output_wire)

  gate = Gate([input_wire_1, input_wire_2], gate_type, output_wire)
  wire_to_gates[input_wire_name_1].append(gate)
  wire_to_gates[input_wire_name_2].append(gate)
  i += 1

while len(wires_queue) != 0:
  wire = wires_queue.popleft()
  connected_gates = wire_to_gates[wire.wire_name]
  for gate in connected_gates:
    gate.set_input_wire_value(wire.wire_name, wire.value)
    if gate.all_inputs_active():
      gate.output_wire.value = gate.calculate_output()
      wires_queue.append(gate.output_wire)

list_z = []
for wire in wires:
  if wire.wire_name[0] == "z":
    list_z.append((wire.wire_name, wire.value))
list_z.sort()
res = ""
for i in reversed(range(len(list_z))):
  res += str(list_z[i][1])
print(int(res, 2))