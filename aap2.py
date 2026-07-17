from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(3,3)

qc.h([0,1,2])

# Oracle
qc.h(2)
qc.ccx(0,1,2)
qc.h(2)

# Diffusion
qc.h([0,1,2])
qc.x([0,1,2])
qc.h(2)
qc.ccx(0,1,2)
qc.h(2)
qc.x([0,1,2])
qc.h([0,1,2])

qc.measure([0,1,2],[0,1,2])

sim=AerSimulator()
result=sim.run(transpile(qc,sim),shots=10000).result()

counts=result.get_counts()

print(counts)

plot_histogram(counts)
plt.show()