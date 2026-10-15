# LAB PROTOCOL — Sweet Potato Amylase: Extraction → Ammonium Sulfate → Dialysis → Gel Filtration → Electrophoresis → DNS Activity Assay

**Course:** Fundamentals in Protein & Enzyme Engineering
**Source:** `PROTOCOL LAB.txt` / `.docx`, `DNS METHOD TO DETERMINE ENZYME ACTIVITY.txt`
**Schedule:** P1 + 4 weeks × 5 h. Week 5 reserve.

> **Status:** framework only. Section headings, quantities and parameters are settled; bench steps
> are marked *TODO* and get written per session.

**Objective.** Purify amylase from sweet potato root through four stages — crude extraction,
70 % (NH₄)₂SO₄, dialysis, Sephadex — then assay each stage by DNS and check by SDS-PAGE.

## Process flow

| --- | Process | In | Out | Key parameter | Session |
| :--: | :--- | :--- | :--- | :--- | :--: |
| A | Crude extraction | 20 g tuber + 60 mL PBS | 60 mL Extract 1 | 1:3 w/v, 0–4 °C | 1 |
| B | Salt precipitation | 20 mL Extract 2 + 46.66667 mL sat. (NH₄)₂SO₄ | pellet → 1.0 mL Crude Enzyme 2 | 70 % saturation | 1 |
| C | Dialysis | 1.0 mL Crude Enzyme 2, 6–12 kDa tubing | desalted Crude Enzyme 2 | 6 h, 4 °C | 1–2 |
| D | Gel filtration | ≤ 2 mL clarified crude | 12 × 4.0 mL fractions | $V_c$ = 80 mL, gravity | 2 |
| E | DNS activity assay | 0.5 mL diluted enzyme + 0.5 mL 1 % starch | A₅₄₀ → µmol → U/mL | 37 °C, 10 min | 3–4 |
| F | Total protein, A₂₈₀ | 12 fractions + stages | A₂₈₀ elution profile | 280 nm | 3 |
| G | Electrophoresis | 10–20 µg per lane | bands at ~50–60 kDa | SDS-PAGE 12 % | 3 |

**Temperature.** Everything except the DNS boiling step stays at 0–4 °C.

---

## Materials

### Chemicals

| Reagent | Amount | Made in | Needed by |
| :--- | :--- | :--- | :--: |
| NaCl | 32.02512 g | PBS | P1 |
| KCl | 0.80514 g | PBS | P1 |
| Na₂HPO₄ anhydrous | 5.6784 g | PBS | P1 |
| KH₂PO₄ | 0.979848 g (PBS) + 3.40225 g (assay buffer) | PBS, assay buffer | P1 |
| HCl, 1 M | ≈ 11.3362836 mL | PBS | P1 |
| NaOH, 2 M | 20 mL; make 100 mL from **8 g** NaOH | DNS | P1 |
| (NH₄)₂SO₄ | **35.5 g** (buy 100 g) | Saturated solution | P1, overnight |
| Soluble starch | **2 g** — 1 g per 100 mL, fresh weeks 3 and 4 | 1 % starch | 3, 4 |
| D-maltose | **100 mg** → 100 mL of 1 mg/mL | Maltose standard | P1 |
| 3,5-Dinitrosalicylic acid | **1 g** | DNS | P1 |
| Rochelle salt | **30 g** | DNS | P1 |
| Na₂HPO₄·12H₂O | **8.9535 g** → 500 mL assay buffer | Assay buffer | P1 |
| CaCl₂ (optional, `R5` item 5) | 1 mM = **0.11098 g/L** | Assay buffer | P1 |

*Needed by: **P1** = prep session, then week numbers. `P1 → 4` means from P1 onward.*

### Electrophoresis chemicals — two 1.0 mm 10-well mini-gels

| Reagent | Amount |
| :--- | :--- |
| Acrylamide/bis 30 % (29:1) — resolving / stacking | ~8 mL (12 %) / ~2 mL (4 %) |
| Tris-HCl 1.5 M pH 8.8 / 0.5 M pH 6.8 | ~5 mL / ~1.25 mL |
| SDS / glycine | 0.2 g / 1.92 g |
| APS / TEMED | ~0.1 g fresh / ~20 µL |
| Bromophenol blue / β-ME | ~2 mg / ~0.4 mL |
| Coomassie R-250 / methanol / acetic acid | 1 g / ~500 mL / ~150 mL |
| Molecular-weight marker | 1 vial |
| Water-saturated butanol, parafilm or 5 % agarose | ~5 mL, for sealing |
| Zymogram (optional): sodium acetate pH 5.0, Triton X-100, I₂ in KCl | 1 set |

### Samples, media, consumables, equipment

| Item | Amount / specification | Session |
| :--- | :--- | :--: |
| Sweet potato tuber | 1, ≥ 100 g (use 20.0 g) | 1 |
| Sephadex G-100 / G-150 / G-200 | ~20 g dry → 80 mL settled bed | P1, 2 |
| Dialysis tubing 6–12 kDa MWCO | ~30 cm | 1 |
| Distilled water | 10 L | P1 |
| Cheesecloth | 3–4 layers, spares | 1 |
| Centrifuge tubes / microcentrifuge tubes | ~20 / ~40 | 1, 2 |
| Fraction tubes | **18**, numbered, marked at 4.0 mL | 2 |
| Reaction tubes 10–15 mL | ~60 | 3, 4 |
| Pipette tips 20/200/1000 µL | 2 boxes each | P1 → 4 |
| Mortar and pestle | **Pre-chillable, ≥ 100 mL** | 1 |
| Beakers / graduated cylinders / volumetric flasks | 50–1000 mL / 10–500 mL / 100 mL, 1 L | P1 |
| Pipettes | 100 µL, 200 µL, 1 mL, 5 mL — **calibrated** | P1 → 4 |
| Burette 50 mL + stand, magnetic stirrer, glass rod | | 1, 2 |
| Chromatography column, clamps, spirit level, desiccator + pump | ~80 mL bed, **stopcock + frit** | 2 |
| pH meter, balance to **0.0001 g**, conductivity probe (optional) | | P1, 1–2 |
| Refrigerator 4 °C, freezer −20 °C | | P1 → 4 |
| Centrifuge, 10 000 × g rotor, refrigerated | | 1, 2 |
| Spectrophotometer | **540 nm and 280 nm** | 3, 4 |
| Water baths | 37 °C, 100 °C, **90 °C for resin** | 3, 4, 1 |
| Electrophoresis tank + power supply, 1.0 mm plates, 10-well comb | | 3 |
| Staining tray, rocker, imager | | 3 |
| Gloves, goggles, chemical-waste containers | 1 each / 2 | P1 → 4 |

