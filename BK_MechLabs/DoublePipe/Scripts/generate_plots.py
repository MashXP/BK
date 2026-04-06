import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

# Add script directory to path to import procedural_calc
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from procedural_calc import rb, rc

# Create Figures directory if it doesn't exist
if not os.path.exists('Figures'):
    os.makedirs('Figures')

def plot_fig(data, mode, fixed_val, tube_label, fig_id):
    """
    mode 'G1': Plot vs Re2 for a fixed G1
    mode 'G2': Plot vs Re1 for a fixed G2
    """
    plt.figure(figsize=(8, 6))
    
    if mode == 'G1':
        subset = [r for r in data if r['gh'] == fixed_val]
        # Sort by GC to ensure Re2 is monotonic
        subset.sort(key=lambda x: x['gc'])
        x = [r['re2'] for r in subset]
        title = f"{tube_label}: Dependence on $Re_2$ at $G_1 = {fixed_val}$ L/min"
        xlabel = "$Re_2$"
    else:
        subset = [r for r in data if r['gc'] == fixed_val]
        subset.sort(key=lambda x: x['gh'])
        x = [r['re1'] for r in subset]
        title = f"{tube_label}: Dependence on $Re_1$ at $G_2 = {fixed_val}$ L/min"
        xlabel = "$Re_1$"

    y_star = [r['ks'] for r in subset]
    y_exp = [r['ke'] for r in subset]
    
    plt.plot(x, y_star, 'o-', label='$K^*$ (Theoretical)')
    plt.plot(x, y_exp, 's--', label='$K_{exp}$ (Experimental)')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Overall Heat Transfer Coefficient $K$ (W/m$\cdot$K)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"Figures/plot_{fig_id}.png")
    plt.close()

# Flow rate values
vals = [4, 6, 8, 10, 12]

# Tube B (plot_1 to plot_8)
# G1 dependence (plot_1-4 -> actually we have 5 values now)
# Let's match the user's previous 4-plot grid if needed, 
# but we have 5 flow rates. We'll plot all 4 requested or just all 5.
# User's previous script used plot_1..plot_4 for B-G1, plot_5..plot_8 for B-G2
# I'll stick to the 4 values [4, 6, 8, 10] if they want 2x2 grid.
# Actually I'll use 4 values: 4, 6, 8, 12 to show the spread.
plot_vals = [4, 6, 8, 12]

for i, v in enumerate(plot_vals):
    plot_fig(rb, 'G1', v, "Tube B", i+1)

for i, v in enumerate(plot_vals):
    plot_fig(rb, 'G2', v, "Tube B", i+5)

# Tube C (plot_9 to plot_16)
for i, v in enumerate(plot_vals):
    plot_fig(rc, 'G1', v, "Tube C", i+9)

for i, v in enumerate(plot_vals):
    plot_fig(rc, 'G2', v, "Tube C", i+13)

print("Generated plot_1.png to plot_16.png (Correctly synced with procedural data)")
