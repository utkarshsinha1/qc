Quantum Tautology Detection using Grover's Diffusion

This project explores an experimental idea: can Grover's diffusion operator be used for analyzing Boolean functions instead of searching for marked states?

How it works
Prepare an equal superposition of all possible input states using Hadamard gates.
Encode the Boolean function as a phase oracle.
Apply a Grover-style diffusion operator.
Measure the quantum state.
Compare the measurement histogram for different Boolean functions, such as tautologies and non-tautologies.

The motivation is to investigate whether quantum interference can reveal global properties of Boolean functions through changes in the final probability distribution.

Features
Phase oracle implementation in Qiskit
Grover-style diffusion operator
Qiskit Aer simulation
Measurement histogram visualization
Experiments with different Boolean functions
Built With
Python
Qiskit
Qiskit Aer
Matplotlib
Current Status

This is an experimental research project exploring a possible application of known quantum primitives to Boolean function analysis. The implementation is intended for experimentation and learning rather than as a proven algorithm for tautology detection.