---

# P1 — set-up and reagents

**≈ 1.25 h plus overnight work. Do this the day before Week 1.**

- [ ] Read safety (`1`)
- [ ] Choose the Sephadex grade (`2`). **Store the powder dry at 4 °C** — hydrate in week 1 (`4`)
- [ ] Collect every reagent from the materials section
- [ ] Make **4 L** 1× PBS (`3.1`)
- [ ] Make **500 mL** assay buffer (`3.2`)
- [ ] Make **100 mL** maltose standard (`3.3`)
- [ ] Make **100 mL** DNS reagent (`3.4`)
- [ ] Make **50 mL** saturated (NH₄)₂SO₄ (`3.5`) — **overnight at 4 °C**
- [ ] Chill the mortar, pestle and a 60 mL aliquot of PBS overnight

*Do not make yet: 1 % starch (weeks 3, 4) and electrophoresis reagents (week 3).*

## 1 Safety and handling

| Hazard | Where | Control |
| :--- | :--- | :--- |
| DNS | `3.4`, weeks 3–4 | Gloves, eye protection. Irritant; do not inhale powder. |
| 2 M NaOH | `3.4` | Caustic. Add acid to water, never water to base. |
| Rochelle salt | `3.4` | Dust — weigh over a paper boat. |
| Boiling bath 100 °C | weeks 3–4 | Heat-resistant gloves; tubes flash-cool on ice. |
| (NH₄)₂SO₄ | week 1 | Dust. Ventilated area; wash hands. |
| Strong acid / base | `3.1`, `3.2` | 1 M HCl/NaOH, dropwise, probe immersed. |
| 90 °C bath | `4` | Glass vessels only; never seal a heated vessel. |
| Acrylamide, β-ME | week 3 | Hood and gloves for unpolymerised acrylamide and boiling β-ME/SDS. |
| Sweet potato | week 1 | Wash well; discard skin and discoloured tissue. |

*TODO: waste and cleanup procedure.*

## 2 Sephadex resin — choose and store

Subunit mass **50–60 kDa**; published native mass **209–239 kDa** (`R5` item 7).

| Resin | Range (globular) | Suitability | $V_0/V_t$ | $V_0$ on 80 mL bed |
| :--- | :--- | :--- | --: | --: |
| G-25 | 1–5 kDa | **Unusable** — excluded, elutes in void | — | — |
| G-50 | 1–15 kDa | **Unusable** — excluded | ≈ 0.33 | — |
| G-75 | 3–70 kDa | Marginal — at the exclusion limit | ≈ 0.33 | 28 mL |
| **G-100** | 4–125 kDa | Good for a 50–60 kDa monomer | ≈ 0.375 | 30 mL |
| G-150 / G-200 | 5–150 / 5–200 kDa | **Needed if native form is the ~220 kDa tetramer** | ≈ 0.40 | 32 mL |

**Weigh ~20 g dry resin now; store at 4 °C.** Hydrate in week 1 (`4`).

> Store unused gel dry at 2–8 °C. Hydrated gel left standing needs a preservative (0.02 % sodium azide or 20 % ethanol) or it grows organisms.

## 3 Buffers and reagents

| § | Reagent | Batch | Make in |
| :--: | :--- | :--- | :--: |
| `3.1` | 1× PBS pH 7.4 | **4 L** | P1 |
| `3.2` | Assay buffer pH 6.8 | **500 mL** | P1 |
| `3.3` | Maltose 1 mg/mL | **100 mL** | P1 |
| `3.4` | DNS reagent | **100 mL** | P1 |
| `3.5` | Saturated (NH₄)₂SO₄ | **50 mL** | P1, then overnight |
| `3.6` | 1 % soluble starch | **2 × 100 mL** | weeks 3, 4 |
| `3.7` | Electrophoresis reagents | 2 mini-gels | week 3 |

### 3.1 1× PBS, pH 7.4

Final: 137 mM NaCl, 2.7 mM KCl, 10 mM Na₂HPO₄, 1.8 mM KH₂PO₄.

$$m\;(\mathrm{g}) = c\;(\mathrm{mol\,L^{-1}}) \times V\;(\mathrm{L}) \times M\;(\mathrm{g\,mol^{-1}})$$

| Symbol | Meaning |
| :--- | :--- |
| $m$ | mass to weigh, g |
| $c$ | molarity, mol/L (137 mM = 0.137 mol/L) |
| $V$ | final volume, L |
| $M$ | molar mass of that salt form, g/mol |

| Reagent | $M$ | Calculation | 1 L | 500 mL | **4 L** |
| :--- | --: | :--- | --: | --: | --: |
| NaCl | 58.44 | 0.137 × 4 × 58.44 | 8.00628 g | 4.00314 g | **32.02512 g** |
| KCl | 74.55 | 0.0027 × 4 × 74.55 | 0.201285 g | 0.1006425 g | **0.80514 g** |
| Na₂HPO₄ anhydrous | 141.96 | 0.010 × 4 × 141.96 | 1.4196 g | 0.7098 g | **5.6784 g** |
| KH₂PO₄ | 136.09 | 0.0018 × 4 × 136.09 | 0.244962 g | 0.122481 g | **0.979848 g** |

**Hydrate warning.** 141.96 is **anhydrous**. Check your bottle:

| Form | $M$ | Per L at 10 mM | For 4 L |
| :--- | --: | --: | --: |
| anhydrous | 141.96 | 1.4196 g | 5.6784 g |
| ·2H₂O | 177.99 | 1.7799 g | 7.1196 g |
| ·7H₂O | 268.065 | 2.68065 g | 10.7226 g |
| ·12H₂O | 358.14 | 3.5814 g | 14.3256 g |

*TODO: PBS preparation steps.*

**Titrant.** The 10 mM / 1.8 mM ratio gives pH ≈ 7.95, not 7.4. With $pK_{a2}' \approx 6.8$ (at $I \approx 0.15$ M, 25 °C):

$$\frac{[\mathrm{HPO_4^{2-}}]}{[\mathrm{H_2PO_4^-}]} = 10^{\,7.4-6.8} = 3.9810717$$

$[\mathrm{HPO_4^{2-}}] = 7.1659291$ mM, so protonate $10 - 7.1659291 = 2.8340709$ mM:

