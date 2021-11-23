import sympy as sym

l, r, m = sym.symbols('l, r, m')  # lambda, ro and mu

M = sym.Matrix.zeros(9, 9)

M[0, 3] = -1 / r
M[1, 4] = -1 / r
M[2, 5] = -1 / r
M[3, 0] = -(l + 2*m)
M[4, 1] = -m
M[5, 2] = -m
M[6, 0] = -l
M[8, 0] = -l

print(M.eigenvals())
