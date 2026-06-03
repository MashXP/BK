# Chapter 3: Mass Transfer and Hydraulics

In this final chapter, we look at how to separate chemicals and how fluids behave in "cluttered" spaces (packed beds). We also explore how "well-behaved" a reactor is.

---

## 1. Distillation
*Separating fluids by boiling point.*

### 🔍 What will you learn?
- The **McCabe-Thiele** method: A "staircase" to purity.
- The **Reflux Ratio**: The lever we pull to control the column.

### 💡 The "Reflux" Concept
Imagine a column where vapor goes up and liquid comes down.
- **High Reflux**: We send more liquid back down. This "washes" the vapor more thoroughly, giving us higher purity but lower product flow.
- **Low Reflux**: More product, but lower purity.

> [!TIP]
> **The McCabe-Thiele Staircase**: Each "step" on the graph represents one physical tray in the column where vapor and liquid meet and reach equilibrium.

### 📐 Key Formulas: Distillation Calculations
1. **Molar Fraction Conversion (from Mass Concentration $C$):**
   $$x = \frac{C/M_{\text{ethanol}}}{C/M_{\text{ethanol}} + (1-C)/M_{\text{water}}}$$
   Where $M_{\text{ethanol}} = 46\text{ g/mol}$ and $M_{\text{water}} = 18\text{ g/mol}$.

2. **Operating Lines (McCabe-Thiele):**
   - **Rectifying (Enriching) Operating Line:** 
     $$y_{n+1} = \frac{R}{R+1}x_n + \frac{x_D}{R+1}$$
     Where $R = L/D$ is the reflux ratio, and $x_D$ is the distillate composition.
   - **Stripping Operating Line:** 
     $$y_{n+1} = \frac{L_s}{V_s}x_n - \frac{B}{V_s}x_B = \frac{V_B+1}{V_B}x_n - \frac{x_B}{V_B}$$
     Where $V_B = V_s/B$ is the boil-up ratio, and $x_B$ is the bottom product composition.
   - **Feed Line (q-line):**
     $$y = \frac{q}{q-1}x - \frac{x_F}{q-1}$$
     Where $q$ is the feed quality parameter. For saturated liquid feed, $q=1$ (vertical line).
     $$q = \frac{H_{GF} - H_F}{H_{GF} - H_{LF}} = \frac{r_{\text{mix}} + C_{\text{mix}}(t_{\text{bp}} - t_F)}{r_{\text{mix}}}$$

3. **Column Efficiencies:**
   - **Overall Column Efficiency ($E_0$):**
     $$E_0 = \frac{N_{\text{theoretical}}}{N_{\text{actual}}}$$
     Where $N_{\text{actual}} = 5$ for the lab column.
   - **Murphree Tray Efficiency ($E_M$):**
     $$E_M = \frac{y_n - y_{n+1}}{y_n^* - y_{n+1}}$$
     Where $y_n^*$ is the vapor composition in equilibrium with liquid composition $x_n$.

---

## 2. Packed Column
*Fluid traffic in a maze.*

### 🔍 What will you learn?
- Why **Ceramic Raschig Rings** are used (to increase surface area).
- The "Traffic Jam" of the chemical world: **Flooding**.

### 💡 Flooding: The Ultimate Limit
Imagine air blowing up a pipe while water trickles down.
1.  **Loading**: The air is fast enough that it starts to "hold up" the water. The pressure drop spikes.
2.  **Flooding**: The air is so fast that water can't flow down at all. The column fills with liquid, and separation stops. 
> [!IMPORTANT]
> **Rule of Thumb**: Always operate at 60-80% of the flooding velocity. Never at 100%!

### 📐 Key Formulas: Pressure Drop & Hydraulics
1. **Dry Column Pressure Drop ($\Delta P_{dry}$):**
   - **Empirical Relationship:** $\Delta P_{dry} = \alpha G^n \quad (\text{where } n \approx 1.8 \text{ to } 2.0)$
   - **Zhavoronkov Equation:**
     $$\Delta P_{dry} = \frac{2f_{dry} G^2 Z}{\varepsilon^2 \rho_G D_e}$$
     Where $G$ is gas mass velocity ($\text{kg}/(\text{m}^2\cdot\text{s})$), $Z$ is packing depth ($\text{m}$), $\varepsilon$ is packing porosity, $\rho_G$ is gas density ($\text{kg/m}^3$), and $D_e = 4\varepsilon / a$ is the equivalent diameter of the packing (specific surface area $a$).

