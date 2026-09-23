# 03 — Enzyme Catalysis & Kinetics

**Module:** 03  
**Parent:** [[00_MOC_Prot_and_Enzyme|Index / MOC]] | **Previous:** [[02_Protein_Structure_and_Folding|02 — Protein Structure & Folding]]  
**Topics:** Biocatalysis, EC Classification (1–6 & 7), Reaction Free Energy & Eyring Equation, Equilibrium Invariance, Transition-State Stabilization, Michaelis–Menten Derivation & Interpretation, Course Project

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
* **Catalytic Efficiency:** The slope $\frac{V_{\max}}{K_m} = \frac{k_{\text{cat}}[\text{E}]_T}{K_m}$ reflects the apparent second-order rate constant, with $\frac{k_{\text{cat}}}{K_m}$ representing enzyme **specificity / catalytic efficiency** ($\text{M}^{-1}\text{s}^{-1}$).

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