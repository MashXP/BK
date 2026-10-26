# 03 — Enzyme Catalysis & Kinetics

**Module:** 03  
**Parent:** [[00_MOC_Prot_and_Enzyme|Index / MOC]] | **Previous:** [[02_Protein_Structure_and_Folding|02 — Protein Structure & Folding]] | **Next:** [[04_Protein_and_Enzyme_Recovery_Techniques|04 — Protein & Enzyme Recovery Techniques]]  
**Topics:** Biocatalysis, EC Classification (1–6 & 7), Reaction Free Energy & Eyring Equation, Equilibrium Invariance, Transition-State Stabilization, Michaelis–Menten Derivation & Interpretation, 3 substrate regimes, Diffusion Limit on $k_{\text{cat}}/K_m$, Reversible Inhibition Types & Diagnostics, Rate Constant → Half-Life, Course Project

---

## 1. Fundamentals of Biological Catalysts

* **Nature:** Macromolecular biocatalysts that accelerate chemical reaction rates by orders of magnitude ($10^5$ to $10^{17}$-fold) without undergoing permanent chemical change or being consumed.
* **Composition:**
  * Vast majority are **globular proteins**.
  * Catalytic RNA molecules are termed **ribozymes** (e.g., peptidyl transferase center of the ribosome, self-splicing group I/II introns).
* **Historical Context:** Systematic biochemical studies originated in the late 18th century (digestion experiments by Spallanzani $\to$ isolation of diastase/amylase by Payen & Persoz $\to$ cell-free fermentation by Buchner, 1897).

---

## 2. Enzyme Commission (EC) Classification

Enzymes are systematically classified into primary classes based on catalyzed reaction type:

| EC Class | Enzyme Class | Primary Catalytic Function | Generalized Reaction Scheme | Representative Examples |
| :---: | :--- | :--- | :--- | :--- |
| **EC 1** | **Oxidoreductases** | Catalyze oxidation-reduction via transfer of electrons, $\text{H}^-$, or $\text{H}^\bullet$ | $\text{A}_{\text{red}} + \text{B}_{\text{ox}} \rightleftharpoons \text{A}_{\text{ox}} + \text{B}_{\text{red}}$ | Dehydrogenases, oxidases, reductases, peroxidases |
| **EC 2** | **Transferases** | Transfer specific functional groups (phosphate, methyl, acyl) from donor to acceptor | $\text{A-X} + \text{B} \rightleftharpoons \text{A} + \text{B-X}$ | Kinases, transaminases, methyltransferases |
| **EC 3** | **Hydrolases** | Cleave covalent bonds through hydrolytic addition of $\text{H}_2\text{O}$ | $\text{A-B} + \text{H}_2\text{O} \to \text{A-OH} + \text{B-H}$ | Peptidases/proteases, lipases, amylases, phosphatases |
| **EC 4** | **Lyases** | Cleave or form $\text{C}-\text{C}, \text{C}-\text{O}, \text{C}-\text{N}$ bonds non-hydrolytically (forming double bonds or rings) | $\text{X-A-B-Y} \rightleftharpoons \text{A=B} + \text{X-Y}$ | Decarboxylases, aldolases, dehydratases |
| **EC 5** | **Isomerases** | Transfer groups within a molecule to produce structural or geometric isomers | $\text{A} \rightleftharpoons \text{A}_{\text{isomer}}$ | Racemases, epimerases, mutases, cis-trans isomerases |
| **EC 6** | **Ligases** | Join two molecules coupled to high-energy nucleoside triphosphate cleavage ($\text{ATP}$) | $\text{A} + \text{B} + \text{ATP} \to \text{A-B} + \text{ADP} + \text{P}_i$ | DNA ligases, synthetases, carboxylases |
| *EC 7* | *Translocases* | Catalyze movement of ions or molecules across membranes | $\text{AX} + \text{B}_{\text{side1}} \to \text{A} + \text{X} + \text{B}_{\text{side2}}$ | ABC transporters, ATP synthases |

---

## 3. Reaction Energetics & Reaction Coordinate

```
Free Energy (G)
      ▲
      │           ‡ (Uncatalyzed Transition State)
      │          / \
      │         /   \  ▲ ΔG‡_uncat
      │        /     \ │
      │   S   /  ES‡  \│           ‡ (Catalyzed Transition State)
      │  ─── /   /\    ▼          / \
      │     ▼   /  \             /   \  ▲ ΔG‡_cat
      │     ───     \           /     ▼ │
      │     ES       \   EP    /
      │               \───/   /
      │                        \     P
      │                         ▼  ──────
      │                            ▲
      │                            │ ΔG° (Unchanged)
      │                            ▼
      └────────────────────────────────────────► Reaction Coordinate
```

