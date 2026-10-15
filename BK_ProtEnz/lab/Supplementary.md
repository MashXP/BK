# Supplementary — β-Amylase Purification and Activity Assay

Calculations, derivations and reasoning. The protocol itself contains none of this.

---

## S1 Buffer arithmetic

### S1.1 The mass formula

$$m\;(\mathrm{g}) = c\;(\mathrm{mol\,L^{-1}}) \times V\;(\mathrm{L}) \times M\;(\mathrm{g\,mol^{-1}})$$

| Symbol | Meaning |
| :--- | :--- |
| $m$ | mass of the salt to weigh |
| $c$ | target molarity, mol/L — **mM must be divided by 1000** (137 mM = 0.137 mol/L) |
| $V$ | final volume of solution, L |
| $M$ | molar mass of that salt form, g/mol |

Molar masses are taken from the CRC Handbook standard values; the hydrate series in `S1.3` is the set that actually appears on reagent bottles.

### S1.2 1× PBS, pH 7.4 — masses

Target: 137 mM NaCl, 2.7 mM KCl, 10 mM Na₂HPO₄, 1.8 mM KH₂PO₄.

| Reagent | $M$ (g/mol) | $c$ (mol/L) | 1 L | 500 mL | **4 L** |
| :--- | --: | --: | --: | --: | --: |
| NaCl | 58.44 | 0.137 | 8.00628 g | 4.00314 g | **32.02512 g** |
| KCl | 74.55 | 0.0027 | 0.201285 g | 0.1006425 g | **0.80514 g** |
| Na₂HPO₄ anhydrous | 141.96 | 0.010 | 1.4196 g | 0.7098 g | **5.6784 g** |
| KH₂PO₄ | 136.09 | 0.0018 | 0.244962 g | 0.122481 g | **0.979848 g** |

Worked example: NaCl = $0.137 \times 4 \times 58.44 = 32.02512$ g.

### S1.3 Na₂HPO₄ hydrate — the mass changes with the bottle

$141.96$ g/mol is **anhydrous**. A hydrate changes the mass you weigh by up to 2.5×:

| Form | $M$ (g/mol) | 1 L at 10 mM | **4 L** |
| :--- | --: | --: | --: |
| Na₂HPO₄ anhydrous | 141.96 | 1.4196 g | 5.6784 g |
| Na₂HPO₄·2H₂O | 177.99 | 1.7799 g | 7.1196 g |
| Na₂HPO₄·7H₂O | 268.065 | 2.68065 g | 10.7226 g |
| Na₂HPO₄·12H₂O | 358.14 | 3.5814 g | 14.3256 g |

### S1.4 Why the pH needs titrating

The recipe as written does **not** natively give pH 7.4. Henderson–Hasselbalch:

