from py_ecc.bn128 import multiply, G1, G2, pairing, add, eq, curve_order
import r1cs, witness

# CONSTRAINTS
OUT = r1cs.OUT
A = r1cs.A
B = r1cs.B

# WITNESSES
wG1 = [multiply(G1, i) for i in witness.w]
wG2 = [multiply(G2, i) for i in witness.w]
allG2 = [G2 for _ in witness.w]

# HELPER: DOT PRODUCT ON ELIPTIC CURVES
def dot_ec(constraints, witness, G):
    r = []
    for constraint in constraints:
        sum = None
        for idx, element in enumerate(constraint):
            if element < 0:
                sum = add(sum, multiply(witness[idx], curve_order + element))
            else:
                sum = add(sum, multiply(witness[idx], element))
        r.append(sum)
    return r

# HELPER: ELEMENTWISE MUL ON ELIPTIC CURVES
def elmul_ec(A, B):
    out = []
    for a, b in zip(A, B):
        out.append(pairing(b, a))
    return out

# CHECK CONSTRAINTS
lhs = elmul_ec(dot_ec(OUT, wG1, G1), allG2)
rhs = elmul_ec(dot_ec(A, wG1, G1), dot_ec(B, wG2, G2))
print(eq(lhs, rhs))