* **Transition State ($\ddagger$):** Transient, high-energy chemical configuration where bonds are in the process of breaking and forming.
* **Activation Energy ($\Delta G^\ddagger$):** Free energy barrier between ground state reactants and transition state.
* **Eyring-Polanyi Rate Formulation:**
  $$k = \frac{k_B T}{h} \exp\left(-\frac{\Delta G^\ddagger}{RT}\right)$$
  * Reaction rate constant $k$ is exponentially dependent on activation free energy $\Delta G^\ddagger$.
  * Lowering $\Delta G^\ddagger$ exponentially enhances reaction rate.
  * **Arrhenius Form (empirical activation energy $E_a$):**
  $$k = A \exp\left(-\frac{E_a}{RT}\right)$$
  * $A$: pre-exponential (attempt frequency); $E_a$: activation energy. Eyring's $\frac{k_B T}{h} \approx 6.2\times 10^{12}\ \text{s}^{-1}$ at 25 °C plays the role of $A$.
  * **Rate Constant → Half-Life:** for first-order decay $[\text{S}](t) = [\text{S}]_0 e^{-kt}$, setting $[\text{S}] = \tfrac{1}{2}[\text{S}]_0$ gives $e^{-kt} = \tfrac{1}{2} \implies kt = \ln 2$:
  $$t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{k}$$
  * **Worked example** ($RT = 2.48\ \text{kJ mol}^{-1}$ at 25 °C):
  ```text
  k = (k_B T/h) exp(−ΔG‡/RT)
  k = 6.2×10¹² × exp(−100 / 2.48)          # uncatalysed
  k = 1.9×10⁻⁵ s⁻¹   →   t½ = 0.693/1.9×10⁻⁵ = 3.6×10⁴ s ≈ 10 h

  k = (k_B T/h) exp(−ΔG‡/RT)
  k = 6.2×10¹² × exp(−80 / 2.48)           # enzyme lowers barrier by 20 kJ/mol
  k = 6.1×10⁻² s⁻¹   →   t½ = 0.693/6.1×10⁻² = 11.4 s

  fold = exp(ΔΔG‡/RT)
  fold = exp(20 / 2.48)
  fold = 3.2×10³ ≈ 3200×
  ```
  * Cutting the barrier by 20 % (100 → 80 kJ/mol) multiplies the rate by ~3200, because the rate factor is **exponential** in the barrier, not linear. Rate is set by the **highest single step** (rate-determining step), not by the number of steps, so a lower multi-step path beats a single high barrier. The enzyme changes rate only: $\Delta G^\circ$ and $K_{eq}$ are untouched (Section 4).
* **Catalyzed Reaction Intermediates:**
  $$\text{E} + \text{S} \rightleftharpoons \text{ES} \to \text{EP} \rightleftharpoons \text{E} + \text{P}$$
  * Enzymes replace a single high barrier ($\Delta G^\ddagger_{\text{uncat}}$) with discrete, lower activation barriers passing through $\text{ES}$ and $\text{EP}$ complexes ($\Delta G^\ddagger_{\text{cat}} \ll \Delta G^\ddagger_{\text{uncat}}$).

---

## 4. Enzymes Do Not Alter Chemical Equilibrium

* **$\Delta G^\circ$ Invariance:** Overall standard free energy change $\Delta G^\circ$ is defined solely by the difference in free energy between reactants and products ($G^\circ_P - G^\circ_S$). Enzymes have **zero effect** on $\Delta G^\circ$.
* **Equilibrium Constant ($K_{\text{eq}}$):** Because $\Delta G^\circ = -RT \ln K_{\text{eq}}$, the equilibrium ratio of products to substrates ($[P]_{\text{eq}} / [S]_{\text{eq}}$) is completely unaffected.
* **Bidirectional Acceleration:** Enzymes lower the activation barrier equally for both the forward and reverse reactions, accelerating the speed at which equilibrium is reached.

---

## 5. Transition-State Stabilization & The Substrate Binding Trap

