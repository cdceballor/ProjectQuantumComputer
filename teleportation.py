import numpy as np
from scipy.linalg import hadamard
import matplotlib.pyplot as plt
import math as mt

def firstEval(nm):

    escalar = 1. / (mt.sqrt(2))
    hada=hadamard(2)*escalar
    hada2= np.kron(hada,np.eye(2))

    #Primer estado
    r1 = hada2 @ nm
    print("Evaluamos el primer estado")
    print(r1)
    print()

    #Segundo estado
    cnot = np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.], [0., 0., 1., 0.]])
    r2 = cnot@r1
    print("Evaluamos el segundo estado")
    print(r2)
    #gatex(r2)
    print()

    #Tercera estado
    r3 = hada2@r2
    print("Evaluamos el tercera estado")
    print(r3)
    print()


def secondEval(nm):

    escalar = 1. / (mt.sqrt(2))
    hada=hadamard(2)*escalar
    hada2= np.kron(hada,np.eye(2))

    #Primer estado
    r1 = hada2 @ nm
    print("Evaluamos el primer estado")
    print(r1)

    #Segundo estado
    cnot = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    r2 = cnot@r1
    print("Evaluamos el segundo estado")
    print(r2)

    #Tercera estado
    r3 = hada2@r2
    print("Evaluamos el tercera estado")
    print(r3)

def gatex(q):
    x = np.array([[0,1],[1,0]])
    print("Gate x to q")
    print(x@q)

def gatez(q):
    x = np.array([[1.,0.],[0.,-1.]])
    print("Gate z to q")
    print(x@q)

def IwannaWinThisS(nm0, nm1):
    plt.title('Quantum in state 1 and 2')

    plt.hist(nm0, bins=60, alpha=1, edgecolor='red', linewidth=1, label='Q0')
    plt.hist(nm1, bins=60, alpha=1, edgecolor='blue', linewidth=1, label='Q1')
    plt.legend(loc='upper right')

    plt.grid(True)
    plt.show()
    plt.clf()

def IwannaWinThisQ(q):
    plt.title('Quantum in state 3')
    plt.hist(q, bins=60, alpha=1, edgecolor='black', linewidth=1, label="Q3")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
    plt.clf()

def opq2x(q2):
    print(gatex(q2))

def opq2z(q2):
    print(gatez(q2))

def makeOperation():
    q0 = np.array([[1.,0.],[0.,1.]]).reshape(2,2)
    q1 = np.array([[0.,1.],[0.,1.]]).reshape(2,2)
    q2 = np.array([[0.,1.],[1.,0.]]).reshape(2,2)

    nmq0 = np.kron(q0, q0)
    nmq1 = np.kron(q1, q1)
    nmq2 = np.kron(q0, q0)

    print()

    firstEval(nmq0)
    print("Finaliza el proceso del primer estado")
    secondEval(nmq1)
    print("Finaliza el proceso del segundo estado")
    firstEval(nmq2)
    print("Finaliza el proceso del tercer estado")
    IwannaWinThisS(nmq0, nmq1)
    opq2x(q2)
    opq2z(q2)
    IwannaWinThisQ(q2)
makeOperation()

