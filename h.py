import numpy as np


## Creamos estado inicial, dos qubit en |0>, es decir |00>
zero = np.array([1,0]).reshape(2,1)
zero_zero = np.kron(zero,zero)

## Aplicamos H al primer cubit del sistema
## Dado que tenemos un sistema de 2 qubits, tenemos que hacer un cambio en H
i = 1/np.sqrt(2)
h_1 = np.array([[i,i],[i,-i]])
h_2 = np.kron(h_1,np.eye(2))

## operamos al primer estado
t1 = h_2 @ zero_zero

## Aplicamos la defincion de CX con el control en el primer qubit y el X en el segundo
X = np.array([[0,1],[1,0]])
C_1_X_2 = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
C_2_X_1 = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])

## Operamos al segundo estado

t2 = C_1_X_2 @ t1

### Operamos al tercer estado con otro H

t3 = h_2 @ t2

## esto deberia dar (0.5,0.5,0.5,-0.5), miren en qiskit
print(t3)

a = 9
o = 2