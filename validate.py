import numpy as np
from numpy.testing import assert_allclose
from thin_film import film_rt

ATOL = 1e-10
lam = np.linspace(400e-9, 1000e-9, 1000)


R, T = film_rt([600e-9, 900e-9], 300e-9)
assert_allclose(R, [0.147929, 0], atol=1e-6)
assert_allclose(T, [0.852071, 1], atol=1e-6)
print("PASS reference values at 600 and 900 nm")

R, T = film_rt(lam, 300e-9)
worst = np.max(np.abs(R + T - 1))
assert worst < ATOL
print("PASS energy conservation, worst error =", worst)

R, T = film_rt(lam, 300e-9, n0=1.5, n1=1.5, n2=1.5)
assert_allclose(R, 0, atol=ATOL)
assert_allclose(T, 1, atol=ATOL)
print("PASS identical media: R = 0, T = 1")

R, T = film_rt(lam, 0)
assert_allclose(R, 0, atol=ATOL)
assert_allclose(T, 1, atol=ATOL)
print("PASS zero thickness: film disappears")

print("All checks passed.")