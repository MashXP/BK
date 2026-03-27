import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('Images', exist_ok=True)

# Figure 1: Drying Curve
t_A, t_B, t_C, t_D = 0, 1, 4, 8
tau = np.linspace(0, 8, 500)
U = np.zeros_like(tau)
theta = np.zeros_like(tau)

U_0, U_th, U_star = 0.8, 0.4, 0.05
theta_0, t_w, t_inf = 20, 40, 80

for i, t in enumerate(tau):
    if t <= t_B: # AB: Warming up
        U[i] = U_0 - (U_0 - 0.78) * (t/t_B)**2
        theta[i] = theta_0 + (t_w - theta_0) * (t/t_B)**0.5
    elif t <= t_C: # BC: Constant rate
        U[i] = 0.78 - (0.78 - U_th) * ((t - t_B)/(t_C - t_B))
        theta[i] = t_w
    else: # CD: Falling rate
        k = 0.6
        U[i] = U_star + (U_th - U_star) * np.exp(-k * (t - t_C))
        theta[i] = t_inf - (t_inf - t_w) * np.exp(-k * (t - t_C))

fig, ax1 = plt.subplots(figsize=(6, 4))
ax2 = ax1.twinx()

ax1.plot(tau, U, 'b-', label='1: Drying curve', linewidth=2)
ax2.plot(tau, theta, 'r--', label='2: Temperature', linewidth=2)

ax1.set_xlabel('Drying time, $\\tau$')
ax1.set_ylabel('Moisture content, $U$', color='b')
ax2.set_ylabel('Temperature, $\\theta$', color='r')
ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_yticks([])

# Annotations for A, B, C, D
ax1.axvline(t_B, ymin=0, ymax=1, color='k', linestyle=':', alpha=0.5)
ax1.axvline(t_C, ymin=0, ymax=1, color='k', linestyle=':', alpha=0.5)

# Place A, B, C, D at the top
y_top = ax1.get_ylim()[1]
ax1.text(t_A, y_top*0.95, 'A', ha='center', va='top', fontsize=12, fontweight='bold')
ax1.text(t_B, y_top*0.95, 'B', ha='center', va='top', fontsize=12, fontweight='bold')
ax1.text(t_C, y_top*0.95, 'C', ha='center', va='top', fontsize=12, fontweight='bold')
ax1.text(t_D, y_top*0.95, 'D', ha='center', va='top', fontsize=12, fontweight='bold')

fig.legend(loc="center right", bbox_to_anchor=(0.9, 0.5))
fig.tight_layout()
plt.savefig('Images/drying_curve.pdf')
plt.close()

# Figure 2: Drying Rate Curve
U_vals = np.linspace(0.01, U_0, 500)
N1 = np.zeros_like(U_vals)
N2 = np.zeros_like(U_vals)
N3 = np.zeros_like(U_vals)
N4 = np.zeros_like(U_vals)
N5 = np.zeros_like(U_vals)

Nc = 1.0
Uc1 = U_th
Uc2 = 0.2

for i, u in enumerate(U_vals):
    if u >= Uc1:
        n = Nc
        N1[i] = N2[i] = N3[i] = N4[i] = N5[i] = n
    else:
        x = u / Uc1
        N1[i] = Nc * x # 1: thin porous
        N2[i] = Nc * (x**0.5) # 2: colloidal
        N3[i] = Nc * (x**2) # 3: porous
        N4[i] = Nc * (3*x**2 - 2*x**3) # 4: porous-colloidal
        if u >= Uc2: # 5: second critical point
            N5[i] = Nc - (Nc - 0.4) * ((Uc1 - u)/(Uc1 - Uc2))
        else:
            N5[i] = 0.4 * (u / Uc2)

plt.figure(figsize=(6, 4))
plt.plot(U_vals, N1, 'k-', label='1: Thin/porous')
plt.plot(U_vals, N2, 'b--', label='2: Colloidal')
plt.plot(U_vals, N3, 'r-.', label='3: Porous')
plt.plot(U_vals, N4, 'g:', label='4: Porous-colloidal')
plt.plot(U_vals, N5, 'm-', alpha=0.6, label='5: Second critical pt')

plt.xlim(max(U_vals), 0) # Plot right to left
plt.xlabel('Moisture content, $U$')
plt.ylabel('Drying rate, $N$')
plt.xticks([])
plt.yticks([])
plt.legend()
plt.tight_layout()
plt.savefig('Images/drying_rate.pdf')
plt.close()
