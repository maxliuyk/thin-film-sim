import numpy as np


def interface_coeffs(ni, nj):
    r = (ni - nj) / (ni + nj)
    t = 2 * ni / (ni + nj)
    return r, t


print("air -> glass:", interface_coeffs(1.0, 1.5))
print("glass -> air:", interface_coeffs(1.5, 1.0))