$$\approx 2.8341\ \text{mL of 1 M HCl per L} \;\Rightarrow\; \mathbf{\approx 11.3362836\ \text{mL for 4 L}}$$

Estimate only. **Titrate to the measured pH, not the calculated volume.** With the classical 8 mM recipe you would need only ≈ 0.834 mL/L.

### 3.2 Assay buffer, pH 6.8

50 mM sodium phosphate. Total consumption ≈ 327 mL — make 500 mL.

| Salt | $M$ | 100 mL | **500 mL** | 1 L |
| :--- | --: | --: | --: | --: |
| Na₂HPO₄·12H₂O | 358.14 | 1.7907 g | **8.9535 g** | 17.907 g |
| KH₂PO₄ | 136.09 | 0.68045 g | **3.40225 g** | 6.8045 g |

*TODO: preparation steps.*

> **Ca²⁺.** Plant β-amylases are Ca²⁺-dependent; neither PBS nor this buffer contains it (`R5` item 5).

### 3.3 Maltose standard, 1 mg/mL

**100.0 mg** maltose ($M$ = 342.296) to **100.0 mL** assay buffer. Store at 4 °C.

### 3.4 DNS reagent

| Component | Amount | Final in 100 mL |
| :--- | --: | --: |
| 3,5-Dinitrosalicylic acid | **1 g** | 10 mg/mL |
| Rochelle salt | **30 g** | 300 mg/mL |
| NaOH, 2 M | **20 mL** | 0.4 M delivered |
| Water | to 100 mL | — |

*TODO: preparation steps. Working colour is deep red-brown; store amber at RT, dark.*

### 3.5 Saturated (NH₄)₂SO₄ — overnight, 4 °C

Solubility ≈ 71 g/100 mL water at 0–4 °C.

$$m = V \times \frac{S}{100} = 50 \times \frac{71}{100} = \mathbf{35.5\ \text{g}}$$

You need 46.66667 mL (`6`) — 50 mL is the right batch. Undissolved crystals at 4 °C confirm saturation; do not filter them out.

### 3.6 1 % soluble starch — weeks 3 and 4, not now

Two 100 mL batches, 1 g starch each, in assay buffer. Heat to 80–90 °C to gelatinise. **Use the same day** — hydrolysed starch inflates the substrate blank.

*TODO: preparation steps.*

### 3.7 Electrophoresis reagents

| Reagent | Recipe | Storage |
| :--- | :--- | :--: |
| 4× Laemmli sample buffer | 250 mM Tris-HCl pH 6.8, 20 % (v/v) glycerol, 4 % (w/v) SDS, 0.004 % (w/v) bromophenol blue, 10 % (v/v) β-ME | 4 °C, fresh weekly |
| 1× running buffer | 25 mM Tris, 192 mM glycine, 0.1 % (w/v) SDS. **Do not adjust pH** | RT |
| 12 % resolving gel, 1.0 mm, 10-well | 375 mM Tris-HCl pH 8.8, 12 % acrylamide/bis (29:1), 0.1 % APS, 0.1 % TEMED | cast week 3 |
| 4 % stacking gel, 1.0 mm | 125 mM Tris-HCl pH 6.8, 4 % acrylamide/bis, 0.1 % APS, 0.1 % TEMED | cast week 3 |
| Coomassie stain | 0.1 % (w/v) R-250 in 40 % methanol, 10 % acetic acid | RT, re-usable |
| Destain | 10 % acetic acid, 40 % methanol | RT, re-usable |

---

# Week 1 — Extraction, precipitation, dialysis setup

**3.50 h.** Ends with dialysis running overnight.

- [ ] Hydrate the Sephadex in the 90 °C bath (`4`) — it runs while you grind
- [ ] Grind and filter 20 g tuber → 60 mL Extract 1 (`5`)
- [ ] Take the 20.0 mL Extract 2 aliquot (`5`)
- [ ] Calculate the salt volume (`6`)
- [ ] Add saturated salt in 5 stages (`7`)
- [ ] Centrifuge, redissolve the pellet (`8`)
- [ ] Load the dialysis bag (`9`)

## 4 Materials and resin hydration

- [ ] Pre-chill mortar, pestle and a 60 mL aliquot of PBS
- [ ] Hydrate ~20 g dry Sephadex in 150 mL PBS, **90 °C bath 1 h** (replaces 3–6 h at RT), then hold at 4 °C
- [ ] Wash, peel, discard discoloured tissue, cut ~5 mm cubes. Weigh **exactly 20.0 g**. Keep on ice

## 5 Grinding and filtration — Extract 1

*TODO: bench steps.*

| Quantity | Value |
| :--- | :--- |
| 30 mL cold PBS to grind + 30 mL to rinse = **60 mL** total | |
| Recovered Extract 1 volume (mL) | |
| Colour | |
| Grinding → freezing (min) | |

> **Naming.** Combined filtrate = **Extract 1**; the 20.0 mL portion taken for precipitation = **Extract 2**. Used this way throughout. Remaining ≈ 40 mL → two aliquots at −20 °C as spare.

## 6 Calculate the volume of saturated salt

$$V_{\text{salt}} = V_0 \times \frac{S_2 - S_1}{1 - S_2} = 20 \times \frac{0.70 - 0}{1 - 0.70} = \frac{14}{0.3} = \mathbf{46.66667\ \text{mL}}$$

**Do not round to 47 mL.** 47 mL gives 0.70 × 47/67 = 0.49105, not 0.70.

| Addition | This (mL) | Cumulative | Total with extract (mL) |
| :--: | --: | --: | --: |
| 1 | 10.0 | 10.0 | 30.0 |
| 2 | 10.0 | 20.0 | 40.0 |
| 3 | 10.0 | 30.0 | 50.0 |
| 4 | 10.0 | 40.0 | 60.0 |
| 5 | **6.66667** | **46.66667** | **66.66667** |

## 7 Add the salt in stages

*TODO: bench steps.* Add slowly from a burette into the 20.0 mL aliquot on ice, stirring continuously. Stir 20–30 min after the last addition.

## 8 Centrifuge and redissolve the pellet

| Parameter | Value |
| :--- | :--- |
| Spin | **10 000 × g, 10 min, 4 °C, twice** — transfer supernatant between spins |
| Pellet mass (mg) | |
| Redissolve in | **1.0 mL** cold PBS |

> **Volume.** Source gives three: 1 mL, 10 mL, 9.9 mL loaded. Not compatible. Record what you actually used: V = __________ mL (`R5` item 2).

## 9 Load the dialysis bag

