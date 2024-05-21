# Homerolled ZK Circuit

Simple example to build up to an (almost) ZK circuit in Python, based on the lessons from the [Rareskills ZK Book](https://www.rareskills.io/zk-book).

## Goal

All three examples in this repo aim to accomplish the same goal:

**Prove that we know an `x` and `z` to solve for `x^3 + 4x^2 - xz + 4 = 529`**

The examples work up in complexity from R1CS on normal arithmetic through using modular arithmetic and finally to a circuit on elliptic curves.

## R1CS

Code: [r1cs.py](./r1cs.py)

This formula can be broken down into three constraints:

1) `x_squared = x * x`
2) `x_cubed = x * x_squared`
3) `result - x_cubed - 4 * x_squared - 4 = -xz`

R1CS encodes these constraints as matrices in a way that can initially feel a bit confusing:

- `OUT` encodes the result (left side of equality) of each of the constraints.
- `A` encodes the left side of the multiplication in each of the constraints.
- `B` encodes the right side of the multiplication in each of the constraints.

While this can feel a bit unintuitive, this arrangement allows us to use matrix multiplication to effectively "pluck" the correct values out of the witness for each part of each constraint.

These matrices are implemented in `r1cs.py` and imported into each example.

## Witness

Code: [witness.py](./witness.py)

In order to prove that we know the solution to this problem, we must have the solution to this problem.

```
y = 529
x = 7
z = 2
```

Further, we have to calculate the intermediate values so that each element in the constraints (`x_squared`, `x_cubed`) is solved for.

These are implemented in `witness.py` and imported into each example.

## Traditional Arithmetic

Code: [arith.py](./arith.py)

This is the simplest possible example. We import the constraints and the witness (`w`) and prove that the dot product of `OUT ⋅ w` is equal to elementwise multiplication of `A ⋅ w` and `B⋅ w`.

This makes intuitive sense:
- We use the dot product to pluck out the right witness values to calculate the result (OUT) for each constraint.
- We do the same for A (left side of multiplication) and B (right side of multiplication).
- Then we multiply the results of A and B together.
- For each constraint, A * B should equal OUT.

This works! But it isn't at all zero knowledge, because we're just passing the values to test.

## Modular Arithmetic

Code: [mod.py](./mod.py)

This version uses modular arithmetic, with `P = 97` to keep the value low enough to reason about.

We use the exact same R1CS constraints and same witness, but have to take each element (including the solution) mod 97.

Unfortunately, numpy doesn't support modular arithmetic, so this example includes two helper functions to perform the dot product or elementwise multiplication with the modulus applied.

This also works! But it also isn't ZK, because we're just passing the values to test.

## Elliptic Curves

Code: [ec.py](./ec.py)

To make this zero knowledge (or at least close to it, since someone could still test a guessed value for correctness), we can use elliptic curves.

Again, we use the same R1CS constraints (and the original solution, since the field modulus of our curve is much larger than 529).

We can't multiply elliptic curve points directly, which kind of breaks the whole `OUT = A * B` thing. But we can take bilinear pairings using elliptic curve points with field extensions.

Instead of just creating one witness, we create two. Each uses the same witness values, but one is multiplied by the point G1 and the other is multiplied by G2. We take the dot product of these witnesses with the constraints, as in the previous examples.

When we "multiply" A and B, we take the bilinear pairing of the two points, which lands us in the G12 group. We can then compare this to the bilinear pairing of dot product of the G1 witness with OUT, paired with a vector of all G2 points. The result is like multiplying by 1, but lands us again in the G12 group.

We finally can compare these two G12 points to see if they are equal.

## References

All good ideas come from the [Rareskills ZK Book](https://www.rareskills.io/zk-book). All bad ideas are my own.
