from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

n = 3

qc = QuantumCircuit(n, n)

# -----------------------------------
# Step 1 : Equal Superposition
# -----------------------------------
qc.h(range(n))

# -----------------------------------
# Step 2 : Tautology Oracle
# Flip the phase of EVERY basis state
# -----------------------------------
qc.global_phase += np.pi

# -----------------------------------
# Step 3 : Diffusion Operator
# -----------------------------------
qc.h(range(n))
qc.x(range(n))

qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)

qc.x(range(n))
qc.h(range(n))

# -----------------------------------
# Step 4 : Measure
# -----------------------------------
qc.measure(range(n), range(n))

sim = AerSimulator()
compiled = transpile(qc, sim)

result = sim.run(compiled, shots=10000).result()
counts = result.get_counts()

print(counts)
plot_histogram(counts)
plt.show()