| Parameter | Value |
| :--- | :--- |
| Tubing MWCO | **6–12 kDa** — a 50–60 kDa amylase must be retained |
| External buffer | **1 L** 1× PBS, changed at **2 h, 4 h, 6 h** |
| Duration | **6 h**, overnight, 4 °C, continuous gentle stirring |

*TODO: bag preparation, leak test, loading steps.*

## 10 Week 1 record

| Quantity | Value |
| :--- | :--- |
| Tissue mass (g) | |
| Buffer: grind / rinse (mL) | |
| Extract 1 recovered volume (mL) | |
| Extract 2 aliquot (mL) | |
| Saturated salt added, total (mL) | |
| Final precipitation volume (mL) | |
| Grinding → freezing (min) | |
| Pellet mass (mg) | |
| Crude Enzyme 2 volume after redissolution (mL) | |
| Dialysis started (time) | |

---

# Week 2 — Dialysis harvest, gel filtration, fractions

**3.75 h.** Start on time — elution cannot be paused.

- [ ] Harvest the bag, clarify twice (`11`)
- [ ] Decant fines, make slurry, degas (`12`)
- [ ] Pack to $V_c$ = 80 mL, equilibrate (`13`)
- [ ] Clarify and load (`14`)
- [ ] Elute, collect 12 fractions (`15`)
- [ ] Split, label, freeze (`16`)

## 11 Finish the dialysis and harvest

*TODO: bench steps.*

| Parameter | Value |
| :--- | :--- |
| Conductivity inside bag (mS/cm) — should match PBS | |
| Recovered volume (mL) | |
| Clarification spin | **10 000 × g, 10 min, 4 °C, twice** |
| **Load activity (U/mL)** — measure before loading | |

## 12 Resin: remove fines and degas

*TODO: bench steps.*

| Parameter | Value |
| :--- | :--- |
| Fines removal | settle under gravity, decant milky supernatant |
| Slurry | **50–75 % (v/v)** in fresh PBS |
| Degas | **15–20 min** under vacuum |

## 13 Pack and equilibrate the column

*TODO: bench steps.*

| Parameter | Value |
| :--- | :--- |
| Bottom wetting | **10 mL** degassed PBS |
| Bed volume $V_c$ | **80 mL**; record settled height |
| Fines wash | **160 mL** (2 CV), discarded |
| Equilibration | **160–240 mL** (2–3 CV), until effluent pH and A₂₈₀ are stable |

## 14 Prepare and load the sample

*TODO: bench steps.*

| Parameter | Value |
| :--- | :--- |
| Clarify | **4000 × g, 15–20 min, 4 °C**, or 0.45 µm low-protein-binding filter |
| Clarified volume (mL) | |
| **Load volume** | **1.0–2.0 mL** (1.25–2.5 % of $V_c$), onto the bed centre |

> **Load size.** Source summary claims 9.9 mL = 12.4 % of the bed — far above the 1–2 % that gives usable resolution. To process the whole sample, run the column several times and pool fractions (`R5` items 1–2).

## 15 Elute and collect

*TODO: bench steps.*

| Parameter | Value |
| :--- | :--- |
| Flow rate | **1–2 mL/min** — record |
| Void $V_0$ discarded | 28 mL (G-75) / 30 mL (G-100) / 32 mL (G-200) |
| Fractions | **4.0 mL × 12**; cumulative after tube *n* = $V_0 + 4n$ |
| Continue past tube 12? | if A₂₈₀ still above baseline, go to ≈ 96 mL (tube 18) |

> Eluting 48 mL at 1.5 mL/min takes ~32 min continuous. Mark tube positions on the column.

## 16 Split, label, store

- [ ] Split each fraction into two labelled aliquots: one for A₂₈₀ and DNS (`18`, `19`), one spare
- [ ] Freeze both at −20 °C if analysing later; **thaw on ice**, never at room temperature
- [ ] Complete the elution log (`R2.1`)

## 17 Week 2 record

| Quantity | Value |
| :--- | :--- |
| Resin grade, lot, dry mass (g) | |
| Settled bed volume / height | |
| Equilibration volume (mL) | |
| Effluent pH / A₂₈₀ | |
| Void discarded $V_0$ (mL) | |
| Flow rate (mL/min) | |
| Clarified load volume (mL) | |
| Load activity (U/mL) | |
| Fractions collected | |

---

# Week 3 — Screening, electrophoresis, pooling

**≈ 3.5 h.** Start the gel first, then screen while it runs.

- [ ] **Make starch batch A** (`3.6`)
- [ ] Read A₂₈₀ on all fractions (`18`)
- [ ] Cast and load the gel, **start the run** (`21`, `22`)
- [ ] *Gel runs ~1.5 h unattended — screen while it runs*
- [ ] Build the 0.6 mL-basis screening curve (`19`)
- [ ] Run the screening DNS on all fractions (`19`)
- [ ] Plot the profile, pool the peak (`20`)
- [ ] Stop the gel, fix and stain (`23`)

## 18 A₂₈₀ of the fractions

- [ ] Thaw aliquots **on ice**
- [ ] Read A₂₈₀ for every fraction, blanked against **the same PBS used to equilibrate the column**
- [ ] Estimate $c$ (mg/mL) ≈ A₂₈₀ × 2. **Rough only** — without a protein assay (`R5` item 8) absolute protein and **U/mg cannot be measured**. Relative comparison only
- [ ] Record in `R2.1`

## 19 Screening DNS assay on the fractions

**Different format from week 4. Do not mix the numbers.**

| Component | Volume |
| :--- | --: |
| Fraction | **0.1 mL** |
| 1 % starch | **0.5 mL** |
| DNS, after incubation | **1.0 mL** |
| Water, after boiling | **2.0 mL** |
| Pre-DNS reaction volume | **0.6 mL** |
| Final volume | **3.6 mL** |

**Screening curve on a 0.6 mL pre-DNS basis:**

| Tube | Maltose (mL) | Buffer (mL) | Pre-DNS | DNS | Water | A₅₄₀ |
| :--- | --: | --: | --: | --: | --: | --: |
| S0 | 0 | 0.60 | 0.60 | 1.0 | 2.0 | __________ |
| S1 | 0.12 | 0.48 | 0.60 | 1.0 | 2.0 | __________ |
| S2 | 0.24 | 0.36 | 0.60 | 1.0 | 2.0 | __________ |
| S3 | 0.36 | 0.24 | 0.60 | 1.0 | 2.0 | __________ |
| S4 | 0.48 | 0.12 | 0.60 | 1.0 | 2.0 | __________ |
| S5 | 0.60 | 0 | 0.60 | 1.0 | 2.0 | __________ |

