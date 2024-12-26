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
  def __init__(self, wire_name, value, affected_by_gates):
    self.wire_name = wire_name
    self.value = value
    self.affected_by_gates = affected_by_gates

lines = open(0).read().splitlines()

def init_circuit():
  global lines
  wires = dict()
  gates = []

  i = 0
  while len(lines[i]) != 0:
    w = Wire(lines[i].split(": ")[0], int(lines[i].split(": ")[1]), [])
    wires[w.wire_name] = w
    i += 1

  i += 1
  while i < len(lines):
    input_wire_name_1 = lines[i].split(" ")[0]
    gate_type = lines[i].split(" ")[1]
    input_wire_name_2 = lines[i].split(" ")[2]
    output_wire_name = lines[i].split("> ")[1]

    input_wire_1 = wires.get(input_wire_name_1)
    input_wire_2 = wires.get(input_wire_name_2)
    if not input_wire_1:
      input_wire_1 = Wire(input_wire_name_1, None, [])
      wires[input_wire_name_1] = input_wire_1
    if not input_wire_2:
      input_wire_2 = Wire(input_wire_name_2, None, [])
      wires[input_wire_name_2] = input_wire_2
    output_wire = Wire(output_wire_name, None, [])
    wires[output_wire_name] = output_wire

    output_wire.affected_by_gates = output_wire.affected_by_gates + input_wire_1.affected_by_gates + input_wire_2.affected_by_gates

    gate = Gate([input_wire_1, input_wire_2], gate_type, output_wire)
    gates.append(gate)
    output_wire.affected_by_gates.append(gate)
    i += 1

  return gates


gates = init_circuit()

swaps = set()
for g in gates:
  if g.gate_type != "XOR" and g.output_wire.wire_name[0] == "z" and g.output_wire.wire_name != "z45":
    swaps.add(g.output_wire.wire_name)
  if ((g.input_wires[0].wire_name[0] != "x" and g.input_wires[0].wire_name[0] != "y") and (g.input_wires[1].wire_name[0] != "x" and g.input_wires[1].wire_name[0] != "y")) and g.gate_type == "XOR" and g.output_wire.wire_name[0] != "z":
    swaps.add(g.output_wire.wire_name)
  if ((g.input_wires[0].wire_name[0] in ["x", "y"]) and (g.input_wires[1].wire_name[0] in ["x", "y"])) and g.gate_type == "XOR" and not (g.input_wires[0].wire_name in ["x00", "y00"] and g.input_wires[1].wire_name in ["x00", "y00"]):
    found = False
    for g2 in gates:
      if g2.gate_type == "XOR" and (g2.input_wires[0].wire_name == g.output_wire.wire_name or g2.input_wires[1].wire_name == g.output_wire.wire_name):
        found = True
        break
    if not found:
      swaps.add(g.output_wire.wire_name)
  if ((g.input_wires[0].wire_name[0] in["x", "y"]) and (g.input_wires[1].wire_name[0] in ["x", "y"])) and g.gate_type == "AND" and not (g.input_wires[0].wire_name in ["x00", "y00"] and g.input_wires[1].wire_name in ["x00", "y00"]):
    found = False
    for g2 in gates:
      if g2.gate_type == "OR" and (g2.input_wires[0].wire_name == g.output_wire.wire_name or g2.input_wires[1].wire_name == g.output_wire.wire_name):
        found = True
        break
    if not found:
      swaps.add(g.output_wire.wire_name)
swaps_list = list(swaps)
swaps_list.sort()
print(",".join(swaps_list))