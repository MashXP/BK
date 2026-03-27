import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('Images', exist_ok=True)

# Using exactly the calculated data from the report tables
U_50 = [4.00, 4.00, 4.00, 4.00, 0.00, 0.00, 0.00]
N_50 = [0.00, 0.00, 0.00, 0.00, 48.00, 0.00, 0.00]

U_60 = [7.69, 3.85, 3.85, 0.00, 0.00, 0.00]
N_60 = [0.00, 76.92, 0.00, 76.92, 0.00, 0.00]

U_70 = [4.00, 4.00, 4.00, 0.00, 0.00, 0.00, 0.00]
N_70 = [0.00, 0.00, 0.00, 120.00, 0.00, 0.00, 0.00]

def plot_rate_curve(U, N, temp, filename):
    plt.figure(figsize=(4, 3))
    # N vs U. Standard is U on x-axis (often reading right-to-left, but scatter is fine either way)
    # We sort by U to make the line continuous, or just plot sequence? 
    # Usually drying goes from high U to low U.
    plt.plot(U, N, 'o-', color='#ff7f0e', linewidth=2, markersize=6)
    
    plt.title(f'Drying Rate at {temp}$^\\circ$C')
    plt.xlabel('Moisture Content $U$ (%)')
    plt.ylabel('Drying Rate $N$ (%/h)')
    plt.grid(True, linestyle='--', alpha=0.6)
    # Standard engineering curve reverses x-axis
    plt.xlim(max(U) + 1, -1)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

plot_rate_curve(U_50, N_50, 50, 'Images/exp_rate_curve_50.pdf')
plot_rate_curve(U_60, N_60, 60, 'Images/exp_rate_curve_60.pdf')
plot_rate_curve(U_70, N_70, 70, 'Images/exp_rate_curve_70.pdf')