*Same temperature and time: 37 °C, 10 min, boil 5 min, read 540 nm. TODO: bench steps.*

> 1. **Standards must be at 0.6 mL pre-DNS.** Reusing the week-4 curve (1.0 mL basis) on a 0.6 mL reaction inflates results by $1.0/0.6 = 1.66667$.
> 2. **Not comparable to week 4.** Screen runs 1.67 % starch, week 4 runs 50 %. **The screen ranks fractions; only `26` is reportable.**

**Calculate** with `R1`, using $V_{\text{total, pre-DNS}}$ = 0.6 mL (step 3) and $V_{\text{enzyme}}$ = 0.1 mL (step 5):

$$\text{U/mL (screen)} = \frac{n_{\mu\mathrm{mol}} \times DF}{10 \times 0.1}$$

## 20 Plot the profile and select the peak

- [ ] Plot **A₂₈₀** and **screen U/mL** against cumulative elution volume (`R2.1`)
- [ ] Identify the peak. **One symmetric peak is the pass criterion**; two mean overload or under-equilibration
- [ ] **Pool** fractions ≥ 50 % of maximum A₂₈₀. Pooled volume: __________ mL — this is the **Gel pool**
- [ ] Keep on ice for week 4, or freeze at −20 °C and thaw on ice

## 21 Cast the SDS-PAGE gel

Standard Laemmli workflow — not in the source notes (`R5` item 9).

*TODO: casting, sample preparation, loading steps.*

| Parameter | Value |
| :--- | :--- |
| Gel | 12 % resolving + 4 % stacking, **1.0 mm, 10-well** |
| Pre-run | **100 V, 15 min** |
| Sample load | **10–20 µg per lane**; 4 volumes sample : 1 volume 4× Laemmli |
| Heating | **95 °C, 5 min** |

| Lane | Content | Lane | Content |
| :--: | :--- | :--: | :--- |
| 1 | Molecular-weight marker | 6 | Crude Enzyme 2 |
| 2 | Extract 1 | 7 | Fraction, highest A₂₈₀ |
| 3 | Extract 1 | 8 | Fraction, next |
| 4 | (blank / buffer) | 9 | Fraction, last collected |
| 5 | (NH₄)₂SO₄ pellet, redissolved | 10 | Peak fraction |

> Pooling happens at `20`, after the gel is running. Lane 10 carries the peak fraction.

## 22 Run the gel

| Parameter | Value |
| :--- | :--- |
| Stacking | **70 V** until the dye front clears the gel (20–30 min) |
| Resolving | **120 V** until the front is ~1 cm from the bottom (60–90 min) |
| Total | **≈ 1.5–2 h**, unattended |
| Temperature | run at 4 °C if it runs hot — heat distorts band positions |

*TODO: bench steps.*

## 23 Stain and image

| Parameter | Value |
| :--- | :--- |
| Fix | **40 % methanol / 10 % acetic acid, 1 h** |
| Stain | Coomassie R-250, **1 h**, rocking |
| Destain | 10 % acetic acid / 40 % methanol, **1–3 h to overnight** |
| Main band (kDa) | __________ |

| Gel | Answers | Expected |
| :--- | :--- | :--- |
| SDS-PAGE, reducing | Species remaining? Subunit mass? | one dominant band **~50–60 kDa**, weaker bands thinning stage to stage |
| SDS-PAGE, non-reducing | Oligomeric state? | extra band near **~220 kDa** if tetrameric (`R5` item 7) |
| Native PAGE | Oligomeric state | 1–2 bands, higher apparent mass |
| Starch zymogram | Which band is active? | transparent zones over the amylase band |

*TODO: zymogram procedure — cast with 0.5–1 % starch, wash in 50 mM sodium acetate pH 5.0 + 0.2 % Triton X-100, incubate 37 °C 1–2 h, stain 1 % I₂ in 1 M KCl.*

---

# Week 4 — Quantitative DNS on all three stages

**≈ 2.5 h.**

**Assay all three stages in this one session, against one standard curve.** Comparing stages is the purpose; separate curves would confound the comparison.

- [ ] **Make starch batch B** (`3.6`)
- [ ] Build the standard curve — **one curve, all three stages** (`24`)
- [ ] Dilution screen on **Extract 1 only** (`25`)
- [ ] Re-run the selected level on Crude Enzyme 2 and Gel pool (`26`)
- [ ] Calculate all three, fill `R2.3`
- [ ] Destain and image the week-3 gel

## 24 Standard curve — 1.0 mL basis

| Tube | Maltose (mL) | Buffer (mL) | $C$ (mg/mL) | DNS | Water after boiling | A₅₄₀ |
| :--- | --: | --: | --: | --: | --: | --: |
| S0 (blank) | 0 | 1.0 | 0 | 1.0 | 8.0 | __________ |
| S1 | 0.2 | 0.8 | 0.2 | 1.0 | 8.0 | __________ |
| S2 | 0.4 | 0.6 | 0.4 | 1.0 | 8.0 | __________ |
| S3 | 0.6 | 0.4 | 0.6 | 1.0 | 8.0 | __________ |
| S4 | 0.8 | 0.2 | 0.8 | 1.0 | 8.0 | __________ |
| S5 | 1.0 | 0 | 1.0 | 1.0 | 8.0 | __________ |

*TODO: boil 5 min, cool on ice, add 8.0 mL water, read 540 nm, zero on S0.*

> **Standards and samples must match exactly:** 1.0 mL pre-DNS + 1.0 mL DNS + 8.0 mL water = 10.0 mL. This is why $x$ reads directly as mg maltose per mL of reaction.

**Fit** A₅₄₀ = $a\,x + b$:

| | Reference | Yours |
| :--- | --: | --: |
| $a$ | 0.8305714 | __________ |
| $b$ | 0.0023810 | __________ |
| $R^2$ | 0.99992317 | __________ |

**Accept $R^2 \geq 0.98$.** If S5 reads above A = 2.0–2.5, reduce the top standard and rebuild. **Never extrapolate beyond S5.**

> Source quotes $b$ = 0.0017. Least squares on its own six points gives **0.0023810** (`R5` item 3).

## 25 Dilution screen

Screen the four levels on **Extract 1 only**, then apply the selected level to the other two stages.

