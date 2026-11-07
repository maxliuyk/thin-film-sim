from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from thin_film import film_rt

out = Path("results")
out.mkdir(exist_ok=True)

lam = np.linspace(400e-9, 1000e-9, 1000)
R, T = film_rt(lam, 300e-9)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(lam * 1e9, R, label="Reflectance R")
ax.plot(lam * 1e9, T, label="Transmittance T")
ax.set_xlabel("Vacuum wavelength (nm)")
ax.set_ylabel("Fraction of incident power")
ax.set_ylim(-0.02, 1.02)
ax.set_title("Single film: n0 = 1.0, n1 = 1.5, n2 = 1.0, d = 300 nm")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(out / "spectrum_d300nm.png", dpi=150)
print("Saved", out / "spectrum_d300nm.png")