import numpy as np
import r1cs, witness

# CONSTANTS
P = 97

# CONSTRAINTS
OUT = np.array(r1cs.OUT)
A = np.array(r1cs.A)
B = np.array(r1cs.B)

# WITNESS
w = np.array([i % P for i in witness.w])

# HELPER: DOT PRODUCT % P
def dot_mod(constraints, witness, mod):
    r = []
    for constraint in constraints:
        sum = 0
        for idx, element in enumerate(constraint):
            sum += element * witness[idx]
        r.append(sum % mod)
    return r

# HELPER: ELEMENTWISE MUL % P
def elmul_mod(A, B, mod):
    out = []
    for a, b in zip(A, B):
        out.append((a * b) % mod)
    return out

# CHECK CONSTRAINTS
lhs = dot_mod(OUT, w, P)
rhs = elmul_mod(dot_mod(A, w, P), dot_mod(B, w, P), P)
print(lhs == rhs)