| Level | Extract (µL) | Buffer (µL) | Total | $DF$ | Transforms | A₅₄₀ |
| :--- | --: | --: | --: | --: | :--- | --: |
| Neat | 2000 | 0 | 2000 | 1 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |
| 1:5 | 400 | 1600 | 2000 | 5 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |
| 1:10 | 200 | 1800 | 2000 | 10 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |
| 1:20 | 100 | 1900 | 2000 | 20 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |

Each level needs **2.0 mL**; prepare **2.5 mL** each. Keep on ice, use the same session.

> **Make 1:20 from the 1:5 stock:** 500 µL of 1:5 + 1500 µL buffer. A single 100 µL → 1900 µL step puts only 0.025 mL of original extract in the reaction, and pipetting error is a significant fraction of that. $DF$ is still 20.

**Selection rule.** Use the most dilute level whose corrected A₅₄₀ falls **strictly inside** S0–S5. If 1:20 exceeds S5, extend to 1:40 or 1:80. **Never report an off-scale reading.**

## 26 Quantitative DNS reaction

| Tube | 1 % starch | Buffer | Diluted enzyme | DNS | When |
| :--- | --: | --: | --: | --: | :--- |
| **Sample** (× 3) | 0.5 mL | 0 | 0.5 mL | 1.0 mL | **after** incubation — stops the reaction |
| **Blank enzyme** (BE) | 0.5 mL | 0 | 0.5 mL | 1.0 mL | **before** enzyme — zero time |
| **Blank substrate** (BS) | 0.5 mL | 0.5 mL | 0 | 1.0 mL | **after** incubation |

**Tubes this session:** 4 levels × Extract 1 (20) + 1 level × Crude Enzyme 2 (5) + 1 level × Gel pool (5) = **30**. Add a full screen back only if a reading is off-scale.

*TODO: bench steps. Sequence: starch → pre-equilibrate 5 min at 37 °C → DNS to BE only → add enzyme, staggered, start timer → 10 min exactly → DNS to samples and BS → boil 5 min → ice cool → +8.0 mL water → read against S0.*

**Calculate** — full chain in `R1`. Record in `R2.2`.

## 27 Week 4 record

| Quantity | Value |
| :--- | :--- |
| Curve $a$ / $b$ / $R^2$ | |
| Level from the Extract 1 screen | |
| Level for Crude Enzyme 2 / Gel pool | |
| Extract 1 (U/mL) and total (U) | |
| Crude Enzyme 2 (U/mL) and total (U) | |
| Gel pool (U/mL) and total (U) | |
| Yield at each step (%) | |
| Main band, reducing (kDa) | |
| Main band, non-reducing / native (kDa) | |

---

# Reference

## R1 Calculation chain

**1 U** = the enzyme releasing **1 µmol reducing sugar (as maltose) per minute** at 37 °C, at the optimum pH.

**Step 1 — blank-corrected absorbance**

$$A_{\text{corr}} = A_{\text{sample}} - A_{\text{BE}} - A_{\text{BS}}$$

**Step 2 — concentration from the curve** (mg/mL of pre-DNS reaction mixture)

$$c = \frac{A_{\text{corr}} - b}{a}$$

**Step 3 — mass of sugar produced** (mg)

$$m = c \times V_{\text{total, pre-DNS}}$$

Week 4: $V_{\text{total, pre-DNS}}$ = 1.0 mL, so $m = c$. Screen: 0.6 mL, so $m = 0.6c$.

**Step 4 — micromoles**, $M$(maltose) = **342.296 g/mol**

$$n_{\mu\mathrm{mol}} = \frac{m \times 1000}{342.296}$$

**Step 5 — volumetric activity** (U per mL of the original undiluted sample)

$$\boxed{\ \text{U/mL} = \frac{n_{\mu\mathrm{mol}} \times DF}{t \times V_{\text{enzyme}}} = \frac{n_{\mu\mathrm{mol}} \times DF}{10 \times 0.5}\ }$$

**Step 6 — total activity**

$$\text{Total U} = (\text{U/mL}) \times V_{\text{stage}}$$

> **Most common error:** dividing by 1.0 mL instead of 0.5 mL in step 5. 1.0 mL is the *reaction* volume (step 3); 0.5 mL is the *enzyme* volume (step 5). Swapping them doubles every result.

| Symbol | Meaning |
| :--- | :--- |
| $a$, $b$ | slope and intercept, A₅₄₀ = $ax + b$ |
| $A_{\text{BE}}$ | **enzyme blank** — sugar already in the extract; DNS added *before* enzyme, a true zero-time control |
| $A_{\text{BS}}$ | **substrate blank** — reducing sugar inherent to the starch |
| $DF$ | dilution factor; back-corrects to the original sample |
| $V_{\text{enzyme}}$ | volume of **diluted** enzyme in the reaction, mL |
| $V_{\text{total, pre-DNS}}$ | total liquid before DNS, mL |

**Error budget.** $\mathrm{d}c/\mathrm{d}A = 1/a = 1.2039904$ mg/mL per absorbance unit. **± 0.002 A₅₄₀ = ± 0.002408 mg/mL**, about ± 0.48 % at $c$ ≈ 0.5 mg/mL. Report to **four significant figures**; carry $a$, $b$ and the saturation volumes at full precision.

## R2 Worksheets

### R2.1 Elution log

| Fraction | Cumulative (mL) | Colour | A₂₈₀ | A₅₄₀ screen | Screen U/mL | Note |
| :--: | --: | :--- | --: | --: | --: | :--- |
| 1–12 | | | | | | |
| 13+ | | | | | | *(continue if A₂₈₀ still high)* |

### R2.2 DNS worksheet — one block per dilution level

| | 1:5 | 1:10 | 1:20 | Other |
| :--- | --: | --: | --: | --: |
| A₅₄₀ sample 1 / 2 / 3 | | | | |
| $A_{\text{sample}}$ = mean | | | | |
| $A_{\text{BE}}$ | | | | |
| $A_{\text{BS}}$ | | | | |
| $A_{\text{corr}}$ (step 1) | | | | |
| $c$ (mg/mL) (step 2) | | | | |
| $m$ (mg) (step 3) | | | | |
| $n$ (µmol) (step 4) | | | | |
| **U/mL** (step 5) | | | | |

### R2.3 Purification summary

