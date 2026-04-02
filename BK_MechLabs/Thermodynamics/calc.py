import os
import math
import matplotlib.pyplot as plt

# ─── Experimental data (Average values) ────────────────────────────────────────
# T = dry bulb, Tw = wet bulb, V_cond = condensed water at cooler (ml/min)
# Points: 1=env (before cooler), 2=after cooler, 3=before nozzle (after dryer), 4=after nozzle

data_saturated = [
    {"v": 3.36, "T1": 31, "Tw1": 24, "T2": 19.5, "Tw2": 17.5, "T3": 35, "Tw3": 25.5, "T4": 34.5, "Tw4": 33.5, "V_cond": 7.25},
    {"v": 1.58, "T1": 31, "Tw1": 24, "T2": 17,   "Tw2": 15,   "T3": 35.5,"Tw3": 25,  "T4": 36.5, "Tw4": 34.5, "V_cond": 7.75},
    {"v": 1.23, "T1": 31, "Tw1": 24, "T2": 15,   "Tw2": 12,   "T3": 37,  "Tw3": 25,  "T4": 37,   "Tw4": 34,   "V_cond": 8.5},
]

data_superheated = [
    {"v": 3.36, "T1": 31, "Tw1": 24, "T2": 16.5, "Tw2": 17.5, "T3": 34,  "Tw3": 24.5,"T4": 34.5, "Tw4": 36.5, "V_cond": 11.25},
    {"v": 1.58, "T1": 31, "Tw1": 24, "T2": 15.5, "Tw2": 15.5, "T3": 34,  "Tw3": 24,  "T4": 34.5, "Tw4": 30.5, "V_cond": 11.0},
    {"v": 1.23, "T1": 31, "Tw1": 24, "T2": 13,   "Tw2": 14.5, "T3": 35,  "Tw3": 25,  "T4": 35.5, "Tw4": 36.5, "V_cond": 11.75},
]

# ─── Constants ──────────────────────────────────────────────────────────────────
F = 0.0144   # outlet area of aerodynamic tube, m²
B = 1.013    # atmospheric pressure, bar
A = 66e-5    # psychrometer factor for v < 0.5 m/s (wet bulb measurement is static)

# ─── Air density lookup table ───────────────────────────────────────────────────
# t from 30°C to 49°C (from source Table 5)
rho_table = {
    30: 1.165, 31: 1.161, 32: 1.157, 33: 1.154, 34: 1.150,
    35: 1.146, 36: 1.142, 37: 1.139, 38: 1.135, 39: 1.131,
    40: 1.128, 41: 1.124, 42: 1.121, 43: 1.117, 44: 1.114,
    45: 1.110, 46: 1.107, 47: 1.103, 48: 1.100, 49: 1.096,
    50: 1.093, 51: 1.089, 52: 1.086, 53: 1.083, 54: 1.079,
}

def get_rho(t):
    t_int = round(t)
    if t_int in rho_table:
        return rho_table[t_int]
    # simple linear fallback
    t_lo = max(k for k in rho_table if k <= t_int)
    t_hi = min(k for k in rho_table if k >= t_int)
    if t_lo == t_hi:
        return rho_table[t_lo]
    return rho_table[t_lo] + (rho_table[t_hi] - rho_table[t_lo]) * (t - t_lo) / (t_hi - t_lo)

def sat_pressure(t):
    """Saturation pressure in bar using Antoine approximation."""
    return 610.78 * math.exp((17.27 * t) / (t + 237.3)) / 100000.0

def psychro(tdry, twet):
    """Return phi (%), d (kg/kg), I (kJ/kg) for given dry and wet bulb temps."""
    if twet > tdry:
        twet = tdry
    Phs_wet = sat_pressure(twet)
    Phs_dry = sat_pressure(tdry)
    Pa = Phs_wet - A * B * (tdry - twet)
    Pa = max(0, min(Pa, Phs_dry))
    phi = Pa / Phs_dry * 100
    denom = B - Pa
    d = (18.0 / 29.0) * Pa / denom if denom > 0 else 0
    I = tdry + (2493 + 1.97 * tdry) * d
    return phi, d, I

# ─── Psychrometric results per dataset ─────────────────────────────────────────
def process_data(data, mode_name, prefix):
    os.makedirs("Plots", exist_ok=True)
    results = []
    for row in data:
        v = row["v"]
        points = []
        for p in range(1, 5):
            tdry = row[f"T{p}"]
            twet = row[f"Tw{p}"]
            phi, d, I = psychro(tdry, twet)
            points.append({"T": tdry, "Tw": twet, "phi": phi, "d": d, "I": I})
        results.append({"v": v, "points": points, "V_cond": row["V_cond"]})

        # Plot
        T_arr = [p["T"] for p in points]
        d_arr = [p["d"] for p in points]
        plt.figure(figsize=(8, 6))
        plt.plot(d_arr, T_arr, marker='o', linestyle='-', color='b')
        for i, (dx, ty) in enumerate(zip(d_arr, T_arr)):
            plt.text(dx, ty, f' P{i+1}', fontsize=12)
        plt.title(f"Airflow changes at v = {v} m/s ({mode_name})")
        plt.xlabel("Absolute Humidity d (kg/kg)")
        plt.ylabel("Dry Bulb Temperature (°C)")
        plt.grid(True)
        fname = f"{prefix}_v_{str(v).replace('.', '_')}.png"
        plt.savefig(os.path.join("Plots", fname))
        plt.close()
    return results

sat_res  = process_data(data_saturated,   "Saturated Steam",   "sat")
sup_res  = process_data(data_superheated, "Superheated Steam", "sup")