* **$\text{E}-\text{S}$ Binding:** Initial substrate recruitment relies on weak non-covalent interactions (hydrogen bonds, electrostatic attraction, hydrophobic contacts, Van der Waals forces).
* **Transition State Complementarity (Pauling Principle):** Active sites are chemically and structurally complementary to the **transition state ($\ddagger$)**, not the ground-state substrate.
* **The Thermodynamic Pit Fallacy:**
  * If an enzyme bound the ground-state substrate too tightly ($K_d \lll 1$), the $\text{ES}$ complex would sit in a deep thermodynamic well.
  * This would **increase** the effective activation energy required to achieve the transition state ($\Delta G^\ddagger_{\text{effective}} \uparrow$), slowing down or arresting catalysis.
  * Optimal catalysis requires moderate substrate affinity and maximal transition-state stabilization.

---

## 6. Enzyme Kinetics: Definition & Measurements

* **Enzyme Kinetics:** Quantitative characterization of reaction velocities and their dependency on enzyme concentration ($[\text{E}]$), substrate concentration ($[\text{S}]$), cofactors, activators, inhibitors, temperature, and $\text{pH}$.
* **Standard Initial Velocity Protocol:**
  1. Mix fixed concentration of enzyme ($[\text{E}]_T$) with varying concentrations of substrate ($[\text{S}]$).
  2. Monitor product accumulation ($[\text{P}]$) or substrate depletion ($[\text{S}]$) continuously over time via spectrophotometry (absorbance).
  3. Determine **initial velocity ($v_0 = \frac{d[\text{P}]}{dt}$)** from the linear slope before significant substrate depletion ($< 10\%$) or reverse reaction/product inhibition occurs.
  4. Construct the hyperbolic saturation curve plotting $v_0$ versus $[\text{S}]$.

---

## 7. Step-by-Step Derivation of the Michaelis–Menten Equation

**Reaction Scheme:**

$$\text{E} + \text{S} \xrightleftharpoons[k_{-1}]{k_1} \text{ES} \xrightarrow{k_{\text{cat}}} \text{E} + \text{P}$$

* $\text{E}$: Free enzyme
* $\text{S}$: Substrate
* $\text{ES}$: Enzyme–substrate complex
* $\text{P}$: Product
* $k_1$: Rate constant for $\text{ES}$ formation ($\text{M}^{-1}\text{s}^{-1}$)
* $k_{-1}$: Rate constant for $\text{ES}$ dissociation back to $\text{E} + \text{S}$ ($\text{s}^{-1}$)
* $k_{\text{cat}}$: Catalytic rate constant / turnover number for product formation ($\text{s}^{-1}$)

---

### Step 1: Define Initial Velocity of Product Formation
The initial rate of product formation ($v_0$) is governed by the irreversible catalytic breakdown of the $\text{ES}$ complex:

$$v_0 = \frac{d[\text{P}]}{dt} = k_{\text{cat}}[\text{ES}] \quad (1)$$

To evaluate $v_0$, the unknown intermediate concentration $[\text{ES}]$ must be expressed in terms of measurable quantities: substrate concentration $[\text{S}]$ and total enzyme concentration $[\text{E}]_T$.

---

### Step 2: Apply the Steady-State Assumption (*Giả định trạng thái ổn định*)
Under the Briggs–Haldane steady-state condition, the concentration of the intermediate complex $[\text{ES}]$ remains approximately constant during initial velocity measurements:

$$\frac{d[\text{ES}]}{dt} \approx 0 \implies \text{Rate of ES formation} = \text{Rate of ES breakdown}$$

* **Rate of $\text{ES}$ formation:** $k_1[\text{E}][\text{S}]$
* **Rate of $\text{ES}$ breakdown:** $k_{-1}[\text{ES}] + k_{\text{cat}}[\text{ES}] = (k_{-1} + k_{\text{cat}})[\text{ES}]$

Equating formation and breakdown rates:

$$k_1[\text{E}][\text{S}] = (k_{-1} + k_{\text{cat}})[\text{ES}] \implies [\text{E}][\text{S}] = \frac{k_{-1} + k_{\text{cat}}}{k_1}[\text{ES}] \quad (2)$$

The **Michaelis Constant ($K_m$)** is defined as the ratio of breakdown to formation rate constants:

$$K_m = \frac{k_{-1} + k_{\text{cat}}}{k_1} \quad (3)$$

Substituting $(3)$ into $(2)$:

$$[\text{E}][\text{S}] = K_m[\text{ES}] \implies [\text{ES}] = \frac{[\text{E}][\text{S}]}{K_m} \quad (4)$$

---

