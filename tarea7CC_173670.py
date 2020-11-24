# Luciano Montes de Oca Villa
# 173670
# Tarea 7 - Computación Cuántica
# Pregunta VI

"""Deutsch-Jozsa algorithm on three qubits in Cirq."""

# Import the Cirq library
import cirq

# Get three qubits -- two data and one target qubit
q0, q1, q2 = cirq.LineQubit.range(3)

# Oracles for constant functions
constant = ("0","1")

# Oracles for balanced functions
balanced = ("x1",
            "x2",
            "notx1",
            "notx2",
            "xor",
            "notxor")

# Dictionary of circuits 
dic = {
       "0": [],
       "1": [cirq.X(q2)],
       "x1": [cirq.CNOT(q0, q2)],
       "x2": [cirq.CNOT(q1, q2)],
       "notx1": [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2)],
       "notx2": [cirq.CNOT(q0, q2), cirq.X(q2)],
       "xor": [cirq.CNOT(q1, q2), cirq.X(q2)],
       "notxor": [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2), cirq.X(q2)]
       }

def print_circuit(key):
    if str(key) == "0":
        print("Circuit for function f_" + str(key) + ": ")
        print("2 : _______")
    else: 
        try: 
            circ = cirq.Circuit()
            circ.append(dic[str(key)][0])
            print("Circuit for function f_" + str(key))
            print(circ)
        except:
            pass 

def your_circuit(oracle):
    """Yields a circuit for the Deutsch-Jozsa algorithm on three qubits."""
    # phase kickback trick
    yield cirq.X(q2), cirq.H(q2)

    # equal superposition over input bits
    yield cirq.H(q0), cirq.H(q1)

    # query the function
    yield oracle

    # interference to get result, put last qubit into |1>
    yield cirq.H(q0), cirq.H(q1), cirq.H(q2)

    # a final OR gate to put result in final qubit
    yield cirq.X(q0), cirq.X(q1), cirq.CCX(q0, q1, q2)
    yield cirq.measure(q2)

# Get a simulator
simulator = cirq.Simulator()

# Execute circuit for oracles of constant value functions
print('Your result on constant functions')
for oracle in constant:
    tag = str(oracle) 
    print("\nFor function f_" + tag + " : \nResult:  ")
    oracle = dic[oracle]
    result = simulator.run(cirq.Circuit(your_circuit(oracle)), repetitions=10)
    print(result)
    print("Circuit for function f_" + tag + ": ")
    circ = cirq.Circuit()
    circ.append(oracle)
    print(circ)
    print("\n")
    
    
# Execute circuit for oracles of balanced functions
print('Your result on balanced functions')
for oracle in balanced:
    tag =  str(oracle)
    print("\nFor function f_" + tag + " : \nResult:  ")
    oracle = dic[oracle]
    result = simulator.run(cirq.Circuit(your_circuit(oracle)), repetitions=10)
    print(result)
    print("Circuit for function f_" + tag + ": ")
    circ = cirq.Circuit()
    circ.append(oracle)
    print(circ)
    print("\n")
