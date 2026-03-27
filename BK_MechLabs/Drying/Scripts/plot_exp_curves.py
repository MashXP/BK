import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('Images', exist_ok=True)

tau_50 = [0, 5, 10, 15, 20, 25, 30]
U_50 = [4.00, 4.00, 4.00, 4.00, 0.00, 0.00, 0.00]

tau_60 = [0, 3, 6, 9, 12, 15]
U_60 = [7.69, 3.85, 3.85, 0.00, 0.00, 0.00]

tau_70 = [0, 2, 4, 6, 8, 10, 12]
U_70 = [4.00, 4.00, 4.00, 0.00, 0.00, 0.00, 0.00]

def plot_curve(tau, U, temp, filename):
    plt.figure(figsize=(4, 3))
    plt.plot(tau, U, 'o-', color='#1f77b4', linewidth=2, markersize=6)
    plt.title(f'Drying Curve at {temp}$^\\circ$C')
    plt.xlabel('Drying Time $\\tau$ (min)')
    plt.ylabel('Moisture Content $U$ (%)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.ylim(-0.5, max(U) + 1.5)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

plot_curve(tau_50, U_50, 50, 'Images/exp_curve_50.pdf')
plot_curve(tau_60, U_60, 60, 'Images/exp_curve_60.pdf')
plot_curve(tau_70, U_70, 70, 'Images/exp_curve_70.pdf')