### Step 3: Apply Enzyme Mass Conservation (*Bảo toàn enzyme*)
Total enzyme concentration ($[\text{E}]_T$) is the sum of free enzyme ($[\text{E}]$) and substrate-bound enzyme ($[\text{ES}]$):

$$[\text{E}]_T = [\text{E}] + [\text{ES}] \implies [\text{E}] = [\text{E}]_T - [\text{ES}]$$

Substitute this expression for $[\text{E}]$ into equation $(4)$:

$$[\text{ES}] = \frac{([\text{E}]_T - [\text{ES}])[\text{S}]}{K_m} \quad (5)$$

Multiply both sides by $K_m$ and expand:

$$K_m[\text{ES}] = [\text{E}]_T[\text{S}] - [\text{ES}][\text{S}]$$

$$K_m[\text{ES}] + [\text{ES}][\text{S}] = [\text{E}]_T[\text{S}]$$

Factor out $[\text{ES}]$:

$$[\text{ES}](K_m + [\text{S}]) = [\text{E}]_T[\text{S}] \implies [\text{ES}] = \frac{[\text{E}]_T[\text{S}]}{K_m + [\text{S}]} \quad (6)$$

---

### Step 4: Formulate the Michaelis–Menten Rate Equation
Substitute $[\text{ES}]$ from equation $(6)$ into the initial velocity equation $(1)$:

$$v_0 = k_{\text{cat}}[\text{ES}] \implies v_0 = \frac{k_{\text{cat}}[\text{E}]_T[\text{S}]}{K_m + [\text{S}]}$$

At saturating substrate concentrations ($[\text{S}] \gg K_m$), all enzyme active sites are occupied ($[\text{ES}] \approx [\text{E}]_T$). The maximum achievable reaction velocity ($V_{\max}$) is defined as:

$$V_{\max} = k_{\text{cat}}[\text{E}]_T$$

Substituting $V_{\max}$ yields the classical **Michaelis–Menten Equation**:

$$v_0 = \frac{V_{\max}[\text{S}]}{K_m + [\text{S}]}$$

---

## 8. Interpretation of the Michaelis–Menten Equation

### 8.1 Low Substrate Concentration ($[\text{S}] \ll K_m$)
When $[\text{S}]$ is very small relative to $K_m$, the term $(K_m + [\text{S}])$ is dominated by $K_m$:

$$\text{When } [\text{S}] \ll K_m \implies K_m + [\text{S}] \approx K_m \implies v_0 \approx \frac{V_{\max}}{K_m}[\text{S}]$$

* **Kinetics:** **First-order** with respect to substrate $[\text{S}]$.
* **Behavior:** Rate increases linearly with $[\text{S}]$. Most enzyme molecules exist in free form ($[\text{E}] \approx [\text{E}]_T$).
* **Catalytic Efficiency:** The slope $\frac{V_{\max}}{K_m} = \frac{k_{\text{cat}}[\text{E}]_T}{K_m}$ reflects the apparent second-order rate constant, with $\frac{k_{\text{cat}}}{K_m}$ representing enzyme **specificity / catalytic efficiency** ($\text{M}^{-1}\text{s}^{-1}$), whose upper bound is set by diffusion (Section 9).

### 8.2 Half-Maximal Saturation ($[\text{S}] = K_m$)
When substrate concentration equals the Michaelis constant:

$$\text{When } [\text{S}] = K_m \implies v_0 = \frac{V_{\max}K_m}{K_m + K_m} = \frac{V_{\max}K_m}{2K_m} = \frac{V_{\max}}{2}$$

* **Operational Definition:** $K_m$ is the substrate concentration at which the reaction velocity reaches exactly half of its maximum value ($\frac{1}{2}V_{\max}$).
* **Affinity Metric:** When $k_{\text{cat}} \ll k_{-1}$, $K_m \approx K_d = \frac{k_{-1}}{k_1}$. A smaller $K_m$ reflects higher apparent substrate-binding affinity.

### 8.3 High Substrate Concentration / Saturation ($[\text{S}] \gg K_m$)
When $[\text{S}]$ is much larger than $K_m$, the denominator $(K_m + [\text{S}])$ is dominated by $[\text{S}]$:

$$\text{When } [\text{S}] \gg K_m \implies K_m + [\text{S}] \approx [\text{S}] \implies v_0 \approx \frac{V_{\max}[\text{S}]}{[\text{S}]} = V_{\max}$$

