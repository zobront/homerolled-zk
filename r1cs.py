# CONSTRAINTS
# 1) `x_squared = x * x`
# 2) `x_cubed = x * x_squared`
# 3) `result - x_cubed - 4 * x_squared - 4 = -xz`

# OUT gives us the output (left side of equality) of each constraint
OUT = [
    [0, 0, 1, 0, 0, 0], # LHS of 1) x^2
    [0, 0, 0, 1, 0, 0], # LHS of 2) x^3
    [-4, 0, -4, -1, 0, 1] # LHS of 3) y - x^3 - 4x^2 - 4
]

# A gives us the left argument (right side of equality) of each constraint
A = [
    [0, 1, 0, 0, 0, 0], # LHARG of 1) x
    [0, 0, 1, 0, 0, 0], # LHARG of 2) x^2
    [0, -1, 0, 0, 0, 0] # LHARG of 3) -x
]

# B give us the right argument (right side of equality) of each constraint
B = [
    [0, 1, 0, 0, 0, 0], # RHARG of 1) x
    [0, 1, 0, 0, 0, 0], # RHARG of 2) x
    [0, 0, 0, 0, 1, 0] # RHARG of 3) z
]