# ─── Heat balance calculation ───────────────────────────────────────────────────
def heat_balance(results):
    rows = []
    for r in results:
        v     = r["v"]
        pts   = r["points"]
        Vcond = r["V_cond"]  # ml/min

        t1, t3 = pts[0]["T"], pts[2]["T"]
        I1, I2, I3 = pts[0]["I"], pts[1]["I"], pts[2]["I"]
        d1, d2      = pts[0]["d"], pts[1]["d"]

        rho1 = get_rho(t1)
        rho3 = get_rho(t3)

        Gkk  = v * F * rho1                         # kg/s
        Q0   = Gkk * (I1 - I2)                      # kW
        Gw   = 3600 * Gkk * (d1 - d2)               # kg/h theory
        Gpw  = 0.06 * Vcond                          # kg/h practice (t1=1 min)
        Gpkk = v * F * rho3                          # kg/s
        Q    = Gpkk * (I3 - I2)                      # kW

        rows.append({
            "v": v, "t1": t1, "rho1": rho1, "Gkk": Gkk,
            "Q0": Q0, "Gw": Gw, "Gpw": Gpw,
            "t3": t3, "rho3": rho3, "Gpkk": Gpkk, "Q": Q,
        })
    return rows

sat_hb = heat_balance(sat_res)
sup_hb = heat_balance(sup_res)

# ─── Write thermo_calc_results.tex ─────────────────────────────────────────────
def fmt_table(results, label):
    s  = f"\\subsubsection{{{label}}}\n"
    s += "\\begin{table}[H]\n\\centering\n"
    s += "\\begin{tabular}{|c|c|c|c|c|c|c|}\\hline\n"
    s += ("\\textbf{v (m/s)} & \\textbf{Point} & \\textbf{T ($^\\circ$C)} & "
          "\\textbf{Tw ($^\\circ$C)} & \\textbf{$\\phi$ (\\%)} & "
          "\\textbf{d (kg/kg)} & \\textbf{I (kJ/kg)} \\\\\\hline\n")
    for r in results:
        for i, p in enumerate(r["points"]):
            v_col = str(r["v"]) if i == 0 else ""
            end   = "\\hline" if i == 3 else "\\cline{2-7}"
            s += (f"{v_col} & {i+1} & {p['T']:.1f} & {p['Tw']:.1f} & "
                  f"{p['phi']:.1f} & {p['d']:.4f} & {p['I']:.2f} \\\\{end}\n")
    s += "\\end{tabular}\n"
    s += f"\\caption{{Calculated parameters -- {label}}}\n"
    s += "\\end{table}\n\n"
    return s

with open("thermo_calc_results.tex", "w") as f:
    f.write("\\subsection{Calculated Parameters}\n")
    f.write(fmt_table(sat_res,  "Saturated Steam"))
    f.write(fmt_table(sup_res,  "Superheated Steam"))

# ─── Write thermo_heat_balance.tex ─────────────────────────────────────────────
note = r"""
\begin{description}
    \item[$v$:] velocity at aerodynamic tube outlet, m/s
    \item[$t_{dry,1}$:] dry-bulb temperature at entrance (Point 1), $^\circ$C
    \item[$t_{dry,3}$:] dry-bulb temperature at dryer entrance (Point 3), $^\circ$C
    \item[$\rho_1, \rho_3$:] specific mass of air before cooler / before dryer, kg/m$^3$
    \item[$G_{kk}$:] mass flowrate into aerodynamic tube, kg/s
    \item[$G'_{kk}$:] mass flowrate before dryer, kg/s
    \item[$Q_0$:] cooling capacity of cooler, kW
    \item[$G_{water}$:] theoretical condensed water flowrate, kg/h
    \item[$G'_{water}$:] practical condensed water flowrate, kg/h
    \item[$Q$:] thermal load of air dryer, kW
\end{description}
"""

def fmt_hb_table(rows, label):
    s  = "\\begin{table}[H]\n\\centering\n"
    s += f"\\caption{{Table 4. Heat balance -- {label}}}\n"
    s += "\\resizebox{\\textwidth}{!}{\n"
    s += "\\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|}\\hline\n"
    s += ("\\textbf{v} & \\textbf{$t_{1}$ ($^\\circ$C)} & \\textbf{$\\rho_1$} & "
          "\\textbf{$G_{kk}$ (kg/s)} & \\textbf{$Q_0$ (kW)} & "
          "\\textbf{$G_{water}$ (kg/h)} & \\textbf{$G'_{water}$ (kg/h)} & "
          "\\textbf{$t_{3}$ ($^\\circ$C)} & \\textbf{$\\rho_3$} & "
          "\\textbf{$G'_{kk}$ (kg/s)} & \\textbf{$Q$ (kW)} \\\\\\hline\n")
    for r in rows:
        s += (f"{r['v']} & {r['t1']:.2f} & {r['rho1']:.4f} & {r['Gkk']:.4f} & "
              f"{r['Q0']:.4f} & {r['Gw']:.4f} & {r['Gpw']:.4f} & "
              f"{r['t3']:.2f} & {r['rho3']:.4f} & {r['Gpkk']:.4f} & "
              f"{r['Q']:.4f} \\\\\\hline\n")
    s += "\\end{tabular}\n}\n\\end{table}\n\n"
    return s

with open("thermo_heat_balance.tex", "w") as f:
    f.write("\\subsection{Heat Balance Calculation Results}\n")
    f.write(fmt_hb_table(sat_hb,  "Saturated Steam"))
    f.write(fmt_hb_table(sup_hb,  "Superheated Steam"))
    f.write(note)

print("Done: thermo_calc_results.tex and thermo_heat_balance.tex generated.")