* **Kinetics:** **Zero-order** with respect to substrate $[\text{S}]$.
* **Behavior:** The enzyme is fully saturated ($[\text{ES}] \approx [\text{E}]_T$). Increasing $[\text{S}]$ yields no further increase in velocity (asymptotic plateau).
* **Limiting Factor:** The catalytic turnover rate constant $k_{\text{cat}}$ ($V_{\max} = k_{\text{cat}}[\text{E}]_T$).

### 8.4 Summary Table: Kinetic Regimes

| Regime | Condition | Simplified Velocity Equation | Reaction Order | Physical State of Enzyme |
| :--- | :--- | :--- | :--- | :--- |
| **Low $[\text{S}]$** | $[\text{S}] \ll K_m$ | $v_0 \approx \left(\frac{V_{\max}}{K_m}\right)[\text{S}]$ | **1st Order** | Free enzyme ($[\text{E}] \approx [\text{E}]_T$); linear rate increase |
| **Half-Saturation** | $[\text{S}] = K_m$ | $v_0 = \frac{V_{\max}}{2}$ | Mixed | Half of active sites occupied ($[\text{ES}] = \frac{1}{2}[\text{E}]_T$) |
| **Saturated $[\text{S}]$** | $[\text{S}] \gg K_m$ | $v_0 \approx V_{\max}$ | **0th Order** | Enzyme fully saturated ($[\text{ES}] \approx [\text{E}]_T$); plateau phase |

### 8.5 Double-Reciprocal Linearisation (Lineweaver–Burk)

Taking the reciprocal of the Michaelis–Menten equation gives a straight line:

$$\frac{1}{v_0} = \frac{K_m}{V_{\max}}\cdot\frac{1}{[\text{S}]} + \frac{1}{V_{\max}}$$

With $y = \frac{1}{v_0}$ and $x = \frac{1}{[\text{S}]}$:

* **Slope** $= \dfrac{K_m}{V_{\max}}$
* **$y$-intercept** $= \dfrac{1}{V_{\max}}$  (read at $x = 0$, i.e. saturating $[\text{S}]$)
* **$x$-intercept** $= -\dfrac{1}{K_m}$

