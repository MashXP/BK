# Chapter 2: Heat Transfer, Thermodynamics, and Drying

In this chapter, we transition from moving solids to moving **energy**. You will explore how to dry materials, how to swap heat between fluids, and how air "holds" water.

---

## 1. Convective Drying
*How air whisks away moisture.*

### 🔍 What will you learn?
- The difference between **Constant Rate** and **Falling Rate** drying.
- Why **Wet-Bulb Temperature** is the "cooling limit" of evaporation.

### 💡 The Drying Curve
Imagine a wet sponge in a wind tunnel:
1.  **Constant Rate Period**: The surface is soaking wet. Evaporation happens as fast as the air can take it.
2.  **Falling Rate Period**: The surface is drying out. Water now has to "crawl" (diffuse) from the inside of the sponge to the surface. This is much slower!

> [!TIP]
> **Wet-Bulb Temperature ($t_w$)**: This is the lowest temperature air can reach by evaporating water into itself. If you feel cold after stepping out of a shower, you are experiencing the wet-bulb effect!

### 📐 Key Formulas: Drying Kinetics
To calculate drying times and describe kinetics, we use equations for the constant and falling rate periods.

1. **Drying Time ($\tau$):**
   The total drying time is the sum of the constant-rate period ($\tau_1$) and falling-rate period ($\tau_2$):
   $$\tau = \tau_1 + \tau_2 = \frac{U_0 - U_{th}}{N} + \frac{U_{th} - U^*}{N} \ln\left(\frac{U_{th} - U^*}{U_2 - U^*}\right)$$
   Alternatively, using common logarithms ($\lg$):
   $$\tau = \frac{U_0 - U_{th}}{N} + \frac{2.3}{N} (U_{th} - U^*) \lg\left(\frac{U_{th} - U^*}{U_2 - U^*}\right)$$
   Where:
   - $U_0$: Initial moisture content ($\text{kg moisture} / \text{kg dry material}$).
   - $U_{th}$: Critical moisture content at the transition point.
   - $U_2$: Final moisture content at the end of the drying process.
   - $U^*$: Equilibrium moisture content.
   - $N$: Constant drying rate ($\text{kg moisture} / (\text{kg dry material} \cdot \text{s})$).

2. **Critical Moisture Content Approximation ($U_{th}$):**
   $$U_{th} = \frac{U_0}{1.8} + U^*$$

3. **Rebinder Number ($Rb$):**
   Characterizes drying kinetics and describes the fraction of heat used for raising the material's temperature vs. vaporizing moisture:
   $$Rb = 1 + \left(\frac{C}{r}\right)\frac{d\theta}{dU}$$
   Where $C$ is the specific heat of the moist material, $r$ is the latent heat of vaporization, and $\theta$ is the material temperature.

---

## 2. Double Pipe Heat Exchanger
*The art of thermal trading.*

### 🔍 What will you learn?
- Why **Counter-Current** flow is usually superior to **Parallel** flow.
- How to calculate the "Mean Temperature Difference" (LMTD).

### 💡 Counter-Current vs. Parallel
- **Parallel Flow**: Hot and Cold fluids start at the same end. They "meet in the middle" and can never cross temperatures.
- **Counter-Current Flow**: Hot and Cold fluids start at opposite ends. This allows the cold fluid to potentially get hotter than the exiting hot fluid! It is much more efficient.

### 🛠️ Practical Laboratory Insight
> [!IMPORTANT]
> **Why do we need a "Heat Balance"?**
> In theory, $Q_{\text{lost by hot}} = Q_{\text{gained by cold}}$. 
> In the lab, $Q_{\text{lost}}$ is always larger. Why? Because the pipe walls aren't perfectly insulated; some heat escapes into the room.

### 📐 Key Formulas: Heat Exchanger Dynamics
1. **Heat Balance ($Q$):**
   $$Q = G_1 C_{p1}(t_{1\text{in}} - t_{1\text{out}}) = G_2 C_{p2}(t_{2\text{out}} - t_{2\text{in}})$$
   Where:
   - $G_1, G_2$: Hot and cold fluid mass flow rates ($\text{kg/s}$).
   - $C_{p1}, C_{p2}$: Average specific heat capacities ($\text{J}/(\text{kg}\cdot\text{K})$).
   - $t_{1\text{in}}, t_{1\text{out}}$: Inlet and outlet temperatures of the hot stream ($^\circ\text{C}$).
   - $t_{2\text{in}}, t_{2\text{out}}$: Inlet and outlet temperatures of the cold stream ($^\circ\text{C}$).

2. **Heat Transfer Rate ($Q$):**
   $$Q = K_l \cdot \Delta t_{\text{log}} \cdot L$$
   Where $L$ is the effective pipe length ($\text{m}$), $K_l$ is the experimental linear heat transfer coefficient ($\text{W}/(\text{m}\cdot\text{K})$), and $\Delta t_{\text{log}}$ is the logarithmic mean temperature difference (LMTD).

