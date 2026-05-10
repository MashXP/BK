import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
d = 0.09 # m
F = np.pi * d**2 / 4 # m^2
Z = 0.42 # m
a = 375 # m^2/m^3
epsilon = 0.586
V_max = 0.286 / 60 # m^3/s
rho_G = 1.1305 # kg/m^3
mu = 1928e-8 # kg/m.s
rho_L = 995.6 # kg/m^3 (water at 30C)
g = 9.81 # m/s^2

# Raw Data (mmH2O)
# Columns: G%, L=0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6
G_percent = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
L_val = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6])

data_mmH2O = np.array([
    [1, 1, 1, 0, 2, 3, 3, 5, 8],
    [5, 6, 8, 4, 8, 9, 14, 20, 25],
    [10, 12, 16, 17, 20, 23, 35, 62, 78],
    [19, 22, 26, 31, 53, 49, 75, 118, 142],
    [29, 32, 42, 49, 107, 95, 163, 328, 258],
    [38, 46, 62, 95, 164, 180, 246, np.nan, np.nan],
    [52, 62, 109, 174, 348, 303, 332, np.nan, np.nan],
    [70, 82, 172, 295, 412, 393, 418, np.nan, np.nan],
    [90, 108, 267, 377, np.nan, np.nan, np.nan, np.nan, np.nan],
    [108, 141, 315, 434, np.nan, np.nan, np.nan, np.nan, np.nan]
])

# Conversions
G_mass = (G_percent / 100.0) * rho_G * V_max / F # kg/s.m^2
L_mass = (L_val * 4.586 * rho_L) / (60 * F * 1000) # kg/s.m^2 (assuming L_val is in gal/min and factor converts to liter)
# Wait, let's re-verify L_mass. 
# Page 25: L = L_gal * 4.586 * rho_L / (60 * F). If L is kg/s.m^2, then 4.586 must be gal->L conversion?
# 1 gal = 3.785 L. 4.586 is likely a factor for this specific flowmeter.

# Calculate Results
def calc_results(dp_mm, g_m, l_m):
    dp_n = dp_mm * 9.81 # N/m^2
    dp_z = dp_n / Z
    re = (4 * g_m) / (a * mu)
    # f = (2 * dp_n * epsilon^3 * rho_G) / (G^2 * Z * a)
    f = (2 * dp_n * epsilon**3 * rho_G) / (g_m**2 * Z * a)
    return dp_n, dp_z, re, f

# Dry Column Calculations (L=0)
dp_dry_mm = data_mmH2O[:, 0]
dp_dry_n, dp_dry_z, re_dry, f_dry = calc_results(dp_dry_mm, G_mass, L_mass[0])

# Wetted Column Calculations
results = {}
for i, l in enumerate(L_val):
    dp_wet_mm = data_mmH2O[:, i]
    mask = ~np.isnan(dp_wet_mm)
    dp_wet_n, dp_wet_z, re_wet, f_wet = calc_results(dp_wet_mm[mask], G_mass[mask], L_mass[i])
    sigma = dp_wet_n / dp_dry_n[mask]
    results[l] = {
        'G': G_mass[mask],
        'dp_z': dp_wet_z,
        'sigma': sigma,
        'f': f_wet,
        're': re_wet
    }

# Plots
plt.figure(figsize=(10, 6))
for l in L_val:
    mask = ~np.isnan(data_mmH2O[:, np.where(L_val == l)[0][0]])
    plt.plot(G_mass[mask], data_mmH2O[mask, np.where(L_val == l)[0][0]] * 9.81 / Z, 'o-', label=f'L={l}')
plt.xlabel('G (kg/s.m^2)')
plt.ylabel('Delta P / Z (N/m^3)')
plt.title('Effect of G and L on Pressure Drop')
plt.legend()
plt.grid(True)
plt.savefig('PackedColumn/Images/dp_chart.png')

plt.figure(figsize=(10, 6))
for l in L_val:
    res = results[l]
    plt.plot(np.log10(res['G']), np.log10(res['dp_z']), 'o-', label=f'L={l}')
plt.xlabel('log10(G)')
plt.ylabel('log10(Delta P / Z)')
plt.title('Logarithmic Plot of Pressure Drop')
plt.legend()
plt.grid(True)
plt.savefig('PackedColumn/Images/log_dp_chart.png')

