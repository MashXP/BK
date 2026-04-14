import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from experiment_data import experiments, vle_x, vle_y
from procedural_calc import McCabeThiele

# Define paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(SCRIPT_DIR, '..', 'Figures')

# Create Figures directory if it doesn't exist
if not os.path.exists(FIGURES_DIR):
    os.makedirs(FIGURES_DIR)

def plot_mccabe_thiele(exp, mt):
    plt.figure(figsize=(8, 8))
    
    # Coordinates
    x_vals = np.linspace(0, 1, 100)
    y_eq = mt.get_y_eq(x_vals)
    
    # 1. Equilibrium Line
    plt.plot(x_vals, y_eq, 'b-', label='Equilibrium Curve', linewidth=2)
    
    # 2. Diagonal Line
    plt.plot([0, 1], [0, 1], 'k--', alpha=0.5)
    
    # 3. Operating Lines
    xf, xd, xw, R, q = exp['xf'], exp['xd'], exp['xw'], exp['R'], exp['q']
    
    # Rectification line
    x_rect = np.linspace(xf, xd, 10)
    y_rect = mt.rect_line(x_rect, R, xd)
    plt.plot(x_rect, y_rect, 'r-', label='Rectification Line')
    
    # Stripping line (from intersection to xw)
    if abs(q - 1) < 1e-3:
        x_int = xf
    else:
        m1 = R / (R + 1)
        c1 = xd / (R + 1)
        m2 = q / (q - 1)
        c2 = -xf / (q - 1)
        x_int = (c2 - c1) / (m1 - m2)
    
    y_int = mt.rect_line(x_int, R, xd)
    plt.plot([xw, x_int], [xw, y_int], 'g-', label='Stripping Line')
    
    # q-line
    plt.plot([xf, x_int], [xf, y_int], 'm-.', label='q-line')
    
    # 4. Stages (Staircase)
    stages = mt.calculate_stages(xf, xd, xw, R, q)
    num_stages = (len(stages) - 1) // 2
    
    st_x = [p[0] for p in stages]
    st_y = [p[1] for p in stages]
    plt.step(st_x, st_y, where='pre', color='orange', label=f'Stages: {num_stages}', linewidth=1.5)
    
    # Formatting
    plt.title(f"McCabe-Thiele Diagram - Experiment {exp['id']}\n(Reflux R={R}, Feed Loc={exp['location']})")
    plt.xlabel("Mole fraction of liquid (x)")
    plt.ylabel("Mole fraction of vapor (y)")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(FIGURES_DIR, f"plot_{exp['id']}.png")
    plt.savefig(save_path)
    plt.close()
    return num_stages

# Initialize Engine
mt_engine = McCabeThiele(vle_x, vle_y)

# Generate Plots
print("Starting stage calculations and plot generation...")
results_summary = []
for exp in experiments:
    n = plot_mccabe_thiele(exp, mt_engine)
    results_summary.append(f"Exp {exp['id']}: {n} theoretical stages")

for res in results_summary:
    print(res)

print("\nAll plots generated in DISTILLATION/Figures/")
