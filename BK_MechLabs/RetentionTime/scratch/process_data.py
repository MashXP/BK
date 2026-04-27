import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# General Parameters
flow_rate = 0.4  # L/min
tank_diameter = 14  # cm
tank_height = 12  # cm
d0_total = 0.03

# Calculate tank volume in L (1 cm3 = 0.001 L)
# V = pi * r^2 * h
# d = 14 cm -> r = 7 cm
v_tank_single = (np.pi * (tank_diameter / 2)**2 * tank_height) / 1000.0
print(f"Tank Volume (Single): {v_tank_single:.4f} L")

# Data
data_1 = {
    't': np.arange(1, 16),
    'D': [0.031, 0.035, 0.030, 0.033, 0.026, 0.002, 0.018, 0.025, 0.004, 0.018, 0.026, 0.004, 0.015, 0.015, 0.002]
}

data_2 = {
    't': np.arange(1, 26),
    'D': [0.006, 0.007, 0.007, 0.013, 0.008, 0.011, 0.005, 0.013, 0.007, 0.006, 0.003, 0.006, 0.001,
          0.006, 0.004, 0.002, 0.006, 0.006, 0.008, 0.006, 0.004, 0.004, 0.006, 0.012, 0.010]
}

data_3 = {
    't': np.arange(1, 36),
    'D': [0.004, 0.007, 0.008, 0.003, 0.008, 0.010, 0.007, 0.008, 0.013, 0.010, 0.009, 0.009,
          0.005, 0.007, 0.009, 0.005, 0.007, 0.007, 0.003, 0.010, 0.011, 0.007, 0.005, 0.005,
          0.006, 0.004, 0.007, 0.004, 0.005, 0.011, 0.004, 0.018, 0.008, 0.002, 0.009]
}

def process_system(t, D, N, d0):
    t = np.array(t)
    D = np.array(D)
    
    # 1. Experiment Calculations
    sum_D = np.sum(D)
    sum_tD = np.sum(t * D)
    t_tb = sum_tD / sum_D
    
    theta_exp = t / t_tb
    E_exp = D / d0
    
    # 2. Theory Calculations
    v_total = N * v_tank_single
    tau = v_total / flow_rate
    
    theta_theo = t / tau
    
    if N == 1:
        E_theo = np.exp(-theta_theo)
    else:
        # E_theta = (N * (N*theta)^(N-1) / (N-1)!) * exp(-N*theta)
        from math import factorial
        E_theo = (N * (N * theta_theo)**(N-1) / factorial(N-1)) * np.exp(-N * theta_theo)
        
    return {
        't': t, 'D': D, 'tD': t*D,
        'theta_exp': theta_exp, 'E_exp': E_exp,
        'theta_theo': theta_theo, 'E_theo': E_theo,
        't_tb': t_tb, 'tau': tau, 'v_total': v_total / 1000.0, # m3
        'sum_D': sum_D, 'sum_tD': sum_tD
    }

res1 = process_system(data_1['t'], data_1['D'], 1, 0.03)
res2 = process_system(data_2['t'], data_2['D'], 2, 0.015)
res3 = process_system(data_3['t'], data_3['D'], 3, 0.01)

# Plotting function
def plot_system(res, N, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(res['theta_exp'], res['E_exp'], 'o-', label='Empirical', color='blue', markersize=4)
    
    # Smooth theory curve
    theta_smooth = np.linspace(0, max(res['theta_theo'].max(), res['theta_exp'].max()), 100)
    if N == 1:
        E_smooth = np.exp(-theta_smooth)
    else:
        from math import factorial
        E_smooth = (N * (N * theta_smooth)**(N-1) / factorial(N-1)) * np.exp(-N * theta_smooth)
        
    plt.plot(theta_smooth, E_smooth, '--', label='Theoretical', color='red')
    
    plt.title(f'Residence Time Distribution - {N} Tank(s) System')
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$E(\theta)$')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Ensure Images directory exists
    os.makedirs('Images', exist_ok=True)
    plt.savefig(f'Images/{filename}')
    plt.close()

plot_system(res1, 1, '1-tank.png')
plot_system(res2, 2, '2-tank.png')
plot_system(res3, 3, '3-tank.png')

# Output LaTeX snippets for Tables
def print_latex_table(res, N):
    print(f"\n% --- {N} Tank System ---")
    for i in range(len(res['t'])):
        print(f"{res['t'][i]} & {res['D'][i]:.3f} & {res['tD'][i]:.3f} & {res['theta_exp'][i]:.2f} & {res['E_exp'][i]:.2f} & {res['theta_theo'][i]:.2f} & {res['E_theo'][i]:.2f} \\\\")
    print(f"\\hline")
    print(f"\\textbf{{Total}} & \\textbf{{{res['sum_D']:.3f}}} & \\textbf{{{res['sum_tD']:.3f}}} & & & & \\\\")

print_latex_table(res1, 1)
print_latex_table(res2, 2)
print_latex_table(res3, 3)

# Print values
print("\n% Values")
for i, r in enumerate([res1, res2, res3], 1):
    print(f"% System {i}")
    print(f"t_tb = {r['t_tb']:.2f}")
    print(f"v_total = {r['v_total']:.4f}")
    print(f"tau = {r['tau']:.2f}")