3. **Logarithmic Mean Temperature Difference (LMTD, $\Delta t_{\text{log}}$):**
   $$\Delta t_{\text{log}} = \frac{\Delta t_{\text{max}} - \Delta t_{\text{min}}}{\ln\left(\frac{\Delta t_{\text{max}}}{\Delta t_{\text{min}}}\right)}$$
   For countercurrent flow:
   $$\Delta t_{\text{max}} = t_{1\text{in}} - t_{2\text{out}}, \quad \Delta t_{\text{min}} = t_{1\text{out}} - t_{2\text{in}}$$

4. **Theoretical Overall Linear Heat Transfer Coefficient ($K_l^*$):**
   $$K_l^* = \frac{\pi}{\frac{1}{\alpha_1 d_1} + \frac{1}{2\lambda_w} \ln\left(\frac{d_2}{d_1}\right) + \frac{1}{\alpha_2 d_{2}}}$$
   Where:
   - $\alpha_1, \alpha_2$: Convective heat transfer coefficients of the inner and outer fluids ($\text{W}/(\text{m}^2\cdot\text{K})$).
   - $\lambda_w$: Thermal conductivity of the copper wall ($\text{W}/(\text{m}\cdot\text{K})$).
   - $d_1, d_2$: Internal and external diameters of the inner pipe ($\text{m}$).

5. **Convective Heat Transfer Coefficient ($\alpha$):**
   $$\alpha = \frac{Nu \cdot \lambda}{l}$$
   Where $Nu$ is the dimensionless Nusselt number, $\lambda$ is the fluid's thermal conductivity, and $l$ is the characteristic dimension.

6. **Dimensionless Numbers:**
   - **Reynolds Number ($Re$):** $Re = \frac{w \cdot l}{\nu}$ (flow regime, where $w$ is velocity and $\nu$ is kinematic viscosity).
   - **Prandtl Number ($Pr$):** $Pr = \frac{\nu}{a} = \frac{\mu \cdot C_p}{\lambda}$ (momentum to thermal diffusivity).
   - **Grashof Number ($Gr$):** $Gr = \frac{g \cdot \beta \cdot \Delta t \cdot l^3}{\nu^2}$ (buoyancy to viscous forces in natural convection).

---

## 3. Thermodynamics (Cooling & Dehumidification)
*Understanding the "invisible" water in air.*

### 🔍 What will you learn?
- How to read a **Psychrometric Chart** (mentally).
- Why windows "fog up" (The Dew Point).

### 💡 The "Moist Air" Cheat Sheet
- **Dry Bulb ($t$)**: The temperature on a normal thermometer.
- **Relative Humidity ($\varphi$)**: How "full" the air is of water (0% = Bone dry, 100% = Fog/Rain).
- **Dew Point ($T_{dp}$)**: The temperature where air can no longer hold its water, and it starts to rain or form droplets.

### 📐 Key Formulas: Air Properties & Energy Balance
1. **Relative Humidity ($\varphi$):**
   $$\varphi = \frac{p_m}{p_b} - \frac{A \cdot B}{p_b}(t_{dry} - t_{wet})$$
   Where $p_m$ and $p_b$ are water vapor saturation pressures at $t_{wet}$ and $t_{dry}$, $B$ is barometric pressure, and $A$ is the psychrometric constant.

2. **Absolute Humidity ($d$):**
   $$d = \frac{18}{29} \times \frac{\varphi \cdot p_b}{B - \varphi \cdot p_b} \quad [\text{kg}_{\text{H2O}}/\text{kg}_{\text{dry\_air}}]$$

3. **Moist Air Enthalpy ($I$):**
   $$I = t_{dry} + (2493 + 1.97 \cdot t_{dry}) \cdot d \quad [\text{kJ/kg}_{\text{dry\_air}}]$$

4. **Dry Air Mass Flow Rate ($G_{kk}$):**
   $$G_{kk} = v \cdot F \cdot \rho \quad [\text{kg/s}]$$
   Where $v$ is air velocity at the aerodynamic tube outlet ($\text{m/s}$), $F = 0.0144\text{ m}^2$ is the outlet area, and $\rho$ is the specific mass of air ($\text{kg/m}^3$).

5. **Cooling Capacity ($Q_0$) & Dehumidification Rate ($G_{water}$):**
   - **Sensible & Latent Heat Load ($Q_0$):** $Q_0 = G_{kk} (I_1 - I_2) \quad [\text{kW}]$
   - **Theoretical Condensate ($G_{water}$):** $G_{water} = 3600 \cdot G_{kk} \cdot (d_1 - d_2) \quad [\text{kg/h}]$
   - **Practical Condensate ($G'_{water}$):** $G'_{water} = \frac{0.06 \cdot V_1}{t_1} \quad [\text{kg/h}]$ (where $V_1$ is volume in $\text{mL}$ and $t_1$ is collection time in $\text{min}$).

### 🧪 Troubleshooting the Lab
> [!NOTE]
> **Why are air velocity measurements tricky?**
> Air doesn't flow at the same speed everywhere in a pipe. It's slower near the walls and faster in the center. We must take an average to get an accurate **Volumetric Flow Rate**.

---

## Related Materials
- [[Mechanical_Lab_Study_Guide.md|Overview Guide]]
- [[Drying/2.DRYING.tex|Drying Report]]
- [[DoublePipe/5.DOUBLE-PIPE.tex|Heat Exchanger Report]]
- [[Thermodynamics/4.THERMODYNAMICS.tex|Thermodynamics Report]]