$$\frac{[\mathrm{HPO_4^{2-}}]}{[\mathrm{H_2PO_4^-}]} = 10^{\,\mathrm{pH}-pK_{a2}'}$$

At 37 °C in 137 mM NaCl, $pK_{a2}' \approx 6.8$ — lower than the textbook 7.21 because of ionic strength.

For pH 7.4 the required ratio is:

$$10^{\,7.4-6.8} = 3.9810717$$

Holding $[\mathrm{H_2PO_4^-}] = 1.8$ mM gives:

$$[\mathrm{HPO_4^{2-}}] = 1.8 \times 3.9810717 = 7.1659291\ \text{mM}$$

So of the 10 mM total, $10 - 7.1659291 = 2.8340709$ mM must be protonated:

$$\text{HCl} = 2.8341\ \text{mL of 1 M per litre} \;\Rightarrow\; \mathbf{11.3362836\ \text{mL for 4 L}}$$

This is an **estimate only** — it assumes anhydrous Na₂HPO₄, no CO₂ absorption and 25 °C. Always titrate to the measured pH.

With the classical **8 mM** Na₂HPO₄ / 1.8 mM KH₂PO₄ recipe the requirement drops to ≈ 0.834 mL per litre.

### S1.5 Assay buffer, pH 6.8 — 50 mM

| Salt | $M$ (g/mol) | 100 mL | **500 mL** | 1 L |
| :--- | --: | --: | --: | --: |
| Na₂HPO₄·12H₂O | 358.14 | 1.7907 g | **8.9535 g** | 17.907 g |
| KH₂PO₄ | 136.09 | 0.68045 g | **3.40225 g** | 6.8045 g |

Worked example: $0.05 \times 0.5 \times 358.14 = 8.9535$ g.

> **Correction worth knowing.** An earlier draft of this protocol specified 50 mM but listed masses of 1.7907 g and 0.68045 g for a **1 L** batch. Those figures are right for **100 mL**, not 1 L — the stated concentration and the stated masses were wrong by 10×. The 10 mM Na₂HPO₄·12H₂O entry in the materials list was the tell: 1.7907 g per litre is 5 mM, not 50 mM.

### S1.6 CaCl₂, if required

1 mM = $0.001 \times 110.98 = 0.11098$ g/L.

### S1.7 Water budget

The protocol's 5 L of distilled water is fully consumed by reagent preparation:

| Use | Water |
| :--- | --: |
| 1× PBS 4 L — dissolve in 3200 mL, top to 4000 | 4.00 L |
| Assay buffer 500 mL — 400 mL, top to 500 | 0.50 L |
| Saturated (NH₄)₂SO₄ | 0.05 L |
| DNS reagent — to 100 mL | 0.10 L |
| Maltose standard — to 100 mL | 0.10 L |
| 1 % starch, 2 batches | 0.20 L |
| Tubing soak, glassware rinsing, spare | ~0.05 L |
| **Total** | **4.95 L** |

Water baths (37 °C, 100 °C) run off the tap and are not in this budget.

Note that PBS is counted once, as the 4 L batch, not again as the volume it is later used as — the extraction (60 mL), dialysis, resin hydration and column buffer all come out of that same 4 L. Total draw is about **1.3 L**, so roughly 2.7 L stays in reserve.

**Dialysis ratio.** The external buffer is **1:200** against the sample — 200 mL for the 1.0 mL of Crude Enzyme 2, changed at 2 h and 4 h. That is 600 mL across the 6 h run, not the 4 L an earlier draft assumed.

---

## S2 Ammonium sulfate saturation

### S2.1 The saturation equation

$$V_{\text{salt}} = V_0 \times \frac{S_2 - S_1}{1 - S_2}$$

$V_0$ = extract volume, $S_1$ = starting saturation (0 for a crude extract), $S_2$ = target saturation.

$$20 \times \frac{0.70 - 0}{1 - 0.70} = 20 \times \frac{0.70}{0.30} = \frac{14}{0.3} = \mathbf{46.66667\ \text{mL}}$$

### S2.2 Why 47 mL is wrong

The error sits in the denominator, so it does not cancel:

$$0.70 \times \frac{47}{20 + 47} = 0.70 \times \frac{47}{67} = 0.49105$$

That is 49 % saturation, not 70 %. The shortfall is not a rounding wobble — it changes which proteins precipitate.

### S2.3 Preparing the saturated stock

$$m = V \times \frac{S}{100} = 50 \times \frac{71}{100} = 35.5\ \text{g}$$

Solubility ≈ 71 g/100 mL water at 0–4 °C. Undissolved crystals at 4 °C **confirm** saturation.

**The 35.5 g is a starting estimate, not a target.** It is computed from a tabulated solubility that assumes a pure salt, a particular temperature and equilibrium with the solid phase. The real value moves with temperature, salt grade and how finely the powder was ground — and 71 g/100 mL sits inside a range that different handbooks quote as anywhere from 71 to 76 g/100 mL for the same 0–4 °C window.

So the figure does one job: it tells you roughly how much to weigh so you are adding by the spoonful rather than by the gram, and it gives you a window of error. The endpoint is empirical — **add the salt a few grains at a time until it stops dissolving and dry crystals remain.** That residue is the real confirmation of saturation, and it is worth several grams either side of the calculation.

This matters more than it looks. A stock that is only *near* saturated gives a final saturation below 0.70, and because the error sits in the denominator of

$$S = \frac{S_2 V_{\text{salt}}}{V_0 + V_{\text{salt}}}$$

it does not cancel. A stock 10 % short moves a nominal 70 % precipitation to roughly 0.66 — which is enough to change which proteins come down.

Filtering the crystals out before use would defeat this: you cannot tell a saturated solution from a nearly saturated one by clarity alone. Leave them in, and let them dissolve back in as the stock is consumed on ice.

### S2.4 The dilution arithmetic behind the 5 additions

| Addition | This (mL) | Cumulative salt | Total volume (mL) |
| :--: | --: | --: | --: |
| 1 | 10.0 | 10.0 | 30.0 |
| 2 | 10.0 | 20.0 | 40.0 |
| 3 | 10.0 | 30.0 | 50.0 |
| 4 | 10.0 | 40.0 | 60.0 |
| 5 | **6.66667** | **46.66667** | **66.66667** |

Adding 46.66667 mL of saturated solution to 20 mL of crude extract dilutes it ~3.3×, which costs recovery. That is the price of reaching a defined saturation in one step.

---

## S3 Standard curve

### S3.1 Regression of the reference data

| Tube | $x$ (mg/mL) | $A_{540}$ |
| :--- | --: | --: |
| S0 | 0 | 0 |
| S1 | 0.2 | 0.168 |
| S2 | 0.4 | 0.340 |
| S3 | 0.6 | 0.500 |
| S4 | 0.8 | 0.666 |
| S5 | 1.0 | 0.832 |

Least-squares fit (ordinary linear regression of $A_{540}$ on $x$, the source's own six points):

$$A_{540} = 0.8305714\,x + 0.0023810 \qquad R^2 = 0.99992317$$

The fit is very slightly convex — a marginal negative deviation at mid-range, positive at the top. Well inside experimental error.

### S3.2 The intercept correction

The source notes quote $a = 0.83$ and **$b = 0.0017$** [Miller 1959 gives the method]. The slope is right; the intercept is not.

Regressing their own six points gives **$b = 0.0023810$**. The difference is small in absolute terms but it applies at low absorbance — precisely where the most-diluted samples sit, where the intercept is a large fraction of the reading:

| $A_{\text{corr}}$ | $c$ with $b = 0.0017$ | $c$ with $b = 0.0023810$ | Difference |
| :--: | --: | --: | --: |
| 0.10 | 0.1183 | 0.11746 | 0.7 % |
| 0.20 | 0.2388 | 0.23796 | 0.4 % |
| 0.42 | 0.5046 | 0.50333 | 0.25 % |

### S3.3 Why standards and samples must match exactly

Both are **1.0 mL pre-DNS + 1.0 mL DNS + 8.0 mL water = 10.0 mL final**. Because the dilution is identical, $x$ on the curve reads directly as mg of maltose **per mL of the pre-DNS reaction mixture** — no dilution factor is needed at step 3. Change the water volume for one set and not the other and that shortcut breaks.

### S3.4 The screening curve runs on a different basis

The week-3 fraction screen uses **0.6 mL** pre-DNS and **2.0 mL** water (3.6 mL final). Reusing the week-4 curve on it inflates results by:

$$\frac{1.0}{0.6} = 1.66667$$

so the screening standards must be rebuilt at 0.6 mL.

---

## S4 Activity calculation chain

**1 U** = the enzyme releasing **1 µmol reducing sugar (as maltose) per minute** at 37 °C, at the optimum pH [Bernfeld 1955; Miller 1959]. Amylase hydrolyses starch to maltose and glucose; the reducing aldehyde end of each product reduces DNS to 3-amino-5-nitrosalicylic acid in hot alkali, red-brown, λmax 540 nm [Miller 1959].

$$\text{Specific activity} = \frac{\text{U/mL}}{\text{mg protein/mL}} = \text{U/mg}$$

### S4.1 The six steps

**Step 1 — blank-corrected absorbance**

$$A_{\text{corr}} = A_{\text{sample}} - A_{\text{BE}} - A_{\text{BS}}$$

**Step 2 — concentration from the curve** (mg/mL of pre-DNS reaction mixture)

$$c = \frac{A_{\text{corr}} - b}{a}$$

**Step 3 — mass of sugar produced** (mg)

$$m = c \times V_{\text{total, pre-DNS}}$$

Week 4: $V_{\text{total, pre-DNS}}$ = 1.0 mL, so $m = c$. Screening: 0.6 mL, so $m = 0.6c$.

**Step 4 — micromoles**, $M$(maltose) = **342.296 g/mol**

$$n_{\mu\mathrm{mol}} = \frac{m \times 10^{-3}\ \mathrm{g} \times 10^{6}\ \mu\mathrm{mol/mol}}{342.296\ \mathrm{g/mol}} = \frac{m \times 1000}{342.296}$$

**Step 5 — volumetric activity** (U per mL of the **original, undiluted** sample)

$$\boxed{\ \text{U/mL} = \frac{n_{\mu\mathrm{mol}} \times DF}{t \times V_{\text{enzyme}}} = \frac{n_{\mu\mathrm{mol}} \times DF}{10 \times 0.5}\ }$$

**Step 6 — total activity**

$$\text{Total U} = (\text{U/mL}) \times V_{\text{stage}}$$

### S4.2 Symbols

| Symbol | Meaning |
| :--- | :--- |
| $a$, $b$ | slope and intercept, A₅₄₀ = $ax + b$ |
| $A_{\text{BE}}$ | **enzyme blank** — sugar already in the extract. DNS added *before* enzyme, so this is a true zero-time control |
| $A_{\text{BS}}$ | **substrate blank** — reducing sugar inherent to the starch preparation |
| $DF$ | dilution factor; back-corrects to the original sample |
| $V_{\text{enzyme}}$ | volume of **diluted** enzyme in the reaction, mL |
| $V_{\text{total, pre-DNS}}$ | total liquid before DNS is added, mL |
| $t$ | incubation time, min |

> **The single most common error in this chain** is dividing by 1.0 mL instead of 0.5 mL in step 5. The 1.0 mL is the *reaction* volume (step 3); 0.5 mL is the *enzyme* volume (step 5). Confusing them doubles every activity reported.

### S4.3 Why the two blanks are subtracted

The DNS assay reads **all** reducing sugar present, and there are two sources other than the enzyme's own action:

- **BE** — the extract already contains free sugar (its own glucose). Without this correction every reading is inflated by whatever the tuber started with. Adding DNS *before* the enzyme makes it a true zero-time control rather than a simulated one.
- **BS** — the starch preparation carries reducing ends from partial hydrolysis during preparation or storage. This is why the starch is made fresh.

A third correction is needed when starch concentration differs between formats. The screen runs at 1.67 % (w/v) starch and the quantitative assay at 50 % — **8.3-fold** — and rate depends on substrate concentration. This is why the screen ranks fractions but is never reported as an absolute number.

### S4.4 Error budget

$$\frac{\mathrm{d}c}{\mathrm{d}A} = \frac{1}{a} = 1.2039904\ \text{mg/mL per absorbance unit}$$

| Absorbance error | Error in $c$ | As % at $c$ = 0.5 mg/mL |
| :--: | --: | --: |
| ± 0.001 | ± 0.001204 mg/mL | ± 0.24 % |
| ± 0.002 | ± 0.002408 mg/mL | ± 0.48 % |
| ± 0.005 | ± 0.006020 mg/mL | ± 1.20 % |

For comparison, a 2 s timing slip over a 600 s reaction is 0.33 %.

---

## S5 Worked example

The source optical data, recomputed at full precision. $a = 0.8305714$, $b = 0.0023810$, $M = 342.296$, $t = 10$ min, $V_{\text{enzyme}} = 0.5$ mL, $V_{\text{total}} = 1.0$ mL.

| Sample | $A_{\text{sample}}$ | $A_{\text{BE}}$ | $A_{\text{BS}}$ | $A_{\text{corr}}$ | $c$ (mg/mL) | $n$ (µmol) | $DF$ | **U/mL** |
| :--- | --: | --: | --: | --: | --: | --: | --: | --: |
| 1:5 | 0.868 | 0.020 | 0.020 | 0.828 | 0.994037 | 2.904029 | 5 | **2.904029** |
| 1:10 | 0.450 | 0.015 | 0.020 | 0.415 | 0.496789 | 1.451344 | 10 | **2.902689** |
| 1:20 | 0.238 | 0.010 | 0.020 | 0.208 | 0.247563 | 0.723243 | 20 | **2.892974** |
| Crude Enzyme 2 | 0.751 | 0.020 | 0.020 | 0.711 | 0.853171 | 2.492493 | 20 | **9.969973** |
| Gel pool | 0.511 | 0.010 | 0.020 | 0.481 | 0.576253 | 1.683492 | 5 | **1.683492** |

Worked, step by step, for the 1:10 level:

| Step | Working | Result |
| :--: | :--- | :--: |
| 1 | $0.450 - 0.015 - 0.020$ | $A_{\text{corr}} = 0.415$ |
| 2 | $(0.415 - 0.0023810)/0.8305714$ | $c = 0.496789$ mg/mL |
| 3 | $0.496789 \times 1.0$ | $m = 0.496789$ mg |
| 4 | $0.496789 \times 1000/342.296$ | $n = 1.451344$ µmol |
| 5 | $1.451344 \times 10/(10 \times 0.5)$ | **2.902689 U/mL** |

**The three dilutions agree within 0.4 %** — the expected spread for three independent dilutions of one sample, and good evidence the arithmetic is right. Their disagreement is also informative: the **1:20 level is least reliable**, because it contributes only 0.025 mL of original extract to the reaction and is most sensitive to the intercept term.

> These optical data are labelled "assumed values" in the source. Treat them as an illustration of the method, not as results. See S7 item 11.

---

## S6 The totals do not close

| Stage | U/mL | Volume | Total U | Yield as printed |
| :--- | --: | --: | --: | :--- |
| Extract, as printed | 2.912 | 49.8 mL | 145.0176 U | — |
| Extract, the 20 mL actually precipitated | 2.912 | 20 mL | **58.24 U** | 100 % |
| Crude Enzyme 2 | 9.988 | 10 mL | 99.88 U | 68.87 % *(on 145.02 U)* |
| Crude Enzyme 2 | 9.988 | 9.9 mL | 98.88 U | **169.7 %** *(on 58.24 U)* |
| Gel pool | 1.687 | 20 mL | 33.74 U | 34.12 % *(on 98.88 U)* |

A precipitation step cannot recover more activity than was put into it. **69 % is the plausible reading; 171 % is not.** The contradiction is arithmetic: the numerator is based on 49.8 mL of extract while the procedure precipitated only 20 mL of it. Resolve S7 items 1–3 before quoting any of these figures.

The same issue recurs with the pellet volume — "redissolve in 1 mL", "total volume 10 mL", "load 9.9 mL" appear in three different places in the source and are mutually incompatible.

---

## S7 Open questions in the source notes

| # | Issue | Conflict | Resolve |
| :--: | :--- | :--- | :--- |
| 1 | **Stage-1 extract volume** | Summary uses 49.8 mL (→ 145.02 U); the procedure precipitates only 20 mL (→ 58.24 U) | Which was processed? Yield is undefined until fixed. |
| 2 | **Crude Enzyme 2 volume** | 1 mL vs 10 mL vs 9.9 mL | Record the real value; use it in the purification table |
| 3 | **Curve intercept** | Source $b$ = 0.0017; least squares gives 0.0023810 | Use your own regression (S3.1) |
| 4 | **PBS phosphate ratio** | 10 mM Na₂HPO₄ / 1.8 mM KH₂PO₄ gives pH ≈ 7.95 unadjusted, not 7.4 | Keep 10 mM and titrate, or switch to 8 mM / 1.8 mM (S1.4) |
| 5 | **Ca²⁺ dependence** | Plant β-amylases are Ca²⁺-dependent; PBS and assay buffer are Ca²⁺-free | Add CaCl₂ to 1 mM if β-amylase is the target |
| 6 | **Dilution volumes** | "2.7 mL out of 5 mL" does not reconcile with 4 levels × 2.0 mL | 4 levels at 2.0 mL need 8.0 mL of prepared dilution |
| 7 | **Resin grade vs void** | Published native mass **209–239 kDa** (tetramer) vs **~56 kDa** subunit on SDS-PAGE. G-100 tops out at 125 kDa and would **exclude** the native enzyme. Separately, Cytiva marks **G-150 and G-200 as discontinued** | **Ask the instructor.** If tetrameric, the realistic options are **Sephacryl S-400** (what Chang et al. used) or a Superdex 200-class medium — not a Sephadex grade, since the two wide-range ones are discontinued |
| 8 | **Protein assay, resolved** | The source has no protein assay. The senior's added A₂₈₀/A₂₆₀ step (Week 3) supplies one, so U/mg **is** computable | Use the Warburg equation, `S10`. Note it assumes dilute, unbuffered-in-UV-clean solution — see `S10` |
| 9 | **Electrophoresis not in source** | No electrophoresis text exists in the notes | Confirm gel system with instructor |
| 10 | **Assay pH unsettled** | Protocol uses pH 6.8; Chang et al. report optimum **pH 5**; a 2022 study reports **pH 7.5** | **Ask the instructor.** Wrong pH changes activity several-fold |
| 11 | **Source ODs** | Labelled "assumed values" | If placeholders, S5 is an illustration only |
| 12 | **20 g and the 1:3 ratio** | 3 mL/g is thin against the 5–20 mL/g usual for plant tissue. The example implies only **≈ 8.75 U/g of tuber** — very low for a crop the USDA literature calls *"a rich source of β-amylase"* | If Extract 1 reads that low, suspect the assay, not the tissue. Run a commercial β-amylase standard on your own curve. Consider 1:5 (20 g + 100 mL). |
| 13 | **Sample volume for assay** | §3 states **0.2 / 0.1 / 0.4 mL** for stages 1–3, but §2.4 pipettes **0.5 mL** diluted enzyme and every calculation in §3 divides by **0.5** | Use **0.5 mL** throughout. The 0.2/0.1/0.4 figures are vestigial and contradict their own arithmetic |

### S7.1 On item 12 — the yield looks too low

$2.912 \ \mathrm{U/mL} \times 60\ \mathrm{mL} = 175$ U from 20 g = **8.75 U per gram of tuber**.

Sweet potato is amylase-rich (USDA ARS calls it *"a rich source of β-amylase"*), and commercial sweet potato β-amylase sells at ≥ 750 U/mg protein. The unit definitions are compatible — Sigma's β-amylase U (1 mg maltose in 3 min) converts to $2.92\ \mu\mathrm{mol}/3\ \mathrm{min} = 0.974$ of this protocol's U — so no conversion rescues the figure.

Two readings: the "assumed values" really are fabricated, or the assay is under-reading. A commercial β-amylase standard run through your own curve distinguishes them.

### S7.2 On item 7 — why resin grade matters here

Sweet potato β-amylase is reported as a **tetramer of ~55–65 kDa subunits**:

| Measurement | Value | Source |
| :--- | :--- | :--- |
| Native, by gel filtration | **209–239 kDa** | Chang et al. 1996 |
| Subunit, by crystallography | **55.88 kDa** (498 aa) | Cheong et al. 1995 |

$4 \times 55.88 = 223.5$ kDa, consistent with the gel-filtration figure. If the native enzyme is ~220 kDa, then **G-100 (4–125 kDa) excludes it entirely** and it elutes in the void alongside the aggregates you are trying to remove — which is why Chang et al. used **Sephacryl S-400** rather than a Sephadex grade.

Expected void fractions, and what they mean for where you start collecting:

| Resin | $V_0/V_t$ | $V_0$ on an 80 mL bed |
| :--- | :--- | :--- |
| G-50 | ≈ 0.33 | 26 mL |
| G-75 | ≈ 0.33–0.35 | 26–28 mL |
| G-100 | ≈ 0.375 | 30 mL |
| G-200 *(discontinued)* | ≈ 0.40 | 32 mL |

The source's 25 mL implies $V_0/V_t = 25/80 = 0.3125$, consistent with G-50/G-75 — the wrong grade if the enzyme is the tetramer.

#### How much dry resin for an 80 mL bed

Cytiva *Instructions for Sephadex Media* (17-0000-01 AB), Table 1 — approximate bed volume per gram dry:

| Gel | mL swelled per g dry | Dry resin for an 80 mL bed |
| :--- | :--: | :--: |
| G-25 | 4–6 | 13–20 g |
| G-50 | 9–11 | 7–9 g |
| G-75 | 12–15 | 5.3–6.7 g |
| **G-100** | **15–20** | **4.0–5.3 g** |
| G-150 *(discontinued)* | 20–30 | 2.7–4.0 g |
| G-200 *(discontinued)* | 30–40 | 2.0–2.7 g |

Cytiva advises using the **lowest** bed-volume factor in the range when calculating the dry mass, so plan on ~5.3 g of G-100 and treat any excess as margin.

Swelling time, Table 2:

| Gel | 20 °C | 90 °C |
| :--- | :--: | :--: |
| G-50 | 3 h | 1 h |
| G-75 | 24 h | 3 h |
| **G-100** | **72 h** | **5 h** |
| G-150 / G-200 *(discontinued)* | 72 h | 5 h |

Add enough buffer to equal the column volume plus 30 % — 80 mL bed needs about 105 mL.

The earlier figure of 20 g for this bed was wrong by roughly 4.5×, and would have swollen to 300–400 mL — far too much for the column.

### S7.3 Deviations from the source notes

Places where this protocol departs from the source files, and why:

| Source says | This protocol uses | Why |
| :--- | :--- | :--- |
| Harvest spin: **10,000 g, 10 min, ×2** | **4000 × g, 30 min, ×2** | The available rotor caps at 4000 × g. The longer time partly compensates for the lower force |
| Suspend resin in **150 mL** PBS | **~105 mL** PBS | Cytiva: column volume + 30 %. 150 mL suits a larger bed than the 80 mL actually packed |
| Screening: add 2.0 mL water **if absorbance is off-scale** | add **2.0 mL unconditionally** | The week-3 screen always runs on a 0.6 mL pre-DNS basis (`S3.4`), so the dilution is fixed by design, not by the reading |
| **2 mL** per dilution level (3 samples + 1 BE) | **2.5 mL** per level | The substrate blank needs its own 0.5 mL. Three samples + BE + BS × 0.5 mL = 2.5 mL |

Two further departures are argued in detail elsewhere: resin swelling at **90 °C for 5 h** rather than the source's 1 h (`S7.2`, Cytiva Table 2) and a **30 mL** void rather than 25 mL (`S7.2`).

---

## S8 Why the reading rules are what they are

| Rule | Reason |
| :--- | :--- |
| Keep load ≤ 2 % of $V_c$ | Above ~2 % a soft-bed Sephadex column smears and the peaks stop separating. The source's 9.9 mL on 80 mL is 12.4 %. |
| Degas immediately before packing | A degassed slurry re-absorbs air within minutes. Degassing early defeats the purpose. |
| Never let the bed dry | Air enters the bed and the column channels. Cover with buffer the moment flow stops. |
| Drain to the bed, then close the stopcock | A flat, undisturbed bed surface gives a narrow band. A disturbed or cracked surface smears the profile. |
| Collect past tube 12 if A₂₈₀ is still high | 12 × 4 mL = 48 mL past the 30 mL void ends at 78 mL = 0.975 $V_c$. A late peak would be cut off. |
| Boil DNS tubes exactly 5 min | Under-boiled reagent reads low; over-boiled drifts as the colour deepens. |
| Stagger enzyme additions | Adding to 15 tubes at once and timing the last leaves several seconds of spread at the start of a 600 s reaction — 1–2 % error before any measurement. |
| Store fractions at −20 °C, thaw on ice | β-amylase loses activity at room temperature. Never thaw at room temperature or straight from frozen. |
| Prepare starch fresh | Hydrolysed starch carries reducing ends that inflate the substrate blank. |
| Hydrate resin at 90 °C, not at room temperature | Cytiva Table 2: G-100 needs **5 h** at 90 °C against **72 h** at 20 °C. Start the bath at the top of week 1 and let it run alongside the extraction. |
| Store unused resin dry at 2–8 °C | Cytiva and Sigma both specify a preservative (0.02 % sodium azide or 20 % ethanol) for hydrated gel left standing. Without one it grows organisms — which fouls the frit and shows up as stray protein in your A₂₈₀ and stray bands on your gel. |
| One standard curve for all three stages | Curve-to-curve drift between sessions would confound the stage-to-stage comparison, which is the entire reason for measuring three times. |

---

## S9 Acceptance criteria and troubleshooting

### S9.1 Accept the run only if

| # | Criterion | Why |
| :--: | :--- | :--- |
| 1 | Standard-curve $R^2 \geq 0.98$ | Below this the slope is not constant and every downstream value is biased |
| 2 | $A_{\text{BE}} \leq 0.03$ and $A_{\text{BS}} \leq 0.03$ | High blanks mean free sugar in the extract or hydrolysed starch |
| 3 | $A_{\text{sample}}$ inside the S0–S5 range | No extrapolation |
| 4 | Triplicate spread $\leq 10 \%$ | Larger is a pipetting or timing error, not real variation |
| 5 | Reacted samples stay brown/red-brown, never green or blue | Blue-green = DNS too alkaline or under-boiled |
| 6 | Elution profile is a single symmetric peak | Two peaks mean the column was overloaded or the resin under-equilibrated |

### S9.2 Symptom → cause

| Symptom | Likely cause | Fix |
| :--- | :--- | :--- |
| No colour change after boiling | DNS expired or added to the wrong tubes | Fresh DNS; verify BE received DNS before enzyme |
| Green or blue final colour | Too alkaline, or the bath never reached 100 °C | Check bath temperature; immerse tubes to the liquid level |
| All readings identical across dilutions | Same dilution pipetted each time, or a flat curve | Re-make dilutions; confirm the standards span the range |
| Readings rise as you dilute | High blank, or the 1:20 aliquot is least reliable | Check $A_{\text{BE}}$; make 1:20 from the 1:5 stock |
| $A_{\text{BE}}$ high | Extract left warm, or starch-rich tissue degraded | Keep everything on ice; re-prepare the starch |
| $A_{\text{BS}}$ high | Starch hydrolysed in storage, or added early and left warm | Prepare starch fresh; add DNS immediately after incubation |
| Split or channelled elution peak | Air in the slurry, disturbed bed surface, or overloading | Degas properly; never drain the bed dry; keep load ≤ 2 % $V_c$ |
| High A₂₈₀ in every fraction, no peak | Load too large, or no equilibration | Reduce load to 1–2 % $V_c$; equilibrate 3 CV |
| Recovery > 100 % | Wrong volume recorded somewhere | S6 — audit the volumes before believing it |
| No band on the gel | Protein too dilute, or it ran off in the stacking gel | Load 20 µg; check the dye front stopped before the gel bottom |
| Band at ~112 kDa where ~56 expected | Dimer not fully reduced, or the gel ran too hot | Confirm β-ME in the Laemmli buffer; run cool |
| Band at ~224 kDa where ~56 expected | Native tetramer, not fully reduced | Expected — see S7.2. Run non-reducing deliberately and record both. |

---

## S10 Yield and purification formulas

$$%\ \text{yield} = \frac{\text{Total U at this stage}}{\text{Total U at the previous stage}} \times 100$$

$$\text{fold purification} = \frac{\text{specific activity at this stage}}{\text{specific activity of stage 1}}$$

$$\text{specific activity} = \frac{\text{U/mL}}{\text{mg protein/mL}} = \text{U/mg}$$

Specific activity is computed from the senior's added A₂₈₀/A₂₆₀ reading (Week 3, Protein Quantification):

$$\text{Protein (mg/mL)} = 1.55\,A_{280} - 0.77\,A_{260}$$

$$\text{Specific activity (U/mg)} = \frac{\text{U/mL}}{\text{Protein (mg/mL)}}$$

That makes fold purification reportable too, so `S7` item 8 is closed. Two caveats. The Warburg–Christian coefficients assume **dilute** solution and **low ionic strength** — both wrong for a 137 mM NaCl extract, so treat the absolute mg/mL as approximate and lean on the ratio. And A₂₆₀ is the absorbance of nucleotides and other aromatic contaminants, which tuber extract has plenty of; a ratio well below 1.7 points to contamination rather than purity.

> **Resolve `S7` items 1 and 2 before quoting any yield.** The source divides a total of 145.02 U (computed on a 49.8 mL extract) by a stage-1 total its own procedure says came from only **20 mL**. Against the 20 mL actually processed the same numbers give **171 %** — impossible, and a direct signal one of the two volumes is wrong. Take the denominator from the volume you actually precipitated.

---

## S11 Session time budget

| Session | Work | Hands-on | Block |
| :--: | :--- | --: | --: |
| **P1** | Safety · weigh resin, store dry · PBS 4 L · assay buffer · maltose · DNS · saturated (NH₄)₂SO₄ overnight · chill mortar | **1.25 h** | 5 h |
| **Week 1** | Start resin bath (5 h, unattended) · grind 20 g / 60 mL · filter · 20.0 mL aliquot · add 46.66667 mL sat. salt · 2 × 4000 × g / 10 min · redissolve 1.0 mL · load dialysis bag into 200 mL PBS (1:200) · change at 2 h and 4 h | **3.50 h** | 5 h |
| **Week 2** | Harvest at 6 h · clarify 2 × 4000 × g / 30 min · decant fines · degas 15–20 min · pack 80 mL · equilibrate 160–240 mL · clarify · load 1.0–1.6 mL · elute void + 12 × 4.0 mL · freeze | **≈ 4.0 h** | 5 h |
| **Week 3** | Starch batch A · A₂₈₀ all fractions · cast + load gel, start run · screen while it runs · plot · pool peak · fix and stain | **≈ 3.5 h** | 5 h |
| **Week 4** | Starch batch B · one curve for all three stages · screen Extract 1 only · selected level on stages 2 and 3 · calculate · destain and image | **≈ 2.5 h** | 5 h |
| **Week 5** | Reserve — re-run failures, finish the report | — | — |

**Why the gel sits in week 3.** Carrying the quantitative DNS *and* the whole electrophoresis in week 4 times out at ≈ 7.1 h, well over the block. Two changes fix it: the 1.5–2 h gel run is unattended and overlaps the fraction screening, and screening four dilution levels on Extract 1 only cuts the reaction count from 60 tubes to 30.

**Forced boundaries.** Dialysis runs overnight; elution is 32–50 min of continuous drainage; DNS boiling batches are serial; the cold chain cannot be split across two days. Week 5 is spare, not a rescue slot.

---

## S12 References

Every DOI below was resolved against Crossref or the publisher record. Items marked **no DOI** are cited in full because the source genuinely has none — see the note beneath the list.

### Assay chemistry and activity definition

- Miller, G. L. (1959). Use of dinitrosalicylic acid reagent for determination of reducing sugar. *Analytical Chemistry* 31(3), 426–428. <https://doi.org/10.1021/ac60147a030> — the DNS reaction, 540 nm endpoint, and the standard-curve procedure in `S3`.
- Bernfeld, P. (1955). Amylases, α and β. *Methods in Enzymology* 1, 149–158. <https://doi.org/10.1016/0076-6879(55)01021-5> — the activity unit and the α/β distinction behind `S4`.
- Nelson, N., Cox, J. D., Lowe, C. V. (1957). A photometric method for measuring the breakdown of certain pyrazolamines. *Journal of Biological Chemistry* 228, 496–499. **no DOI**

### Sweet potato β-amylase

- Balls, A., Walden, M., Thompson, R. (1948). A crystalline β-amylase from sweet potatoes. *Journal of Biological Chemistry* 173, 9–19. <https://doi.org/10.1016/s0021-9258(18)35550-9> — the founding characterisation of the enzyme.
- Chang, C. T., Liou, H. Y., Tang, H. L., Sung, H. Y. (1996). Activation, purification and properties of β-amylase from sweet potatoes (*Ipomoea batatas*). *Agricultural and Biological Chemistry* 50, 201–208. **no DOI** — native mass 209 kDa (Tainung No. 57) and 239 kDa (Chailai) by gel filtration; optimum pH 5, 50 °C; (NH₄)₂SO₄ fractionation then **Sephacryl S-400**; yields 73–76 %. Source of every claim in `S7` item 7, `S7.2` and `S7` item 10.
- Cheong, C. G., Eom, S. H., Chang, C., Shin, D. H., Song, H. K., Min, K., Moon, J. H., Kim, K. K., Hwang, K. Y., Suh, S. W. (1995). Crystallization, molecular replacement solution, and refinement of tetrameric beta-amylase from sweet potato. *Proteins* 21(2), 105–117. <https://doi.org/10.1002/prot.340210204> — **tetramer of identical subunits, 222 symmetry; subunit 498 aa, Mr 55,880.** PDB **1FA2** (<https://doi.org/10.2210/pdb1FA2/pdb>). This is the primary source for the subunit figure in `S7.2`.
- Teotia, S., Khare, S., Gupta, M. (2001). An efficient purification process for sweet potato beta-amylase by affinity precipitation with alginate. *Enzyme and Microbial Technology* 28, 792–795. <https://doi.org/10.1016/s0141-0229(01)00338-6>

### Chromatography media

- Cytiva. *Instructions for Sephadex Media*, document **17-0000-01 AB**. <https://www.cytivalifesciences.co.jp/tech_support/manual/pdf/17000001.pdf> — **no DOI** (technical manual). Source of Table 1 bed-volume factors, Table 2 swelling times (G-100: 72 h at 20 °C, **5 h at 90 °C**), the "choose the lowest bed-volume factor" rule, the "column volume plus 30 %" swelling rule, and storage conditions. All quoted in `S7.2` and `S8`.
  - ⚠ **Table 1 note: Sephadex G-150, G-150 SF, G-200 and G-200 SF are discontinued products.** This constrains `S7` item 7 — see below.
- Sigma-Aldrich. *Sephadex G-25 product sheet.* **no DOI** — antimicrobial agent required for stored hydrated gel (`S8`).

### Electrophoresis

- Laemmli, U. K. (1970). Cleavage of structural proteins during the assembly of the head of bacteriophage T4. *Nature* 227(5259), 680–685. <https://doi.org/10.1038/227680a0> — the discontinuous SDS-PAGE system used in Week 3.

### Context

- USDA ARS. *Sweetpotato bibliography.* <https://www.ars.usda.gov/southeast-area/raleigh-nc/fsmqhru/docs/sweetpotato-bibliography> — **no DOI**. Source of "rich source of β-amylase" quoted in `S7` item 12.
- Megazyme. *Ceralpha* and *Betamyl-3* assay manuals. **no DOI** — extraction ratios for cereal and malt β-amylase, used only for the range in `S7` item 12.
- Course notes: `PROTOCOL LAB.docx`, `PROTOCOL LAB.txt`, `DNS METHOD TO DETERMINE ENZYME ACTIVITY.txt`.

### Why some items have no DOI

Four entries predate or fall outside DOI registration and were not found in Crossref:

| Reference | Reason |
| :--- | :--- |
| Nelson, Cox & Lowe 1957 | *J. Biol. Chem.* predates DOI registration; not in Crossref |
| Chang et al. 1996 | *Agric. Biol. Chem.* pre-1999 volumes are not deposited with Crossref, and J-Stage's ABC coverage for volume 50 is incomplete |
| Cytiva 17-0000-01 AB | Vendor technical manual, not a journal or book |
| USDA ARS / Sigma-Aldrich / Megazyme | Non-scholarly documents |