**Worked numbers** ($V_{\max} = 100\ \mu\text{M/s}$, $K_m = 20\ \mu\text{M}$, competitive inhibitor with $\alpha = 2$, $\alpha' = 1$):

```text
1/v = (K_m/V_max)(1/[S]) + 1/V_max
no inhibitor:      1/v = (20/100)(1/[S]) + 1/100    slope 0.2,  intercept 0.01
with inhibitor:    1/v = (40/100)(1/[S]) + 1/100    slope 0.4,  intercept 0.01

set 1/[S] = 0  →  1/v = 1/V_max = 0.01  →  v = V_max = 100 µM/s   (both lines)
K_m^app = slope × V_max = 0.4 × 100 = 40 µM = α K_m
```

Both lines cross the $y$-axis at the same point → $V_{\max}$ unchanged; slope doubled → apparent $K_m$ doubled.

**Three linearisations of the same data:**

| Plot | $y$ | $x$ | Slope | Intercept |
| :--- | :--- | :--- | :--- | :--- |
| **Lineweaver–Burk** | $1/v_0$ | $1/[\text{S}]$ | $K_m/V_{\max}$ | $1/V_{\max}$ |
| **Eadie–Hofstee** | $v_0$ | $v_0/[\text{S}]$ | $-K_m$ | $V_{\max}$ |
| **Hanes–Woolf** | $[\text{S}]/v_0$ | $[\text{S}]$ | $K_m/V_{\max}$ | $1/V_{\max}$ |

**Interpretation rule:** the reciprocal plot is a *diagnostic* tool for reading inhibition type from line geometry. It magnifies low-$[\text{S}]$ scatter, so quantitative parameters are fitted by nonlinear regression on the hyperbola; the linear plot stays the visual classifier.

---


## 9. Diffusion Limit on $k_{\text{cat}}/K_m$

Collision (Smoluchowski) rate for two spherical partners in solution:

$$k_{\text{coll}} = 4\pi N_A (r_{\text{E}} + r_{\text{S}})(D_{\text{E}} + D_{\text{S}})$$

$$k_{\text{coll}} \approx 10^{10}\ \text{M}^{-1}\text{s}^{-1} \quad (r \approx 500\ \text{pm},\ D \approx 10^{-9}\ \text{m}^2\text{s}^{-1})$$

Observed ceiling is lower: orientation requirements, steric gating, and an activation barrier reduce the effective rate to

$$\frac{k_{\text{cat}}}{K_m} \lesssim 10^{8} - 10^{9}\ \text{M}^{-1}\text{s}^{-1}$$

Enzymes near this ceiling are called **kinetically perfect** (diffusion-limited). A measured value far below the ceiling means chemistry, not capture, is rate-limiting.

**Worked comparison:** $k_{\text{cat}} = 500\ \text{s}^{-1}$, $K_m = 20\ \mu\text{M}$:

$$\frac{k_{\text{cat}}}{K_m} = \frac{500\ \text{s}^{-1}}{20\ \mu\text{M}} = 25\ \mu\text{M}^{-1}\text{s}^{-1} = 2.5\times 10^{7}\ \text{M}^{-1}\text{s}^{-1}$$

$$\frac{2.5\times 10^{7}}{10^{9}} = 2.5\% \text{ of the diffusion ceiling}$$

---
## 10. Reversible Inhibition: Scheme & $\alpha/\alpha'$ Formalism

**General scheme (steady state with inhibitor):**

$$\text{E} + \text{S} \overset{k_1}{\underset{k_{-1}}{\rightleftharpoons}} \text{ES} \xrightarrow{k_{\text{cat}}} \text{E} + \text{P}$$
$$\text{E} + \text{I} \overset{}{\underset{K_i}{\rightleftharpoons}} \text{EI} \qquad \text{ES} + \text{I} \overset{}{\underset{K_i'}{\rightleftharpoons}} \text{ESI}$$

**Multiplier definitions:**

$$\alpha = 1 + \frac{[\text{I}]}{K_i} \qquad \alpha' = 1 + \frac{[\text{I}]}{K_i'}$$

**Rate equation in the presence of inhibitor:**

$$v = \frac{V_{\max}[\text{S}]}{\alpha K_m + \alpha'[\text{S}]}$$

Apparent parameters: $V_{\max}^{\text{app}} = \dfrac{V_{\max}}{\alpha'}$, $\quad K_m^{\text{app}} = \dfrac{\alpha}{\alpha'}K_m$.

**Boundary cases:**

* $\alpha' = 1$ (I binds E only) $\to$ **competitive**
* $\alpha = \alpha'$ (I binds E and ES with equal affinity) $\to$ **pure noncompetitive**
* $\alpha = 1$ (I binds ES only) $\to$ **uncompetitive**

---

## 11. Inhibitor Classification Cheat Sheet

| Type | Binding target | Complexes formed | $V_{\max}$ | $K_m$ | $k_{\text{cat}}/K_m$ | Reversible by $[\text{S}]$? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Competitive** | Free E, active site | EI only (ESI dead-end) | **unchanged** | **up** ($\alpha K_m$) | down | **Yes** (high $[\text{S}]$ outcompetes) |
| **Pure noncompetitive** | E and ES, equal affinity | EI + ESI | **down** ($V_{\max}/\alpha$) | **unchanged** | down | **No** |
| **Uncompetitive** | ES only | ESI only | **down** ($V_{\max}/\alpha'$) | **down** ($K_m/\alpha'$) | unchanged | **No** |
| **Mixed** ($\alpha > \alpha'$) | E and ES, E favoured | EI + ESI | **down** | **up** | down | **No** |
| **Mixed** ($\alpha' > \alpha$) | E and ES, ES favoured | EI + ESI | **down** | **down** | down | **No** |

**Diagnostics:** measure $v$ vs $[\text{S}]$ at fixed $[\text{I}]$. Lineweaver–Burk intersection: competitive lines meet on the $y$-axis ($V_{\max}$ fixed); noncompetitive meet on the $x$-axis ($K_m$ fixed); uncompetitive lines are parallel; mixed intersect left of the $y$-axis.

**Direction rule for affinity:** $K_m^{\text{app}}$ up $\Rightarrow$ apparent affinity down; $K_m^{\text{app}}$ down $\Rightarrow$ apparent affinity up. Affinity is inversely related to $K_m$.

---

## 12. Complex Formation Diagrams

```text
Competitive:      E + I ⇌ EI                S cannot bind when I is bound
                  ES → E + P                high [S] displaces I
                  ESI = dead-end (not formed)

Pure noncompetitive:  E + I ⇌ EI
                      ES + I ⇌ ESI          dead-end, no product

Uncompetitive:        ES + I ⇌ ESI          I binds only the ES form

Mixed:                E + I ⇌ EI   and   ES + I ⇌ ESI   (affinities differ)
```
