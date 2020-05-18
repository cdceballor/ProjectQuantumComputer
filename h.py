from scipy.linalg import hadamard
import math as mt
from sympy.physics.quantum.gate import H
from sympy.physics.quantum.gate import CNOT
from sympy.physics.quantum.gate import CNotGate
from sympy.physics.quantum.gate import HadamardGate


escalar = 1. / (mt.sqrt(2.))
p = hadamard(4)

"""
print("Hadamard ")
print(p)

print("Hadamard por escalar")
print(p*escalar)

print("Hadamard dividido escalar")
print(p/escalar)
"""