import numpy as np


def interface_coeffs(ni, nj):
    r = (ni - nj) / (ni + nj)
    t = 2 * ni / (ni + nj)
    return r, t

def film_amplitudes(wavelength, thickness, n0=1.0, n1=1.5, n2=1.0):

    lam = np.asarray(wavelength, dtype=float)

    r01, t01 = interface_coeffs(n0, n1)   
    r12, t12 = interface_coeffs(n1, n2) 

    delta = 2 * np.pi * n1 * thickness / lam
    z = np.exp(2j * delta) 
    den = 1 + r01 * r12 * z 

    r = (r01 + r12 * z) / den
    t = t01 * t12 * np.exp(1j * delta) / den
    return r, t

def film_rt(wavelength, thickness, n0=1.0, n1=1.5, n2=1.0):
    r, t = film_amplitudes(wavelength, thickness, n0, n1, n2)
    R = np.abs(r) ** 2
    T = (n2 / n0) * np.abs(t) ** 2
    return R, T
