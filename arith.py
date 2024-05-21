import numpy as np
import r1cs, witness

# CONSTRAINTS
OUT = np.array(r1cs.OUT)
A = np.array(r1cs.A)
B = np.array(r1cs.B)

# WITNESS
w = np.array(witness.w)

# CHECK CONSTRAINTS
result = OUT.dot(w) == np.multiply(A.dot(w), B.dot(w))
print(result.all())