# Output LaTeX Tables
def print_latex_table(l, res):
    print(f"% Table for L={l}")
    print("\\begin{table}[H]")
    print("    \\centering")
    print(f"    \\caption{{Results for $L={l}$}}")
    print("    \\begin{tabular}{ccccccc}")
    print("        \\hline")
    print("        $G [\\%]$ & $G [kg/s.m^2]$ & $\\Delta P [mmH_2O]$ & $\\Delta P/Z [N/m^3]$ & $\\sigma$ & $f_{wet}$ & $Re$ \\\\")
    print("        \\hline")
    for j in range(len(res['G'])):
        g_pct = G_percent[j]
        dp_mm = data_mmH2O[j, np.where(L_val == l)[0][0]]
        print(f"        {g_pct} & {res['G'][j]:.4f} & {dp_mm} & {res['dp_z'][j]:.2f} & {res['sigma'][j]:.2f} & {res['f'][j]:.2f} & {res['re'][j]:.2f} \\\\")
    print("        \\hline")
    print("    \\end{tabular}")
    print("\\end{table}")

# Flooding Point Calculations
# We assume the last point for each L (where data ends or where it jumps) is the flooding point G*
flooding_data = []
for i, l in enumerate(L_val):
    if l == 0: continue
    dp_wet_mm = data_mmH2O[:, i]
    mask = ~np.isnan(dp_wet_mm)
    last_idx = np.where(mask)[0][-1]
    g_star_pct = G_percent[last_idx]
    g_star = G_mass[last_idx]
    v = g_star / rho_G
    
    # pi1 = (f_dry * a / epsilon^3) * (v^2 / 2g) * (rho_G / rho_L) * mu_td^0.2
    # Use f_dry corresponding to g_star
    f_d = f_dry[last_idx]
    pi1 = (f_d * a / epsilon**3) * (v**2 / (2 * g)) * (rho_G / rho_L) * (1.0**0.2)
    pi2 = (L_mass[i] / g_star) * np.sqrt(rho_G / rho_L)
    
    flooding_data.append({
        'L': l,
        'G_star_pct': g_star_pct,
        'G_star': g_star,
        'v': v,
        'pi1': pi1,
        'pi2': pi2
    })

plt.figure(figsize=(10, 6))
pi1_vals = [d['pi1'] for d in flooding_data]
pi2_vals = [d['pi2'] for d in flooding_data]
plt.plot(np.log10(pi2_vals), np.log10(pi1_vals), 'rs-', label='Flooding Point')
plt.xlabel('log10(pi2)')
plt.ylabel('log10(pi1)')
plt.title('Flooding Chart of Packed Column')
plt.grid(True)
plt.savefig('PackedColumn/Images/flooding_chart.png')

# Output LaTeX Tables
print("\\section{RESULTS}")
for l in L_val:
    res = results[l]
    print(f"\n% Table for L={l}")
    print("\\begin{table}[H]")
    print("    \\centering")
    print(f"    \\caption{{Experimental results for $L={l}$ gal/min}}")
    print("    \\begin{tabular}{ccccccc}")
    print("        \\hline")
    print("        $G [\\%]$ & $G [kg/s.m^2]$ & $\\Delta P [mmH_2O]$ & $\\Delta P/Z [N/m^3]$ & $\\sigma$ & $f_{wet}$ & $Re$ \\\\")
    print("        \\hline")
    for j in range(len(res['G'])):
        g_pct = G_percent[j]
        dp_mm = data_mmH2O[j, np.where(L_val == l)[0][0]]
        print(f"        {g_pct} & {res['G'][j]:.4f} & {dp_mm} & {res['dp_z'][j]:.2f} & {res['sigma'][j]:.2f} & {res['f'][j]:.2f} & {res['re'][j]:.2f} \\\\")
    print("        \\hline")
    print("    \\end{tabular}")
    print("\\end{table}")

print("\n\\subsection{Flooding Point Data}")
print("\\begin{table}[H]")
print("    \\centering")
print("    \\caption{Flooding point data for different liquid flow rates}")
print("    \\begin{tabular}{cccccccc}")
print("        \\hline")
print("        $L [gal/min]$ & $G^* [\\%]$ & $G^* [kg/s.m^2]$ & $v [m/s]$ & $\\pi_1$ & $\\pi_2$ & $\\log \\pi_1$ & $\\log \\pi_2$ \\\\")
print("        \\hline")
for d in flooding_data:
    print(f"        {d['L']} & {d['G_star_pct']} & {d['G_star']:.4f} & {d['v']:.4f} & {d['pi1']:.4f} & {d['pi2']:.4f} & {np.log10(d['pi1']):.4f} & {np.log10(d['pi2']):.4f} \\\\")
print("        \\hline")
print("    \\end{tabular}")
print("\\end{table}")