| | Extract 1 | Crude Enzyme 2 | Gel pool |
| :--- | --: | --: | --: |
| Total volume (mL) | | | |
| Dilution factor used | | | |
| $A_{\text{sample}}$ (mean) | | | |
| $A_{\text{BE}}$ | | | |
| $A_{\text{BS}}$ | | | |
| $A_{\text{corr}}$ | | | |
| $c$ (mg/mL) | | | |
| $n$ (µmol) | | | |
| **Volumetric activity (U/mL)** | | | |
| **Total activity (U)** | | | |
| **Yield (%)** | 100 | | |
| A₂₈₀ | | | |
| Protein (mg/mL) | *(estimate)* | *(estimate)* | *(estimate)* |
| **Specific activity (U/mg)** | *(n/a)* | *(blank)* | *(blank)* |
| **Fold purification** | 1.00 | | |
| Main band (kDa) | | | |

$$%\ \text{yield} = \frac{\text{Total U, this stage}}{\text{Total U, previous stage}} \times 100 \qquad \%\ \text{purification} = \frac{\text{spec. act., this stage}}{\text{spec. act., stage 1}}$$

> Resolve `R5` items 1–2 before filling in any yield.

## R3 Reference calculations

$a$ = 0.8305714, $b$ = 0.0023810, $M$ = 342.296, $t$ = 10 min, $V_{\text{enzyme}}$ = 0.5 mL, $V_{\text{total}}$ = 1.0 mL.

| Sample | $A_{\text{sample}}$ | $A_{\text{BE}}$ | $A_{\text{BS}}$ | $A_{\text{corr}}$ | $c$ (mg/mL) | $n$ (µmol) | $DF$ | **U/mL** |
| :--- | --: | --: | --: | --: | --: | --: | --: | --: |
| 1:5 | 0.868 | 0.020 | 0.020 | 0.828 | 0.994037 | 2.904029 | 5 | **2.904029** |
| 1:10 | 0.450 | 0.015 | 0.020 | 0.415 | 0.496789 | 1.451344 | 10 | **2.902689** |
| 1:20 | 0.238 | 0.010 | 0.020 | 0.208 | 0.247563 | 0.723243 | 20 | **2.892974** |
| Crude Enzyme 2 | 0.751 | 0.020 | 0.020 | 0.711 | 0.853171 | 2.492493 | 20 | **9.969973** |
| Gel pool | 0.511 | 0.010 | 0.020 | 0.481 | 0.576253 | 1.683492 | 5 | **1.683492** |

The three dilutions agree within **0.4 %**. The 1:20 level is least reliable — only 0.025 mL of original extract per reaction, most sensitive to the intercept.

**Standard curve reference:** S0–S5 at 0, 0.168, 0.340, 0.500, 0.666, 0.832 →
$A_{540} = 0.8305714\,x + 0.0023810$, $R^2$ = 0.99992317.

**Totals — these do not close:**

| Stage | U/mL | Volume | Total U | Yield as printed |
| :--- | --: | --: | --: | :--- |
| Extract, as printed | 2.912 | 49.8 mL | 145.0176 U | — |
| Extract, the 20 mL precipitated | 2.912 | 20 mL | **58.24 U** | 100 % |
| Crude Enzyme 2 | 9.988 | 10 mL | 99.88 U | 68.87 % *(on 145.02 U)* |
| Crude Enzyme 2 | 9.988 | 9.9 mL | 98.88 U | **169.7 %** *(on 58.24 U)* |
| Gel pool | 1.687 | 20 mL | 33.74 U | 34.12 % *(on 98.88 U)* |

A precipitation step cannot recover more than goes in. **69 % is plausible; 171 % is not.**

## R4 Acceptance and troubleshooting

**Accept only if:** $R^2 \geq 0.98$ · $A_{\text{BE}} \leq 0.03$ and $A_{\text{BS}} \leq 0.03$ ·
$A_{\text{sample}}$ inside S0–S5 · triplicate spread $\leq 10 \%$ · brown/red-brown colour, never
green or blue · single symmetric elution peak.

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| No colour after boiling | DNS expired or added to wrong tubes | Fresh DNS; check BE got DNS before enzyme |
| Green or blue | Too alkaline, or bath below 100 °C | Check bath temperature |
| Identical readings across dilutions | Same dilution each time, or flat curve | Re-make dilutions |
| Readings rise as you dilute | High blank, or unreliable 1:20 | Check $A_{\text{BE}}$; make 1:20 from 1:5 |
| $A_{\text{BE}}$ high | Extract left warm | Keep on ice |
| $A_{\text{BS}}$ high | Hydrolysed starch | Prepare fresh; add DNS immediately after incubation |
| Split / channelled peak | Air in slurry, disturbed bed, overload | Degas properly; never drain dry; load ≤ 2 % $V_c$ |
| High A₂₈₀ everywhere | Load too large, or no equilibration | Load 1–2 % $V_c$; equilibrate 3 CV |
| Recovery > 100 % | Wrong volume recorded | `R3`, `R5` |
| No band on the gel | Protein too dilute, or ran off | Load 20 µg; check the dye front stopped |
| Band at ~220 kDa where 50–60 expected | Tetramer not fully reduced, or gel too hot | Confirm β-ME in the Laemmli buffer; run cool |

**Waste.** (NH₄)₂SO₄, DNS and Coomassie/destain are **aqueous chemical waste**. Gloves, gel casts and electrophoresis buffer are chemical waste.

## R5 Unresolved — settle before you run

| # | Issue | Conflict | Decide |
| :--: | :--- | :--- | :--- |
| 1 | **Stage-1 extract volume** | Summary uses 49.8 mL (→ 145.02 U); procedure precipitates only 20 mL (→ 58.24 U) | Which was processed? Yield is undefined until fixed. |
| 2 | **Crude Enzyme 2 volume** | 1 mL vs 10 mL vs 9.9 mL | Record the real value; use in `R2.3` |
| 3 | **Curve intercept** | Source $b$ = 0.0017; least squares gives 0.0023810 | Use your own regression (`24`) |
| 4 | **PBS phosphate ratio** | 10 mM Na₂HPO₄ / 1.8 mM KH₂PO₄ gives pH ≈ 7.95, not 7.4 | Keep 10 mM and titrate, or switch to 8 mM / 1.8 mM |
| 5 | **Ca²⁺ dependence** | Plant β-amylases are Ca²⁺-dependent; PBS and assay buffer are Ca²⁺-free | Add CaCl₂ to 1 mM if β-amylase is the target |
| 6 | **Dilution volumes** | "2.7 mL out of 5 mL" does not reconcile with 4 × 2.0 mL | Use 2.5 mL per level (`25`) |
| 7 | **Resin grade vs void** | Published native mass **209–239 kDa** (tetramer) vs **~64 kDa** on SDS-PAGE. G-100 tops out at 125 kDa and would **exclude** the native enzyme | **Ask the instructor.** If tetrameric, use **G-200 or Sephacryl S-400** |
| 8 | **No protein assay** | Without Bradford/Lowry, U/mg cannot be computed (`18`) | Add Bradford, or report activity only |
| 9 | **Electrophoresis not in source** | `21`–`23` are a standard workflow | Confirm gel system and which gels are required |
| 10 | **Assay pH unsettled** | Protocol uses pH 6.8; Chang et al. report optimum **pH 5**; a 2022 study reports **pH 7.5** | **Ask the instructor.** Wrong pH changes activity several-fold |
| 11 | **Source ODs** | Labelled "assumed values" | If placeholders, `R3` is a worked example only |
| 12 | **20 g and 1:3 ratio** | 3 mL/g is thin against the 5–20 mL/g usual for plant tissue. The example implies only **≈ 8.75 U/g of tuber**, very low for a crop the USDA literature calls *"a rich source of β-amylase"* | If Extract 1 reads that low, suspect the assay, not the tissue. Run a commercial β-amylase standard on your own curve. Consider 1:5 (20 g + 100 mL). |

