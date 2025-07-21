from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit (3)

circuit.h(0)
circuit.cx(0, 1)
circuit.cx(0, 2)

state = Statevector(circuit)
print("State of Quantum Circuit: ", state)

circuit.measure_all()

shots = 1000

result = StatevectorSampler().run([circuit], shots = 1000).result()[0]

counts = result.data.meas.get_counts()

print(counts)

prob_dict = {state: c / shots for state, c in counts.items()}

#circuit.draw("mpl")
#plot_histogram(prob_dict)