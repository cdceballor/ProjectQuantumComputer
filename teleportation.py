import numpy as np
from scipy.linalg import hadamard
import math as mt

def Hadamart(A):
    print("Salida Hadamart")
    escalar = 1 / (mt.sqrt(2))
    print(hadamard(4)*escalar)
    print()
"""
    sol = A

    escalar = 1 / (mt.sqrt(2))
    for i in range(len(A)):
        for j in range(len(A[i])):
            p = A[i][j] * escalar
            sol[i][j] = p
    print("Salida de la Hadammart")
    print(sol)
"""

def Cnot(A):
    #other_matrix = np.array([[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]])
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    print("Salida de la CNOT")
    print(np.dot(A, cnot))
    print()


def makeOperation():
    A = np.array([[1.0,2.0,3.0,4.0],[1.0,2.0,3.0,4.0],[5.0,6.0,8.0,87.5],[2.0,7.0,9.0,32.2]])

    Hadamart(A)
    Cnot(A)


makeOperation()
