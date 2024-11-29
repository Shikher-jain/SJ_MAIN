import sys
def main():
    n = int(input().strip())  # Number of gates
    gates = {}  # Gate definitions

    for _ in range(n):
        parts = input().strip().split("=")
        gate_name = parts[0].strip()  # Gate output
        gate_definition = parts[1].strip().split("[(), ]+")
        gates[gate_name] = gate_definition

    t = int(input().strip())
    values = {}
    while True:
        line = input().strip()
        if line.isalpha():

            target_gate = line.strip()
            simulate_circuit(gates, values, target_gate, t)
            break
        parts = line.split(" ")
        input_var = parts[0]
        timings = list(map(int, parts[1:]))
        values[input_var] = timings

def simulate_circuit(gates, values, target_gate, t):
    outputs = {}
    for gate in gates.keys():
        outputs[gate] = [0] * t

    for cycle in range(1, t):
        for gate in gates.keys():
            definition = gates[gate]
            operation = definition[0]
            input1 = definition[1]
            input2 = definition[2]

            value1 = get_value(input1, outputs, values, cycle - 1)
            value2 = get_value(input2, outputs, values, cycle - 1)

            # Compute the output based on the operation
            result = compute_gate(operation, value1, value2)
            outputs[gate][cycle] = result

    # Print the output for the target gate
    target_output = outputs[target_gate]
    print(" ".join(map(str, target_output)))

def get_value(var, outputs, values, cycle):
    if var in values:
        return values[var][cycle]
    else:
        return outputs[var][cycle]

def compute_gate(operation, value1, value2):
    if operation == "AND":
        return value1 & value2
    elif operation == "OR":
        return value1 | value2
    elif operation == "NAND":
        return ~(value1 & value2) & 1  # Keep binary representation
    elif operation == "NOR":
        return ~(value1 | value2) & 1  # Keep binary representation
    elif operation == "XOR":
        return value1 ^ value2
    else:
        return 0  # Invalid operation

if __name__ == "__main__":
    main()

