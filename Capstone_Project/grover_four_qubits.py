from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import math

qubits = 4
grover_circ = QuantumCircuit (qubits)

for each in range(qubits):
    grover_circ.h(each)

loop = ((math.pi)/4) * math.sqrt(2 ** qubits)

while loop > 1:

    # Tag Solution with Oracle
    grover_circ.x([0, 1, 3])
    grover_circ.h(3)
    grover_circ.mcx([0, 1, 2], 3)  # multi-controlled Toffoli
    grover_circ.h(3)
    grover_circ.x([0, 1, 3])

    # Grover's Diffusion
    grover_circ.h([0, 1, 2, 3])
    grover_circ.x([0, 1, 2, 3])
    grover_circ.h(3)
    grover_circ.mcx([0, 1, 2], 3)  # multi-controlled Toffoli
    grover_circ.h(3)
    grover_circ.x([0, 1, 2, 3])
    grover_circ.h([0, 1, 2, 3])
    loop -= 1

state = Statevector(grover_circ)
print(" ")
print("State of Quantum Circuit: ", state)

grover_circ.measure_all()

shots = 1000

result = StatevectorSampler().run([grover_circ], shots = shots).result()

counts = result[0].data.meas.get_counts()

prob_dict = {state: c / shots for state, c in counts.items()}

#plot_histogram(prob_dict)
    
#grover_circ.draw("mpl")