2. **Dry Friction Factor ($f_{dry}$):**
   For turbulent flow ($50 < Re_c < 7000$):
   $$f_{dry} = \frac{3.8}{Re_c^{0.2}} \quad \text{with} \quad Re_c = \frac{G D_e}{\varepsilon \mu} = \frac{4G}{a \mu}$$
   Where $\mu$ is gas viscosity.

3. **Wetted Column Pressure Drop ($\Delta P_{wet}$):**
   $$\Delta P_{wet} = \sigma \Delta P_{dry} \quad \implies \quad f_{wet} = \sigma f_{dry}$$
   - **Leva's Correlation:** $\sigma = 10^{\Omega L} \implies \log \sigma = \Omega L$ (where $L$ is liquid velocity and $\Omega = 0.084$ for 12.7 mm Raschig rings).
   - **Alternative Hold-up Equation ($A < 0.3$):**
     $$\frac{\Delta P_{wet}}{\Delta P_{dry}} = \frac{1}{(1-A)^3} \quad \text{with} \quad A = \sqrt{\frac{1.75}{Re_L} \left( \frac{G_L}{F \rho_L} \right) \frac{q}{2g \varepsilon^2}}$$

---

## 3. Residence Time Distribution (RTD)
*The "Age" of a fluid element.*

### 🔍 What will you learn?
- The **Pulse Method**: Injecting a tracer as a pulse signal (represented mathematically by the **Dirac Delta Function** $\delta(t)$) to determine how long fluid elements reside in the system.
- **Dead Zones**: The "corners" where fluid gets stuck.

### 💡 The $E(t)$ Curve
- **Ideal Plug Flow (PFR)**: Everything enters and exits at exactly the same time. The curve is a single sharp spike.
- **Ideal Mixer (CSTR)**: Some fluid exits immediately, some stays for a long time. The curve is a smooth decay.

### 📐 Key Formulas: RTD Modeling
1. **Average Retention Time ($\bar{t}$):**
   Calculated from experimental tracer concentration curve (or absorbance $D_i$ as a proxy):
   $$\bar{t} = \frac{\sum t_i C_i}{\sum C_i} \approx \frac{\sum t_i D_i}{\sum D_i}$$

2. **Theoretical Space Time (Volume Time, $\tau$):**
   $$\tau = \frac{V_R}{v}$$
   Where $V_R$ is the volume of fluid in the reactor ($\text{L}$), and $v$ is the volumetric flow rate ($\text{L/min}$).

3. **RTD Curve Functions:**
   - **Dimensionless (Compact) Time:** $\theta = \frac{t}{\tau} \quad (\text{or } \theta = \frac{t}{\bar{t}})$
   - **RTD Distribution Function $E(t)$:**
     $$E(t) = \frac{C(t)}{\int_0^\infty C(t)dt} \quad \text{and} \quad E(\theta) = \tau E(t)$$

4. **Tanks-in-Series Model ($N$ reactors in series):**
   $$E(\theta) = \frac{N(N\theta)^{N-1}}{(N-1)!} e^{-N\theta}$$
   - Single CSTR ($N=1$): $E(\theta) = e^{-\theta}$
   - Two CSTRs ($N=2$): $E(\theta) = 4\theta e^{-2\theta}$
   - Three CSTRs ($N=3$): $E(\theta) = \frac{27}{2}\theta^2 e^{-3\theta}$

### 🧪 Troubleshooting the Lab
> [!CAUTION]
> **The Photometer Challenge**:
> RTD experiments use light to detect tracer concentration. 
> - **Dirty Cuvettes**: Even a fingerprint on the glass can throw off the results.
> - **Finite Pulse**: In theory, we inject the tracer in 0 seconds. In reality, it takes ~5 seconds. This "spreads" the data and makes it look different from theory.

---

## Related Materials
- [[Mechanical_Lab_Study_Guide.md|Overview Guide]]
- [[DISTILLATION/6.DISTILLATION.tex|Distillation Report]]
- [[PackedColumn/8.PACKED_COLUMN.tex|Packed Column Report]]
- [[RetentionTime/7.RETENTIONTIME.tex|RTD Report]]