## R6 Schedule

| Session | Work | Hands-on |
| :--: | :--- | --: |
| **P1** | Safety · choose and weigh resin, store dry · PBS 4 L · assay buffer · maltose · DNS · saturated (NH₄)₂SO₄ overnight · chill mortar | **1.25 h** |
| **Week 1** | Resin into the 90 °C bath · grind 20 g / 60 mL · filter · 20.0 mL aliquot · add 46.66667 mL sat. salt in 5 stages · stir 20–30 min · 2 × 10 000 × g / 10 min · redissolve 1.0 mL · load dialysis bag into 1 L PBS | **3.50 h** |
| **Week 2** | Buffer change at 6 h · harvest · 2 × 10 000 × g · decant fines · degas 15–20 min · pack 80 mL · equilibrate 160–240 mL · clarify 4000 × g · load 1–2 mL · elute void + 12 × 4.0 mL · split, label, freeze | **3.75 h** |
| **Week 3** | Starch batch A · A₂₈₀ all fractions · **cast + load gel, start run** · screen while it runs · plot profile · pool peak · fix and stain | **≈ 3.5 h** |
| **Week 4** | Starch batch B · one standard curve for all 3 stages · screen Extract 1 only · selected level on stages 2 and 3 · calculate, fill `R2.3` · destain and image | **≈ 2.5 h** |
| **Week 5** | Reserve — re-run failures, finish the report | — |

**Forced boundaries:** dialysis runs overnight; elution is 32–50 min of continuous drainage; DNS boiling batches are serial; the cold chain cannot be split across two days.

## R7 References

- Miller, G. L. (1959). Use of dinitrosalicylic acid for reducing sugars. *Analytical Chemistry* 31(3), 426–428.
- Bernfeld, L. (1955). Amylases, carbohydrases and maltases. *Methods in Enzymology* 1, 105–128.
- Chang, C. T. et al. (1996). Activation, purification and properties of β-amylase from sweet potatoes. *Agric. Biol. Chem.* — native mass 209–239 kDa; optimum pH 5; Sephacryl S-400.
- Oktiarni, D. et al. (2015). Isolation, purification and characterization of β-amylase from sweet potato. — SDS-PAGE 64 kDa.
- Cytiva. *Instructions for Sephadex Media.* — swelling times, storage dry at 2–8 °C.
- Laemmli, U. K. (1970). Cleavage of structural proteins during heat-SDS electrophoresis. *Nature* 227, 680–685.
- USDA ARS. *Sweetpotato bibliography* — "sweet potatoes are a rich source of β-amylase."
- Course notes: `PROTOCOL LAB.docx`, `DNS METHOD TO DETERMINE ENZYME ACTIVITY.txt`.

---

## Appendix A — Quick card

```
REACTION   0.5 mL 1% starch + 0.5 mL diluted enzyme     37 °C, 10 min
THEN       + 1.0 mL DNS -> boil 5 min -> ice cool -> + 8.0 mL water -> A540
BLANKS     BE: DNS BEFORE enzyme     BS: buffer replaces enzyme
CURVE      A540 = 0.8305714 x + 0.0023810    x = mg/mL of the 1.0 mL pre-DNS mixture
STEP 1     Acorr = Asample - ABE - ABS
STEP 2     c    = (Acorr - b) / a                         [mg/mL]
STEP 3     m    = c x Vtotal_preDNS      (1.0 mL here)   [mg]
STEP 4     umol = m x 1000 / 342.296
STEP 5     U/mL = umol x DF / (10 x 0.5)   <-- 0.5 = ENZYME volume, not 1.0
STEP 6     U    = U/mL x Vstage

SCREEN     0.1 mL fraction + 0.5 mL starch; + 1.0 mL DNS; + 2.0 mL water
           rebuild standards on a 0.6 mL pre-DNS basis, or results are 1.66667x high
```

## Appendix B — Volumes

| Step | Volume | Session |
| :--- | --: | :--: |
| Extraction buffer | 30 mL grind + 30 mL rinse = **60 mL** for 20 g | 1 |
| Extract 2 | **20.0 mL** | 1 |
| Saturated (NH₄)₂SO₄ to add | **46.66667 mL** (10+10+10+10+6.66667) | 1 |
| Final precipitation volume | **66.66667 mL** | 1 |
| Pellet redissolved in | **1.0 mL** | 1 |
| Dialysis buffer | **1 L**, changed at 2, 4, 6 h | 1–2 |
| Slurry | 150 mL PBS, 50–75 % | 1, 2 |
| Bed volume $V_c$ | **80 mL** | 2 |
| Equilibration | **160–240 mL** | 2 |
| Column load | **1.0–2.0 mL** (1.25–2.5 % of $V_c$) | 2 |
| Void $V_0$ | 28 mL (G-75) / 30 mL (G-100) / 32 mL (G-200) | 2 |
| Fractions | **12 × 4.0 mL**, continue to tube 18 if needed | 2 |
| DNS reaction | 0.5+0.5 pre-DNS; +1.0 DNS; +8.0 water = **10.0 mL** | 4 |
| Screen reaction | 0.1+0.5 pre-DNS; +1.0 DNS; +2.0 water = **3.6 mL** | 3 |

---

*Compiled from `PROTOCOL LAB.docx` / `PROTOCOL LAB.txt` and `DNS METHOD TO DETERMINE ENZYME ACTIVITY.txt`. Originals unmodified in `lab/`. Values carried at full precision per `R1`; source conflicts listed in `R5`.*