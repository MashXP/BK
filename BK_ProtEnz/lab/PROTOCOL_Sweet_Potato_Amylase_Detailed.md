# LAB PROTOCOL — Sweet Potato Amylase: Extraction → Ammonium Sulfate → Dialysis → Gel Filtration → Electrophoresis → DNS Activity Assay

**Course:** Fundamentals in Protein & Enzyme Engineering
**Source material:** `PROTOCOL LAB.txt` / `.docx`, `DNS METHOD TO DETERMINE ENZYME ACTIVITY.txt`
**Vault path:** `Atlas/BK/BK_ProtEnz/lab`
**Schedule:** 4 weeks × 5 h per week · 5th week held as contingency

**Objective.** Purify amylase from sweet potato (*Ipomoea batatas*) root tissue through four
stages — crude extraction, 70 % (NH₄)₂SO₄ precipitation, dialysis and Sephadex gel filtration —
then characterise each stage by DNS reducing-sugar assay and by SDS-PAGE.

## Process flow

|  | Process | In | Out | Key parameter | Week |
| :--: | :--- | :--- | :--- | :--- | :--: |
| A | Crude extraction | 20 g tuber + 60 mL PBS | 60 mL Extract 1 | 1:3 w/v, 0–4 °C | 1 |
| B | Salt precipitation | 20 mL Extract 2 + 46.66667 mL sat. (NH₄)₂SO₄ | pellet → 1.0 mL Crude Enzyme 2 | 70 % saturation | 1 |
| C | Dialysis | 1.0 mL Crude Enzyme 2, 6–12 kDa tubing | desalted Crude Enzyme 2 | 6 h, 4 °C | 1–2 |
| D | Gel filtration | ≤ 2 mL clarified crude | 12 × 4.0 mL fractions + pooled peak | $V_c$ = 80 mL, gravity | 2 |
| E | DNS activity assay | 0.5 mL diluted enzyme + 0.5 mL 1 % starch | A₅₄₀ → µmol → U/mL | 37 °C, 10 min | 3–4 |
| F | Total protein, A₂₈₀ | 12 fractions + stages | A₂₈₀ elution profile | 280 nm | 3 |
| G | Electrophoresis | 10–20 µg per lane | bands at ~50–60 kDa | SDS-PAGE 12 % | 4 |

**Temperature rule.** Everything from tissue to assay tube except the DNS colour-development step
is held at 0–4 °C. The only deliberate excursions to 37 °C are the reaction itself and, briefly,
the resin hydration bath.

---

## Total materials for the whole protocol

One list covering all four weeks. Quantities are the totals the protocol actually consumes, so
buy with a margin for one re-run.

### Total 1× PBS requirement — 4 L

| Use | Volume |
| :--- | --: |
| Dialysis buffer, 1 L changed at 2 h, 4 h, 6 h | 3000 mL |
| Column: 10 mL bed wetting + 150 mL slurry + 160 mL fines wash + 160–240 mL equilibration + 0.5 mL wall rinse + elution (~150 mL) | 630–750 mL |
| Extraction | 60 mL |
| Contingency | 200 mL |
| **Total** | **≈ 4 L** |

Scale the PBS recipe by 4 — the volume term $V$ becomes 4 L, $c$ and $M$ stay the same:

$$m = c \times 4 \times M$$

For example, NaCl: $0.137\ \mathrm{mol/L} \times 4\ \mathrm{L} \times 58.44\ \mathrm{g/mol} = 32.02512\ \mathrm{g}$.

| Salt | Per 1 L | **For 4 L** |
| :--- | --: | --: |
| NaCl | 8.00628 g | **32.02512 g** |
| KCl | 0.201285 g | **0.80514 g** |
| Na₂HPO₄ (anhydrous) | 1.4196 g | **5.6784 g** |
| KH₂PO₄ | 0.244962 g | **0.979848 g** |
| 1 M HCl for pH 7.4 | ≈ 2.8341 mL | **≈ 11.3362836 mL** |

### Chemicals and reagents

| Reagent | Amount for the protocol | Made in | Needed by |
| :--- | :--- | :--- | :--: |
| NaCl | 32.02512 g | PBS | P2 |
| KCl | 0.80514 g | PBS | P2 |
| Na₂HPO₄ (anhydrous) | 5.6784 g | PBS | P2 |
| KH₂PO₄ | 0.979848 g (PBS) + 3.40225 g (assay buffer) | PBS, assay buffer | P2 |
| HCl, 1 M | ≈ 11.3362836 mL (plus assay buffer) | PBS, assay buffer | P2 |
| NaOH, 2 M | 20 mL for DNS; make 100 mL from **8 g** NaOH | DNS reagent | P2 |
| (NH₄)₂SO₄ | **35.5 g** used (50 mL saturated); buy 100 g | Saturated (NH₄)₂SO₄ | P2, overnight |
| Soluble starch | 1 g per 100 mL, **fresh in week 3 and week 4** → **2 g** | 1 % starch | 3, 4 |
| D-maltose | **100 mg** (100 mL of 1 mg/mL) | Maltose standard | P2 |
| 3,5-Dinitrosalicylic acid | **1 g** | DNS reagent | P2 |
| Rochelle salt (NaK tartrate) | **30 g** | DNS reagent | P2 |
| Na₂HPO₄·12H₂O (assay buffer) | 17.907 g per L → **8.9535 g** for the 500 mL batch | Assay buffer | P2 |
| KH₂PO₄ (assay buffer) | 6.8045 g per L → **3.40225 g** for the 500 mL batch | Assay buffer | P2 |
| CaCl₂ (only if resolving β-amylase) | 1 mM → **0.11098 g/L** (MW 110.98) | Assay buffer | P2 |

*"Needed by" uses session codes: **P1** = the early prep session, **P2** = the day-before session,
then the week numbers. Equipment needed from P1 onward is marked `P1 → 4`.*

### Electrophoresis chemicals (enough for two 1.0 mm, 10-well mini-gels)

| Reagent | Amount | Used in |
| :--- | :--- | :--- |
| Acrylamide/bis 30 % (29:1), **resolving** | ~8 mL (12 %) | `21` |
| Acrylamide/bis 30 % (29:1), **stacking** | ~2 mL (4 %) | `21` |
| Tris-HCl 1.5 M pH 8.8 | ~5 mL | `21` |
| Tris-HCl 0.5 M pH 6.8 | ~1.25 mL | `21` |
| SDS | 0.2 g | running buffer, gels, Laemmli |
| Glycine | 1.92 g | running buffer |
| APS (ammonium persulfate) | ~0.1 g, **fresh** | gel polymerisation |
| TEMED | ~20 µL | gel polymerisation |
| Bromophenol blue | ~2 mg | Laemmli |
| β-mercaptoethanol | ~0.4 mL | Laemmli |
| Coomassie Brilliant Blue R-250 | 1 g | stain |
| Methanol | ~500 mL | stain, destain, fixing |
| Acetic acid (glacial) | ~150 mL | stain, destain, fixing |
| **Molecular-weight marker** | 1 vial | `22` |
| Water-saturated butanol | ~5 mL | gel overlay |
| Parafilm or 5 % agarose | for sealing the cassette | `21` |
| *(Optional zymogram)* sodium acetate pH 5.0, Triton X-100, I₂ in KCl | 1 set | `23` |

### Samples and chromatography media

| Item | Amount | Week |
| :--- | :--- | :--: |
| **Sweet potato tuber** | 1 tuber ≥ 100 g (you use 20.0 g) | 1 |
| Sephadex G-100 (or G-150) | ~20 g dry → 80 mL settled bed | Pre, 2 |
| Dialysis tubing, 6–12 kDa MWCO | ~30 cm | 1 |
| Distilled / deionised water | 10 L | P1 → 4 |

### Consumables

| Item | Quantity | Week |
| :--- | :--- | :--: |
| Cheesecloth or muslin | 3–4 layers, spares | 1 |
| Centrifuge tubes, 15/50 mL | ~20 | 1, 2 |
| Microcentrifuge tubes, 1.5/2 mL | ~40 (fraction aliquots + spare) | 2–4 |
| Fraction collection tubes | **18**, numbered, marked at 4.0 mL | 2 |
| Reaction tubes, 10–15 mL | ~60 across weeks 3–4 | 3, 4 |
| Pipette tips, 20/200/1000 µL | 2 boxes each | 1–4 |
| Nitrile gloves, box | 1 | P1 → 4 |
| Goggles | 1 pair | P1 → 4 |
| Ice | ~2 bags per week | 1–4 |
| Parafilm, cling film, aluminium foil | — | P1 → 4 |
| Chemical-waste containers (aqueous + organic) | 2 | P1 → 4 |

### Glassware and hardware

| Item | Specification | Week |
| :--- | :--- | :--: |
| Mortar and pestle | **Pre-chillable, ≥ 100 mL** | 1 |
| Beakers | 50, 100, 250, 500 mL, 1000 mL | P1 → 2 |
| Graduated cylinders | 10, 50, 100, 500 mL | 1, 2 |
| Volumetric flasks | 100 mL, 1000 mL | P2 |
| Pipettes (volumetric) | 100 µL, 200 µL, 1 mL, 5 mL — **calibrated** | P1 → 4 |
| Burette, 50 mL, with stand | for staged salt addition | 1 |
| Magnetic stirrer + bars | 1–2 sets | P1 → 2 |
| Glass rod, funnel, filter paper | for gel filtration | 2 |
| Chromatography column | ~80 mL bed, **stopcock + frit**, reservoir | 2 |
| Clamps and retort stand, spirit level | for a vertical column | 2 |
| Vacuum desiccator + pump | for degassing | 2 |
| Glass rod, weighing boats, spatula | general | P1 → 4 |
| pH meter + probe | buffered before use | P2 |
| Balance readable to **0.0001 g** | for the buffer masses | P2 |
| Conductivity probe (optional) | to confirm de-salting | 1–2 |

### Equipment

| Instrument | Used for | Week |
| :--- | :--- | :--: |
| Refrigerator, 4 °C | all storage | P1 → 4 |
| Freezer, −20 °C | fractions, spare extract | 1–4 |
| Centrifuge with a 10 000 × g rotor and refrigeration | precipitation, dialysis harvest | 1, 2 |
| Spectrophotometer, **540 nm and 280 nm** | DNS assay, protein | 3, 4 |
| Water baths, thermostated | 37 °C (reaction), 100 °C (boiling) | 3, 4 |
| 90 °C bath | resin hydration | P1 |
| Electrophoresis tank, power supply, 1.0 mm plates + 10-well comb | SDS-PAGE | 4 |
| Staining tray, rocker, gel imaging (densitometer or camera + scanner) | visualisation | 4 |
| Timer / stopwatch | **every** 10 min incubation | 3, 4 |

---

# P1 — set-up and reagents

Hands-on **≈ 1.25 h**, plus unattended overnight work. Do this **the day before Week 1**.

- [ ] Read the safety table (`1`)
- [ ] Choose your Sephadex grade (`2`) — this decides the whole elution, do not guess
- [ ] Weigh ~20 g dry Sephadex G-100, **store the dry powder at 4 °C** (`2`)
- [ ] Collect every salt, sugar and chemical listed in the materials section
- [ ] Make **4 L** 1× PBS (`3.1`) — 32.02512 g NaCl, 0.80514 g KCl, 5.6784 g Na₂HPO₄, 0.979848 g KH₂PO₄, ≈ 11.3362836 mL of 1 M HCl
- [ ] Make **500 mL** assay buffer, pH 6.8 (`3.2`) — 8.9535 g Na₂HPO₄·12H₂O, 3.40225 g KH₂PO₄
- [ ] Make **100 mL** maltose standard (`3.3`) and **100 mL** DNS reagent (`3.4`)
- [ ] Make **50 mL** saturated (NH₄)₂SO₄ (`3.5`) — **overnight at 4 °C**. The source notes are
      explicit that this is a *one-day-before* preparation: it needs a night to equilibrate at 4 °C
      before it reaches saturation.
- [ ] Chill the mortar, pestle and a 60 mL aliquot of PBS overnight

**Not now** — the 1 % starch (`3.6`) is made at the start of weeks 3 and 4, and the
electrophoresis reagents (`3.7`) at the start of week 3. Both spoil or polymerise.

**Why the resin is weighed but not hydrated here.** Cytiva's instructions for Sephadex media say to
store **unused gel dry at 2–8 °C**, and to keep *hydrated* gel only with a preservative — 0.02 %
sodium azide or 20 % ethanol. A hydrated slurry sitting unazided for the week between this session
and Week 2 risks microbial growth, which fouls the frit and adds protein that shows up as a
distraction in your A₂₈₀ and as stray bands on your gel.

So the resin stays dry here and is hydrated at the **start of Week 1**, in the 90 °C bath, running
in parallel with the sweet potato grinding (`4`). One hour in the bath replaces 3–6 h at room
temperature, and you never have to store it wet.

**There is no prep session before weeks 2, 3 or 4, and there does not need to be one.** Everything
those weeks require either keeps for weeks (PBS, assay buffer, maltose, DNS — made above) or has
the opposite problem — it *must* be made in-week, because it spoils or polymerises:

| Made in-week, deliberately | Why |
| :--- | :--- |
| Resin hydration (`4`) | A hydrated gel left standing needs a preservative. Hydrating it a day before use avoids the question entirely. |
| Resin fines decant + degas + slurry (`12`) | A degassed slurry re-absorbs air. Degassing immediately before packing is the point. |
| Column packing and equilibration (`13`) | A packed bed settles and drains; it cannot be left standing for days. |
| 1 % starch (`3.6`) | Hydrolysed starch inflates the substrate blank and ruins the assay. |
| Gel casting, APS/TEMED (`21`) | Polymerise the moment they are mixed. |

Weeks 3 and 4 instead use the checklist in **Appendix C** at the start of the session.

## 1 Safety and handling

| Hazard | Where | Control |
| :--- | :--- | :--- |
| 3,5-Dinitrosalicylic acid (DNS) | DNS reagent, weeks 3–4 | Nitrile gloves, eye protection. Irritant; do not inhale powder. |
| 2 M NaOH | DNS reagent | Caustic. Add acid to water, never water to concentrated base. Gloves + goggles. |
| Rochelle salt (NaK tartrate) | DNS reagent | Bulk dust — weigh over a paper boat, not over the balance pan. |
| Boiling water bath, 100 °C | weeks 3–4 | Capped or hooded bath. Use heat-resistant gloves; tubes flash-cool on ice. |
| (NH₄)₂SO₄ | weeks 1 | Fine dust, irritant to eyes and respiratory tract. Prepare in a ventilated area; wash hands. |
| Strong acid / base | PBS, assay buffer | 1 M HCl/NaOH — add dropwise with the probe immersed. |
| Hot resin hydration bath, 90 °C | Sephadex resin | Glass vessels only; never seal a heated vessel. |
| Acrylamide, β-mercaptoethanol | week 4 | Handle unpolymerised acrylamide and boiling β-ME/SDS in the hood; gloves. |
| Sweet potato tissue | week 1 | Wash thoroughly; discard skin and any discoloured or rotted tissue. |

## 2 Sephadex resin — choose it, then hydrate it

Sweet potato amylase is a **50–60 kDa** protein (α-amylase ≈ 45–50 kDa; β-amylase is a
~55–65 kDa subunit, commonly a dimer). Resin choice decides whether it resolves at all:

| Resin | Fractionation range (globular proteins) | Suitability for a 50–60 kDa amylase |
| :--- | :--- | :--- |
| G-25 | 1–5 kDa | **Unusable** — fully excluded, elutes in the void. |
| G-50 | 1–15 kDa | **Unusable** — fully excluded. |
| G-75 | 3–70 kDa | Marginal — amylase sits at the exclusion limit, so it elutes early with poor resolution from aggregates. |
| **G-100** | 4–125 kDa | **Recommended** — well included, separates cleanly from high-MW aggregates. |
| G-150 / G-200 | 5–150 / 5–200 kDa | Acceptable; more headroom, longer runs. |

Expected void fraction $V_0/V_t$: ≈ 0.33 (G-50), ≈ 0.33–0.35 (G-75), ≈ 0.375 (G-100). **For
$V_c$ = 80 mL that gives $V_0$ ≈ 26.4–28 mL (G-75) or ≈ 30 mL (G-100).** The 25 mL void in your
source notes implies $V_0/V_t$ = 25/80 = **0.3125**, which corresponds to G-50/G-75 — the
*marginal* resin above. **If you use G-100, start collecting at 30 mL, not 25 mL**, or you lose the
front of the peak (`R5`, item 7).

**Hydration, done now so it is ready for week 2.**

1. **Weigh the dry resin.** For a settled bed of $V_c$ = 80 mL, weigh enough dry Sephadex to give
   80 mL of *settled* gel. Sephadex G-100 swells roughly 4× its dry mass, so ≈ 20 g dry — confirm
   against your bottle's swelling ratio.
2. **Hydrate** in 150 mL PBS. Swell 3–6 h at room temperature, or 1 h in a 90 °C water bath for
   standard grades (not for Superdex or agarose-based media — check the datasheet).
3. Cover and hold at 4 °C. Do **not** add the detergent or soak steps — you will decant fines and
   degas in week 2 (`12`).

## 3 Buffers and reagents

Each reagent is sized to what the protocol actually consumes, and grouped by when you make it.

| § | Reagent | **Batch to make** | Make in |
| :--: | :--- | :--- | :--: |
| `3.1` | 1× PBS, pH 7.4 | **4 L** | P2 |
| `3.2` | Assay buffer, pH 6.8 | **500 mL** | P2 |
| `3.3` | Maltose standard, 1 mg/mL | **100 mL** | P2 |
| `3.4` | DNS reagent | **100 mL** | P2 |
| `3.5` | Saturated (NH₄)₂SO₄ | **50 mL** | P2, then overnight |
| `3.6` | 1 % soluble starch | **2 × 100 mL** | weeks 3 and 4 — **not in advance** |
| `3.7` | Electrophoresis reagents | for 2 mini-gels | week 3 |

### 3.1 1× phosphate-buffered saline, pH 7.4

Final concentrations: 137 mM NaCl, 2.7 mM KCl, 10 mM Na₂HPO₄, 1.8 mM KH₂PO₄.

$$m\;(\mathrm{g}) = c\;(\mathrm{mol\,L^{-1}}) \times V\;(\mathrm{L}) \times M\;(\mathrm{g\,mol^{-1}})$$

| Symbol | Meaning | Value here |
| :--- | :--- | :--- |
| $m$ | mass of the salt to weigh, in **grams** | the answer |
| $c$ | target **molar concentration**, in mol/L | the final concentrations above — write mM as ÷ 1000, so 137 mM = 0.137 mol/L |
| $V$ | final **volume** of solution, in litres | 1 L, or 0.5 L, or 4 L for the scaled batch |
| $M$ | **molar mass** of that salt form, in g/mol | column 2 of the table below — this is the number that changes with the hydrate |

The units cancel: $(\mathrm{mol\,L^{-1}}) \times (\mathrm{L}) \times (\mathrm{g\,mol^{-1}}) = \mathrm{g}$.

| Reagent | $M$ (g/mol) | Calculation | Mass for 1 L | Mass for 500 mL | **Mass for 4 L** |
| :--- | :--: | :--- | --: | --: | --: |
| NaCl | 58.44 | 0.137 × 1 × 58.44 | **8.00628 g** | **4.00314 g** | **32.02512 g** |
| KCl | 74.55 | 0.0027 × 1 × 74.55 | **0.201285 g** | **0.1006425 g** | **0.80514 g** |
| Na₂HPO₄ (anhydrous) | 141.96 | 0.010 × 1 × 141.96 | **1.4196 g** | **0.7098 g** | **5.6784 g** |
| KH₂PO₄ (anhydrous) | 136.09 | 0.0018 × 1 × 136.09 | **0.244962 g** | **0.122481 g** | **0.979848 g** |

**Make the 4 L batch** — the protocol consumes ≈ 4 L of PBS in total, and the dialysis alone takes
3 L of it (see the materials section at the top). The 1 L column is there only for reference.

**Hydrate warning.** 141.96 g/mol is **anhydrous** Na₂HPO₄. If your bottle is a hydrate, substitute
its molar mass — the mass you weigh changes by up to 2.5×:

| Form | $M$ (g/mol) | Mass for 10 mM / 1 L | Mass for 4 L |
| :--- | --: | --: | --: |
| Na₂HPO₄ (anhydrous) | 141.96 | 1.4196 g | 5.6784 g |
| Na₂HPO₄·2H₂O | 177.99 | 1.7799 g | 7.1196 g |
| Na₂HPO₄·7H₂O | 268.065 | 2.68065 g | 10.7226 g |
| Na₂HPO₄·12H₂O | 358.14 | 3.5814 g | 14.3256 g |

**Procedure — scales to any volume.** Use the column matching your final volume $V$.

1. **Weigh** each salt separately to the masses in that column, reading the balance to 0.0001 g.
2. **Dissolve** all four in **~80 % of the final volume** of distilled water on a magnetic stirrer
   (800 mL for 1 L, 400 mL for 500 mL, **3200 mL for 4 L**). Add the Na₂HPO₄ first and stir until
   clear before adding KH₂PO₄.
3. **Adjust pH to 7.4** with 1 M HCl or 1 M NaOH, dropwise, probe immersed.
4. **Bring to the final volume** (1000.0 mL, 500.0 mL or 4000.0 mL), mix thoroughly, and re-check
   pH after dilution.
5. Filter if a precipitate appears; store at 4 °C. **Label with the date and the volume.**

**Anticipated titrant volume.** The salt ratio as written does *not* natively give pH 7.4. Using
Henderson–Hasselbalch with the apparent second dissociation constant $pK_{a2}' \approx 6.8$
(valid at $I \approx 0.15$ M, 25 °C):

$$\frac{[\mathrm{HPO_4^{2-}}]}{[\mathrm{H_2PO_4^-}]} = 10^{\,7.4-6.8} = 3.9810717$$

Holding $[\mathrm{H_2PO_4^-}] = 1.8$ mM gives $[\mathrm{HPO_4^{2-}}] = 7.1659291$ mM, so
$10 - 7.1659291 = 2.8340709$ mM of HPO₄²⁻ must be protonated:

$$\approx 2.8341\ \text{mL of 1 M HCl per litre of buffer}$$

Expect roughly that much 1 M HCl — **≈ 11.3362836 mL for the 4 L batch**. Treat it as an estimate
only — it assumes anhydrous Na₂HPO₄, no CO₂ absorption and 25 °C. **Always titrate to the measured
pH, never to the calculated volume.** (With the classical 8 mM Na₂HPO₄ formulation the
requirement falls to ≈ 0.834 mL of 1 M HCl per litre — see `R5`, item 4.)

### 3.2 Assay buffer, pH 6.8

Sodium phosphate, **pH 6.8** — the pH at which sweet potato amylase is reported to work fastest.
**Make the 500 mL batch:** the protocol consumes ≈ 327 mL of it across weeks 1, 3 and 4.

| Salt | $M$ (g/mol) | For 100 mL | **For 500 mL** | For 1 L |
| :--- | --: | --: | --: | --: |
| Na₂HPO₄·12H₂O | 358.14 | 1.7907 g | **8.9535 g** | 17.907 g |
| KH₂PO₄ | 136.09 | 0.68045 g | **3.40225 g** | 6.8045 g |

Dissolve both in 400 mL water, adjust to **pH 6.8** with 1 M HCl/NaOH, and bring to 500.0 mL.
Store at 4 °C — this one keeps for the whole run.

> **Decide the Ca²⁺ question before you start.** Plant β-amylases are Ca²⁺-dependent, and both
> PBS and this buffer are Ca²⁺-free. See `R5`, item 5 — if your group is resolving β-amylase
> activity, add CaCl₂ to **0.11098 g/L** (1 mM, $M$ = 110.98) here, and use the same buffer for
> the starch.

### 3.3 Maltose standard, 1 mg/mL

**Weigh 100.0 mg maltose ($M$ = 342.296 g/mol) and bring to 100.0 mL with assay buffer.** Mark the
bottle and store at 4 °C; discard if it grows mould.

### 3.4 DNS reagent

| Component | Amount | Final concentration in 100 mL |
| :--- | --: | --: |
| 3,5-dinitrosalicylic acid | **1 g** | 10 mg/mL |
| Rochelle salt (NaK tartrate) | **30 g** | 300 mg/mL |
| NaOH, 2 M | **20 mL** | 0.4 M NaOH delivered |
| Distilled water | to 100 mL | — |

1. Dissolve **1 g DNS** in ~20 mL distilled water with stirring (warm gently to 40 °C if needed).
2. Add **20 mL of 2 M NaOH** — the solution darkens to deep red-brown as DNS is reduced to the
   naphthoquinonylhydrazide form in alkali. This is the reagent's working colour.
3. Add **30 g Rochelle salt** in portions, stirring until dissolved.
4. Bring to **100.0 mL**, mix, filter out undissolved particles.
5. Store in an amber bottle at room temperature, protected from light. Discard if a precipitate
   forms or the colour goes green or black.

### 3.5 Saturated (NH₄)₂SO₄ solution — overnight, 4 °C

**Solubility of (NH₄)₂SO₄ ≈ 71 g / 100 mL water at 0–4 °C.**

$$m_{\text{salt}} = V_{\text{water}} \times \frac{S}{100} = 50 \times \frac{71}{100} = 35.5\ \text{g}$$

1. Place 50 mL distilled water in a beaker and start the stirrer.
2. Add **35.5 g** (NH₄)₂SO₄ in 4–5 small portions, stirring until each has dissolved.
3. A few crystals will remain undissolved at 4 °C — **expected, and it confirms saturation.** Do
   not filter them out; they dissolve as the solution is used on ice.
4. Refrigerate at 4 °C overnight. **Keep in an ice bath whenever it is in use.**

You need 46.66667 mL (`6`), so 50 mL is the right batch.

### 3.6 1 % (w/v) soluble starch — **make in weeks 3 and 4, not now**

**Do not make this in advance.** Hydrolysed starch gives a high substrate blank (BS) and the
blank ruins the assay. You need **two 100 mL batches** — one at the start of week 3, one at the
start of week 4. Each batch is 1 g of starch.

1. Weigh **1 g soluble starch** into a 100 mL volumetric flask.
2. Add ~80 mL assay buffer. **Disperse the powder first** in a few mL of buffer into a
   smooth slurry before adding the rest — dumping starch into liquid clumps it irreversibly.
3. Heat to 80–90 °C in a boiling-water bath or microwave (30–60 s, swirling) to gelatinise and
   dissolve; the solution should be clear to slightly opalescent.
4. Cool to room temperature, bring to 100.0 mL with assay buffer, mix.
5. Use the same day. Discard the remainder — do not carry it into the next week.

| Batch | Made at | Used for | Volume |
| :--: | :--- | :--- | --: |
| A | start of week 3 | screening curve blanks + screening reactions | 100 mL |
| B | start of week 4 | quantitative reactions | 100 mL |

### 3.7 Electrophoresis reagents

| Reagent | Recipe | Storage |
| :--- | :--- | :--: |
| **4× Laemmli sample buffer** | 250 mM Tris-HCl pH 6.8, 20 % (v/v) glycerol, 4 % (w/v) SDS, 0.004 % (w/v) bromophenol blue, 10 % (v/v) β-mercaptoethanol | 4 °C, **fresh weekly** |
| **1× running buffer** | 25 mM Tris, 192 mM glycine, 0.1 % (w/v) SDS; do **not** adjust pH | RT |
| **12 % resolving gel**, 1.0 mm, 10-well | 375 mM Tris-HCl pH 8.8, 12 % acrylamide/bis (29:1), 0.1 % APS, 0.1 % TEMED | cast in week 4 |
| **4 % stacking gel**, 1.0 mm | 125 mM Tris-HCl pH 6.8, 4 % acrylamide/bis, 0.1 % APS, 0.1 % TEMED | cast in week 4 |
| **Coomassie stain** | 0.1 % (w/v) Coomassie Brilliant Blue R-250 in 40 % (v/v) methanol, 10 % (v/v) acetic acid | RT, re-usable |
| **Destain** | 10 % (v/v) acetic acid, 40 % (v/v) methanol | RT, re-usable |

---

# Week 1 — Crude extraction, 70 % (NH₄)₂SO₄ precipitation, dialysis setup

Hands-on **3.50 h** of the 5 h block. Ends with dialysis running overnight.

- [ ] Grind and filter 20 g tuber → 60 mL Extract 1 (`4`–`5`)
- [ ] Take the 20.0 mL Extract 2 aliquot (`5`, step 7)
- [ ] Calculate the salt volume (`6`)
- [ ] Add saturated salt in 5 stages (`7`)
- [ ] Centrifuge, redissolve the pellet (`8`)
- [ ] Load the dialysis bag (`9`)

**Materials:** 20 g sweet potato, 60 mL cold 1× PBS, chilled mortar and pestle, 3–4 layers of
cheesecloth, ≥ 100 mL beaker, graduated cylinder, 50 mL saturated (NH₄)₂SO₄ on ice,
100 mL beaker on a stirrer in an ice bath, 2 × centrifuge tubes and rotor at 4 °C, dialysis tubing
6–12 kDa MWCO, 1 L cold PBS, 500 mL beaker on a stirrer, ice bath, clips.

## 4 Materials and pre-chilling

1. **Pre-chill** the mortar, pestle and a 60 mL aliquot of PBS on an ice bath (0–4 °C) — they were
   left in the fridge overnight. A room-temperature mortar warms a 20 g mash by several degrees in
   the first minute.
2. **Prepare the tissue.** Wash the tuber under running water, peel, remove any discoloured or soft
   tissue, and cut into ~5 mm cubes. Weigh **exactly 20.0 g** into a tared clean beaker.
3. Keep the cut tissue on ice until you grind it.

## 5 Grinding and filtration — Extract 1

1. Pour **30 mL** cold PBS into the chilled mortar, then add the 20 g of tissue. **Do not add buffer
   on top of dry tissue** — it clumps.
2. **Grind** with the pestle in short, firm strokes until no visible fragments remain and the
   paste is smooth. Work in 2–3 min bouts, returning the mortar to the ice bath between bouts.
3. **Filter** the homogenate through 3–4 layers of cheesecloth into a clean beaker, squeezing
   gently. **Do not squeeze hard** — forcing starch and fine debris through raises the substrate
   blank (BS) in weeks 3–4.
4. **Rinse** with the remaining 30 mL of cold PBS in 3–4 small portions, washing the mortar, the
   pestle and the residue retained on the cloth. Combine all filtrate.
5. **Make up the volume** to **60.0 mL** with cold PBS.
6. **Record:** recovered volume = __________ mL; colour; time from grinding to freezing =
   __________ min.
7. **Split:** 20.0 mL → **Extract 2**, to be used immediately in `6`. The remaining ≈ 40 mL
   → 2 aliquots at −20 °C as spare.

> **Naming.** The combined filtrate is **Extract 1**; the 20.0 mL portion taken from it for
> precipitation is **Extract 2**. Both names are used exactly this way throughout.

## 6 Calculate the volume of saturated salt

$$V_{\text{salt}} = V_0 \times \frac{S_2 - S_1}{1 - S_2}$$

With $V_0$ = 20 mL, $S_1$ = 0, $S_2$ = 0.70:

$$V_{\text{salt}} = 20 \times \frac{0.70 - 0}{1 - 0.70} = 20 \times \frac{0.70}{0.30} = \frac{14}{0.3} = \mathbf{46.66667\ \text{mL}}$$

**Do not round this to 47 mL.** 47 mL would give a final saturation of $0.70 \times \frac{47}{67} =
0.49105$ instead of 0.70 — the error sits in the denominator, so it does not cancel.

## 7 Add the salt in stages

Place the 20.0 mL Extract 2 in a beaker in an ice bath with the stirrer running. Add saturated
(NH₄)₂SO₄ slowly, dropwise, from a burette or pipette reservoir, **stirring continuously**:

| Addition | This addition (mL) | Cumulative salt (mL) | Total volume = salt + 20 mL extract (mL) |
| :--: | --: | --: | --: |
| 1 | 10.0 | 10.0 | 30.0 |
| 2 | 10.0 | 20.0 | 40.0 |
| 3 | 10.0 | 30.0 | 50.0 |
| 4 | 10.0 | 40.0 | 60.0 |
| 5 | **6.66667** | **46.66667** | **66.66667** |
| | | | |

The final 6.66667 mL is the arithmetic remainder of `6`; measure it as 6.67 mL on a burette.
Continue stirring **20–30 min** after the last addition, still on ice. Protein precipitates as
white-to-cream floccules. Record when flocculation became visible: __________ min.

## 8 Centrifuge and redissolve the pellet

1. **Centrifuge at 10 000 × g, 10 min, 4 °C** — *transfer the supernatant to a fresh tube,
   discard the pellet, repeat once.* Two 10 min spins at 10 000 × g are needed; a single
   4000 × g spin does not clear the supernatant and will carry precipitated protein into the
   dialysis bag. Retain the supernatant if you want a "70 % cut-through" control.
2. **Record the pellet mass** (tube + pellet, then tube alone): __________ mg.
3. **Redissolve the pellet in 1.0 mL cold PBS**, triturating with a spatula until no visible
   fragments remain. This is the start of **Crude Enzyme 2**.
4. Go immediately to `9`.

> **Volume conflict.** Your source gives three different volumes here: "redissolve in 1 mL" (this
> procedure), "total volume 10 mL" (its summary table), and "load 9.9 mL" onto the column. These
> are mutually exclusive, and the choice changes every yield downstream. The written procedure
> says 1 mL; the record it must match is `R5`, item 2. **Record what you actually used:**
> V = __________ mL.

## 9 Load the dialysis bag

> **MWCO and buffer volume are missing from your source notes.** They are not optional details — a
> 6–8 kDa membrane is required to retain a 50–60 kDa amylase, and the buffer must be in large
> excess (≥ 50× the sample) for the salt gradient to clear. Added here as the standard choice.

1. **Prepare the bag.** Soak 6–12 kDa MWCO tubing in distilled water for 20 min to open the pores,
   then rinse thoroughly. Test it: fill a 5 mL piece with water, tie it off, immerse and check
   for leaks over 5 min.
2. **Load.** Pipette the 1.0 mL of Crude Enzyme 2 in, seal both ends with clamps, rinse the outside.
3. **Dialyse.** Submerge the bag completely in **1 L of cold 1× PBS** in a beaker in an ice bath.
   Stir gently and continuously — stirring is what keeps the boundary layer thin and the diffusion
   rate high.
4. **Leave overnight, 6 h.** Change the external buffer at **2 h, 4 h and 6 h**: discard and add
   1 L of fresh cold PBS each time. Finish in `11`.

## 10 Week 1 record

| Quantity | Value |
| :--- | :--- |
| Tissue mass weighed (g) | |
| Buffer used for grinding (mL) | |
| Buffer used for rinsing (mL) | |
| Extract 1 recovered volume (mL) | |
| Extract 2 aliquot taken (mL) | |
| Saturated salt added, total (mL) | |
| Final precipitation volume (mL) | |
| Time from grinding to freezing (min) | |
| Pellet mass (mg) | |
| Crude Enzyme 2 volume after redissolution (mL) | |
| Dialysis started at (time) | |

---

# Week 2 — Dialysis harvest, Sephadex gel filtration, fraction collection

Hands-on **3.75 h** of the 5 h block. **This is the heavy week — start on time.** Elution is
~32–50 min of continuous real-time drainage that cannot be paused, and the whole session is
schedule-critical.

- [ ] Harvest the dialysis bag, clarify twice (`11`)
- [ ] Decant fines, make slurry, degas (`12`)
- [ ] Pack to $V_c$ = 80 mL, equilibrate (`13`)
- [ ] Clarify and load the sample (`14`)
- [ ] Elute, collect 12 fractions (`15`)
- [ ] Split, label, freeze (`16`)

## 11 Finish the dialysis and harvest

1. **Confirm de-salting.** If you have a conductivity probe, the exterior should read close to the
   PBS you started with — for ammonium sulphate this is the difference between tens of mS/cm and
   a few. Conductivity inside the bag: __________ mS/cm.
2. **Harvest.** Remove the bag, blot the outside dry on paper towel, snip one end, transfer the
   contents to a chilled tube. Record the recovered volume: __________ mL.
3. **Clarify — centrifuge twice at 10 000 × g, 10 min, 4 °C.** After the first spin transfer the
   supernatant to a clean chilled tube and discard the pellet; after the second, keep the
   supernatant. This is **Crude Enzyme 2, desalted**.
4. **Measure its activity before loading** (Week 4, the same procedure you will run on the stages
   next week). This is the "load" activity used in the recovery calculation. Record it now so a
   failed column run still yields a usable datum.
5. Keep on ice for the rest of the session.

## 12 Resin: remove fines and degas

1. **Remove fines.** Let the hydrated beads settle under gravity, then carefully decant the milky
   supernatant, which carries broken beads that will block the column frit.
2. **Make a slurry.** Resuspend the settled bed in fresh PBS to a **50–75 % (v/v) slurry**.
3. **Degas** under a vacuum desiccator for **15–20 min**. Trapped air is the single most common
   cause of a cracked, channelling column.

## 13 Pack and equilibrate the column

1. Mount the column **vertically** — check with a spirit level — and clamp it firmly in a
   vibration-free rack. Fit the bottom outlet and stopcock; **close the stopcock**.
2. Pour **10 mL of degassed PBS** into the bottom and let it wet the frit. The level should rise
   flat across the bed support, with no air pocket underneath.
3. **Pour the slurry down the inside wall in one continuous stream**, guiding it with a glass rod.
   Pouring from height and breaking the stream traps bubbles; letting the slurry run *up* the wall
   packs against gravity.
4. **Settle.** Open the outlet and let buffer drain under gravity until the bed height stops
   changing — a stable bed volume of $V_c$ = **80 mL**. Measure and record the settled height:
   h = __________ mm. **Never let the bed dry** — the moment flow stops, cover with buffer.
5. **Wash off fines.** Run 2 bed volumes (160 mL) of PBS through, then discard that effluent.
6. **Equilibrate** with **2–3 column volumes (160–240 mL)** of degassed PBS. Equilibration is
   complete when effluent pH and A₂₈₀ baseline are both stable — record pH = ______ ;
   A₂₈₀ = ______.

## 14 Prepare and load the sample

1. **Clarify** Crude Enzyme 2 at 4000 × g for 15–20 min at 4 °C, or pass it through a 0.45 µm
   low-protein-binding syringe filter. Record which: __________.
2. Measure the clarified volume: __________ mL.
3. **Drain the head.** Let buffer drain until the meniscus is flush with the top of the bed, then
   **close the stopcock immediately.** A flat, undisturbed bed surface is what makes the band
   narrow; a disturbed or cracked surface smears the elution profile.
4. **Load** the sample in one smooth motion onto the **centre** of the bed with a micropipette,
   without touching the bed surface. **Keep the load at 1.0–2.0 mL, i.e. 1.25–2.5 % of $V_c$.**

   > **Load-volume conflict.** Your source notes specify 1.0–1.6 mL here, but its summary table
   > claims 9.9 mL was loaded. 9.9 mL on an 80 mL bed is 12.4 % of the bed volume — far above the
   > 1–2 % that gives usable resolution on a soft-bed Sephadex column. Use 1.0–2.0 mL per run; if
   > the whole crude sample must go through, **run the column several times** and pool the
   > corresponding fractions (`R5`, items 1–2).

5. **Allow the sample to enter** with the outlet closed for 1 min, then open it.
6. **Wash the wall** with 0.5 mL of PBS and let it soak into the bed before topping up with bulk
   buffer.

## 15 Elute and collect

1. Top up with PBS and open the outlet. Maintain a constant gravity flow of **1–2 mL/min**.
   Measure and record the flow rate: __________ mL/min.
2. **Discard the void.** Let the first $V_0$ mL drain to waste — 25 mL on G-75, ≈ 30 mL on G-100
   (see the Sephadex resin table under P1). Note: the salt from the crude load also
   elutes here.
3. **Collect 4.0 mL per fraction into 12 numbered tubes.** Cumulative volume after tube *n* is
   $V_0 + 4n$. For $V_0$ = 25 mL, tubes 1–12 span 25 → 73 mL.

   > **Practical note.** Eluting 48 mL at 1.5 mL/min takes ~32 min of continuous, uninterrupted
   > time — you cannot pause mid-run. Either work through it in one sitting or use a fraction
   > collector. Mark the tube positions on the column so you can cut the stream at the right
   > volume.

4. **Stop condition.** If A₂₈₀ in tube 12 is still above the buffer baseline, **keep going** in
   4.0 mL fractions out to ≈ 1.2 $V_c$ = 96 mL (tube 18) before declaring the peak finished. A
   12-fraction, 48 mL collection on an 80 mL bed stops at 0.91 $V_c$ and will cut off a
   late-eluting peak.
5. Keep the fractions on ice — they contain the activity.

## 16 Split, label, store

1. Split each fraction into two labelled aliquots: one for A₂₈₀ and DNS (Week 3), one spare.
2. If analysis is on a later day, **freeze both at −20 °C** and **thaw on ice** in week 3 — never
   at room temperature, never straight from frozen.
3. Complete the elution log (`R2.1`).

## 17 Week 2 record

| Quantity | Value |
| :--- | :--- |
| Resin grade, lot, dry mass (g) | |
| Settled bed volume $V_c$ (mL) | |
| Settled bed height h (mm) | |
| Equilibration volume (mL) | |
| Effluent pH / A₂₈₀ | |
| Void volume discarded $V_0$ (mL) | |
| Flow rate (mL/min) | |
| Clarified load volume (mL) | |
| Load activity, U/mL | |
| Fractions collected (no. × mL) | |
| Fractions continued to (no.) | |

---

# Week 3 — Screening, electrophoresis, and pooling

Hands-on **≈ 3.5 h** of the 5 h block. The key trick is that **the gel run is unattended**: start it
first, then do the fraction screening while it runs. You are looking for **where the peak is**,
not for a reportable number.

- [ ] **Make starch batch A** — 1 g in 100 mL assay buffer
- [ ] Thaw fractions on ice, read A₂₈₀ (`18`)
- [ ] Cast and load the SDS-PAGE, **start the run** (`21`, `22`)
- [ ] *gel runs ~1.5 h unattended — do the screening while it runs*
- [ ] Build the 0.6 mL-basis screening curve (`19`)
- [ ] Run the screening DNS assay on all fractions (`19`)
- [ ] Plot the elution profile, pick and pool the peak (`20`)
- [ ] Stop the gel, fix and stain it (`23`)

## 18 A₂₈₀ of the fractions

1. Thaw the fraction aliquots **on ice**. Never at room temperature.
2. Read **A₂₈₀** for every fraction, **zeroed against the same PBS you used to equilibrate the
   column** — not distilled water. A salt-mismatched blank shifts the whole profile.
3. Estimate protein concentration as $c\,(\mathrm{mg/mL}) \approx A_{280} \times 2$, using
   $A_{280} = 1 \leftrightarrow 1\ \mathrm{mg/mL}$ for a generic protein mixture. **This is a rough
   estimate, and only that:** with no Bradford or Lowry on the bench (`R5`, item 8) and no
   extinction coefficient for a mixed plant extract, absolute protein — and therefore **specific
   activity (U/mg)** — cannot be measured, and those cells stay blank in `R2.3`. A₂₈₀ is used
   here for **relative** comparison only.
4. Record A₂₈₀ in the elution log (`R2.1`).

## 19 Screening DNS assay on the fractions

**This format is not the same as week 4. Do not mix the two sets of numbers.**

| Component | Volume |
| :--- | --: |
| Fraction (undiluted, or pre-diluted) | **0.1 mL** |
| 1 % starch | **0.5 mL** |
| DNS, added after incubation | **1.0 mL** |
| Water, added after boiling | **2.0 mL** |
| Pre-DNS reaction volume | **0.6 mL** |
| Final volume | **3.6 mL** |

Temperature and time are unchanged: 37 °C, 10 min, boil 5 min, read A₅₄₀.

**Build the screening standard curve first — at a 0.6 mL pre-DNS basis.** Six tubes from the
1 mg/mL maltose stock:

| Tube | Maltose stock (mL) | Buffer (mL) | Pre-DNS total (mL) | DNS (mL) | Water (mL) | A₅₄₀ |
| :--- | --: | --: | --: | --: | --: | --: |
| S0 | 0 | 0.60 | 0.60 | 1.0 | 2.0 | __________ |
| S1 | 0.12 | 0.48 | 0.60 | 1.0 | 2.0 | __________ |
| S2 | 0.24 | 0.36 | 0.60 | 1.0 | 2.0 | __________ |
| S3 | 0.36 | 0.24 | 0.60 | 1.0 | 2.0 | __________ |
| S4 | 0.48 | 0.12 | 0.60 | 1.0 | 2.0 | __________ |
| S5 | 0.60 | 0 | 0.60 | 1.0 | 2.0 | __________ |

> **Two things must change with this format, or the numbers are wrong.**
>
> 1. **The standards must be rebuilt at 0.6 mL pre-DNS.** If you reuse the week-4 curve (a 1.0 mL
>    basis) on a 0.6 mL reaction you inflate every result by $1.0/0.6 = 1.66667$ times.
>    2. **The results are not comparable to week 4 in absolute terms.** The screen runs at
>    1.67 % (w/v) starch while week 4 runs at 50 % — an 8.3-fold difference in substrate
>    concentration, and rate depends on substrate. **The screen ranks the fractions; only the
>    week-4 assay (`26`) on the pooled peak is reportable.**

**Run.** Add 0.5 mL starch to each tube; pre-equilibrate 5 min at 37 °C; add 0.1 mL fraction;
incubate exactly 10 min; add 1.0 mL DNS; boil 5 min; cool on ice; add 2.0 mL water; read at 540 nm
against S0. **Stagger the fraction additions and time on the first one** — a few seconds of drift
across a series of tubes is visible in the profile.

**Calculate** with the same chain as week 4 (`R1`), substituting $V_{\text{total, pre-DNS}} = 0.6$
mL in step 3 and $V_{\text{enzyme}} = 0.1$ mL in step 5:

$$\text{U/mL (screen)} = \frac{n_{\mu\mathrm{mol}} \times DF}{10 \times 0.1}$$

## 20 Plot the profile and select the peak

1. Plot **A₂₈₀** and **screen U/mL** against cumulative elution volume on the same axes (`R2.1`).
2. Identify the peak. A single symmetric peak is the pass criterion; two peaks mean the column was
   overloaded or the resin was under-equilibrated.
3. **Pool the peak fractions** — those at or above 50 % of the maximum A₂₈₀. Record the pooled
   volume: __________ mL. This pooled sample is your **Gel pool** for week 4.
4. Keep the pooled sample on ice for week 4, or freeze at −20 °C and thaw on ice.

## 21 Cast the SDS-PAGE gel

> **Provenance.** Your source notes end at gel filtration and the DNS assay; there is no
> electrophoresis text. `21`–`23` are a standard Laemmli workflow inserted where your bench
> sequence puts it — **after the column, before the report**. Confirm the gel system and which
> gels are required with your instructor (`R5`, item 9).

**Do this first, then start it running and come back to the screening** (`19`). The 1.5–2 h
electrophoresis is unattended bench time you would otherwise spend standing at the tank.

1. **Assemble** the glass plates with 1.0 mm spacers and the comb, clamp, and seal the bottom edge
   with parafilm or 5 % agarose. Pour water in and check for leaks; drain.
2. **Cast the resolving gel** (12 %, recipe under P1) to within 1 cm of the top, overlay with
   water-saturated butanol, and leave 30–45 min to polymerise at room temperature.
3. **Pour off the overlay**, rinse the surface twice with water, and **cast the stacking gel** on
   top. Insert the comb immediately, leaving wells 1 mm deep; allow 20–30 min to set.
4. **Pre-run** in 1× running buffer at **100 V for 15 min** to clear unpolymerised acrylamide.

**Prepare the samples.**

5. Estimate protein load from A₂₈₀ (`18`). Target **10–20 µg per lane**.
6. Mix **4 volumes of sample with 1 volume of 4× Laemmli buffer**. The buffer already carries
   10 % β-mercaptoethanol — for a **non-reducing** gel omit it or add 2 mM iodoacetamide at room
   temperature instead.
7. **Heat at 95 °C for 5 min**, then spin briefly, in the fume hood.

**Lane plan (10-well gel):**

| Lane | Content | Lane | Content |
| :--: | :--- | :--: | :--- |
| 1 | Molecular-weight marker | 6 | Crude Enzyme 2 |
| 2 | Extract 1 (crude) | 7 | Gel fraction, highest A₂₈₀ |
| 3 | Extract 1 (crude) | 8 | Gel fraction, next |
| 4 | (blank / buffer) | 9 | Gel fraction, last collected |
| 5 | (NH₄)₂SO₄ pellet, redissolved | 10 | Peak fraction (same as lane 7, loaded twice for clarity) |

> **Why there is no "pooled peak" lane.** Pooling happens at `20`, which is *after* the gel is
> already running. Lane 10 carries the peak fraction instead. That costs nothing — the gel's job is
> to show the band thinning from Extract 1 through Crude Enzyme 2 to the column fraction, and a
> single fraction shows that perfectly well.

## 22 Run the gel

1. Fill the tank with 1× running buffer so the gel is submerged. **Do not adjust the pH** — the
   glycine buffer self-corrects to ≈ pH 8.3 at the electrode.
2. Load 10–20 µL per lane alongside the marker. Lanes 2, 3, 5 and 10 carry the stage series, so
   the purification can be read off a single gel.
3. **Run at 70 V** until the dye front passes the stacking gel (20–30 min), then **120 V** until
   the front is ~1 cm from the bottom (60–90 min). **Total ≈ 1.5–2 h.**
4. If the gels run hot, run at 4 °C — losing a gel to heat is common and also distorts band
   positions.
5. Power down, open the cassette, and **cut the stacking gel off** before fixing.

## 23 Stain and image

1. Fix in **40 % methanol / 10 % acetic acid, 1 h**.
2. Stain in Coomassie R-250 (recipe under P1) for **1 h** with gentle rocking.
3. **Destain** in 10 % acetic acid / 40 % methanol with a piece of sponge tissue in the tank — the
   tissue absorbs released dye and keeps the background clear. **1–3 h to overnight.**
4. Rinse in water and image. **Record the apparent molecular weight of the main band:**
   __________ kDa. Compare against the **50–60 kDa** expected for sweet potato amylase.

   > **Check the native mass.** Published sweet potato β-amylase is a **tetramer of ~55–65 kDa
   > subunits** — gel filtration gives ~209–239 kDa for the native enzyme (Chang et al. 1996),
   > while SDS-PAGE gives ~64 kDa (Oktiarni et al. 2015). So on a **non-reducing** or native gel
   > expect a band near **~220 kDa**, not ~110–130 kDa. If your native band is ~220 kDa rather than
   > ~128 kDa, that confirms the tetramer — and it means your resin choice also needs revisiting
   > (`R5`, item 7).

| What to run | Answers | Expected |
| :--- | :--- | :--- |
| SDS-PAGE, reducing | How many species remain? Subunit mass? | one dominant band at **~50–60 kDa**, weaker bands thinning stage to stage |
| SDS-PAGE, non-reducing | Oligomeric state? | extra band near **~220 kDa** if the enzyme is a tetramer |
| Native PAGE | Oligomeric state, charge isoforms | 1–2 bands at higher apparent mass |
| Starch zymogram | Which band is active? | transparent zones over the amylase band(s) |

**Zymogram, if your group has starch-agar or starch-embedded gels:** cast the resolving gel with
0.5–1 % soluble starch; after running, wash twice in 50 mM sodium acetate pH 5.0 + 0.2 % Triton
X-100 (20 min each, 4 °C) to renature; incubate at 37 °C for 1–2 h; stain with 1 % I₂ in 1 M KCl.
Active bands appear as transparent zones on a blue-black background.

---

# Week 4 — Quantitative DNS on all three stages

Hands-on **≈ 2.5 h** of the 5 h block.

**All three stages are assayed in this one session, against one standard curve.** That is
deliberate: the reason for measuring three times is to *compare* activity across purification
steps, and curve-to-curve drift between separate sessions would confound exactly the comparison
you are trying to make. If you measure Extract 1 earlier for your own information, treat it as a
trial run, not a reportable number.

- [ ] **Make starch batch B** — 1 g in 100 mL assay buffer
- [ ] Build the 1.0 mL-basis standard curve (`24`) — **one curve, all three stages**
- [ ] Run the dilution screen on **Extract 1 only** (`25`)
- [ ] Re-run only the selected level on Crude Enzyme 2 and the Gel pool (`26`)
- [ ] Calculate all three, fill the purification summary (`R2.3`)
- [ ] Destain and image the gel from week 3

**Samples to assay, all three:** Extract 1 (or Extract 2, whichever you recorded), Crude Enzyme 2
desalted, and the Gel pool from `20`.

## 24 Standard curve — 1.0 mL basis

Six tubes, **1.0 mL pre-DNS each**, by $C_1V_1 = C_2V_2$ from the 1 mg/mL maltose stock:

| Tube | Maltose stock (mL) | Assay buffer (mL) | $C$ (mg/mL) | DNS (mL) | Water after boiling (mL) | A₅₄₀ |
| :--- | --: | --: | --: | --: | --: | --: |
| S0 (blank) | 0 | 1.0 | 0 | 1.0 | 8.0 | __________ |
| S1 | 0.2 | 0.8 | 0.2 | 1.0 | 8.0 | __________ |
| S2 | 0.4 | 0.6 | 0.4 | 1.0 | 8.0 | __________ |
| S3 | 0.6 | 0.4 | 0.6 | 1.0 | 8.0 | __________ |
| S4 | 0.8 | 0.2 | 0.8 | 1.0 | 8.0 | __________ |
| S5 | 1.0 | 0 | 1.0 | 1.0 | 8.0 | __________ |

**Procedure.** Add 1.0 mL DNS to every tube (order does not matter here). Boil **5 min** in a
100 °C bath — start timing when the tubes go in — then cool in ice water to room temperature.
Add 8.0 mL water, mix by inversion, read at 540 nm.

> **The treatment must match the samples exactly.** Both standards and samples are
> **1.0 mL pre-DNS + 1.0 mL DNS + 8.0 mL water = 10.0 mL final**. That is why $x$ on the standard
> curve can be read directly as mg of maltose per mL of the reaction mixture. Change the water
> volume for one set and not the other and the curve is invalid.

**Zero the instrument with S0**, not with buffer or water.

**Regression.** Fit $A_{540} = a\,x + b$ by least squares:

| Coefficient | Reference value (`R3.2`) | Your run |
| :--- | --: | --: |
| $a$ (slope) | 0.8305714 | __________ |
| $b$ (intercept) | 0.0023810 | __________ |
| $R^2$ | 0.99992317 | __________ |

**Accept $R^2 \geq 0.98$.** Reject a curve that is visibly curved at the top; if S5 reads above
A = 2.0–2.5, reduce the top standard and rebuild. **Never extrapolate beyond S5.**

> Your source notes quote $a = 0.83$ and $b = 0.0017$. The slope is right; **the intercept is
> not** — least-squares regression on its own six (0, 0.168, 0.340, 0.500, 0.666, 0.832) points
> gives $b = 0.0023810$. Using 0.0017 introduces a small positive bias at low absorbance, which is
> exactly where your most-diluted samples sit. Use your own regression; the reference table is
> only the reference (`R5`, item 3).

## 25 Dilution screen

Bring every sample into the 0–1.0 mg/mL range before measurement.

**Screen the four levels on Extract 1 only** — it is the most concentrated sample, so it is the one
most likely to read off-scale, and the level it selects is then applied to Crude Enzyme 2 and the
Gel pool. Crude Enzyme 2 is typically ~3× more active per mL than Extract 1 and the Gel pool
~0.6×, so if Extract 1 lands inside the curve at 1:10, expect Crude Enzyme 2 to need 1:20 and the
Gel pool to be fine neat. **Confirm each one rather than assuming** — but do not run all four
levels on all three samples unless a reading comes off-scale.

| Level | Extract (µL) | Buffer (µL) | Total (µL) | Dilution factor $DF$ | Transforms | Screening A₅₄₀ |
| :--- | --: | --: | --: | --: | :--- | --: |
| Neat | 2000 | 0 | 2000 | 1 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |
| 1:5 | 400 | 1600 | 2000 | 5 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |
| 1:10 | 200 | 1800 | 2000 | 10 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |
| 1:20 | 100 | 1900 | 2000 | 20 | 3 × 0.5 mL + 1 × 0.5 mL | __________ |

Each level needs **2.0 mL** (three 0.5 mL sample reactions + one 0.5 mL enzyme blank). Prepare
**2.5 mL of each** to allow for pipetting loss. **Keep all four on ice and use them the same
session** — a freshly made dilution is worth more than a re-made one.

> **Prepare 1:20 as a two-step dilution.** A single 100 µL → 1900 µL step gives a 0.5 mL reaction
> containing only **0.025 mL** of original extract, and the relative error of a 100 µL pipetting
> step is a significant fraction of that. Make 1:20 from the 1:5 stock instead —
> **500 µL of 1:5 + 1500 µL buffer = 2000 µL** — so every step is at least 1:4 and the source
> volume is five times larger. The dilution factor is still 20.
> *(Your source states the four levels consume "2.7 mL out of 5 mL"; that does not reconcile. Four
> levels at 2.0 mL need 8.0 mL of prepared dilution, or 10.0 mL at the 2.5 mL figure above.
> See `R5`, item 6.)*

**Selection rule.** Use the most dilute level whose corrected A₅₄₀ falls **strictly inside** the
standard-curve range, between S0 and S5. If even 1:20 exceeds S5, extend the series (1:40, 1:80)
and re-measure. **Never report a value from a sample that read off-scale.**

## 26 Quantitative DNS reaction

Three tube types per sample. $t = 0$ is the moment enzyme meets starch.

**Tubes for this session:** 4 dilution levels × Extract 1 (20 tubes) + 1 level × Crude Enzyme 2
(5) + 1 level × Gel pool (5) = **30 tubes**, not 60. If a reading comes off-scale, add that
sample's full four-level screen back in.

| Tube | 1 % starch | Assay buffer | Diluted enzyme | DNS | When |
| :--- | --: | --: | --: | --: | :--- |
| **Sample** (× 3) | 0.5 mL | 0 | 0.5 mL | 1.0 mL | **after** incubation — stops the reaction |
| **Blank enzyme** (BE) | 0.5 mL | 0 | 0.5 mL | 1.0 mL | **before** enzyme — zero-time |
| **Blank substrate** (BS) | 0.5 mL | 0.5 mL | 0 | 1.0 mL | **after** incubation |

1. Pipette **0.5 mL of 1 % starch** into every tube (3 sample + 1 BE + 1 BS = 5 tubes per level).
2. **Pre-equilibrate** in a 37 °C water bath for **5 min**. Add 0.5 mL buffer to BS now so all
   five tubes are volume-matched and heat-equilibrated.
3. Add **1.0 mL DNS to BE only** — it must contain the reagent *before* any enzyme, or the
   zero-time control will develop colour and read high.
4. **Start the reaction.** Add **0.5 mL of diluted enzyme** to the 3 sample tubes and to BE.
   **Stagger the additions** and start the timer on the first one. Adding enzyme to 15 tubes at
   once and timing the last gives a spread of several seconds at the start of a 600 s reaction —
   1–2 % error before any measurement is made.
5. **Incubate exactly 10 min at 37 °C.** Stopwatch, not the bath timer. $t = 10$ min = 600 s.
6. Add **1.0 mL DNS** to the 3 sample tubes and to BS, terminating the reaction.
7. **Boil 5 min** in a 100 °C bath. Cool in ice water to room temperature.
8. Add **8.0 mL water**, mix by inversion.
9. Read **A₅₄₀**, zeroing on S0. Record every tube individually before taking the mean — a
   replicate visibly off the line is information, not noise to be averaged away.

**Then calculate** — full chain in `R1`. Record in `R2.2`.

## 27 Week 4 record

| Quantity | Value |
| :--- | :--- |
| Curve $a$ / $b$ / $R^2$ | |
| Level selected from the Extract 1 screen | |
| Level used for Crude Enzyme 2 | |
| Level used for Gel pool | |
| Extract 1 activity (U/mL) and total (U) | |
| Crude Enzyme 2 activity (U/mL) and total (U) | |
| Gel pool activity (U/mL) and total (U) | |
| Yield at each step (%) | |
| Main SDS-PAGE band, reducing (kDa) — from week 3 gel | |
| Main band, non-reducing/native (kDa) | |
| Bands visible in Extract 1 vs Gel pool | |

---

# Reference

Material you read but do not perform at the bench.

## R1 The calculation chain

### R1.1 Principle and unit definition

Amylase hydrolyses starch to maltose and glucose. The reducing aldehyde end of each product
reduces 3,5-dinitrosalicylic acid to **3-amino-5-nitrosalicylic acid** in hot alkali, giving a
red-brown colour with a maximum at **540 nm**. Absorbance is proportional to the mass of reducing
sugar over the range established by the standard curve.

**Unit definition.** 1 U = the amount of enzyme that releases **1 µmol of reducing sugar
(as maltose) per minute** at 37 °C, at the pH of optimum activity.

$$\text{Specific activity} = \frac{\text{U/mL}}{\text{mg protein/mL}} = \text{U/mg}$$

### R1.2 The six steps

Work down this chain. No step may be skipped or combined — each one is a place a transcription
error hides.

**Step 1 — blank-corrected absorbance**

$$A_{\text{corr}} = A_{\text{sample}} - A_{\text{BE}} - A_{\text{BS}}$$

**Step 2 — reducing sugar concentration from the curve** (mg/mL of the pre-DNS reaction mixture)

$$c = \frac{A_{\text{corr}} - b}{a}$$

**Step 3 — mass of reducing sugar produced** (mg)

$$m = c \times V_{\text{total, pre-DNS}}$$

For week 4, $V_{\text{total, pre-DNS}}$ = 1.0 mL (0.5 starch + 0.5 enzyme), so $m = c$ mg exactly.
For the week-3 screen it is 0.6 mL, so $m = 0.6c$ mg.

**Step 4 — convert to micromoles**, using $M$(maltose) = **342.296 g/mol**

$$n_{\mu\mathrm{mol}} = \frac{m \times 10^{-3}\ \mathrm{g} \times 10^{6}\ \mu\mathrm{mol/mol}}{342.296\ \mathrm{g/mol}} = \frac{m \times 1000}{342.296}$$

**Step 5 — volumetric activity** (U per mL of the **original, undiluted** sample)

$$\boxed{\ \text{U/mL} = \frac{n_{\mu\mathrm{mol}} \times DF}{t \times V_{\text{enzyme}}} = \frac{n_{\mu\mathrm{mol}} \times DF}{10 \times 0.5}\ }$$

**Step 6 — total activity** (U in the whole volume of that stage)

$$\text{Total U} = (\text{U/mL}) \times V_{\text{stage}}$$

### R1.3 Which symbol means what

| Symbol | Meaning |
| :--- | :--- |
| $a$, $b$ | slope and intercept of the standard curve, A₅₄₀ = $ax + b$ |
| $A_{\text{BE}}$ | **enzyme blank** — sugar already present in the extract; DNS added *before* enzyme, so this is a true zero-time control |
| $A_{\text{BS}}$ | **substrate blank** — reducing sugar inherent to the starch preparation; compensates for hydrolysed starch |
| $DF$ / HSPL | dilution factor applied before the assay; back-corrects the result to the original sample |
| $V_{\text{enzyme}}$ | volume of **diluted** enzyme added to the reaction, in mL |
| $V_{\text{total, pre-DNS}}$ | total liquid in the reaction before DNS is added, in mL |
| $t$ | incubation time, min |
| U/mL | activity per mL of the original extract or fraction |
| U/mg | specific activity — activity per mg of total protein; the cleanest measure of purification progress |

> **The single most common error in this chain** is dividing by 1.0 mL instead of 0.5 mL in step 5.
> The 1.0 mL is the *reaction* volume (step 3); 0.5 mL is the *enzyme* volume (step 5). Confusing
> them doubles every activity reported.

### R1.4 Error budget

$\mathrm{d}c/\mathrm{d}A = 1/a = 1.2039904$ mg/mL per absorbance unit, so **± 0.002 A₅₄₀ translates
to ± 0.002408 mg/mL** of sugar. At $c \approx 0.5$ mg/mL that is ± 0.48 % — comparable to the error
from a 1–2 s timing slip over 600 s. Readings are therefore not worth better than **four
significant figures**; report $a$ and $b$ to seven and six decimals so they enter step 2 at full
precision.

## R2 Worksheets

### R2.1 Gel filtration elution log

| Fraction | Cumulative vol. (mL) | Colour | A₂₈₀ | A₅₄₀ (screen) | Screen U/mL | Note |
| :--: | --: | :--- | --: | --: | --: | :--- |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |
| 13+ | | | | | | *(continue if A₂₈₀ still high)* |

### R2.2 DNS assay worksheet — one block per dilution level

| | 1:5 | 1:10 | 1:20 | Other: ______ |
| :--- | --: | --: | --: | --: |
| A₅₄₀ sample 1 | | | | |
| A₅₄₀ sample 2 | | | | |
| A₅₄₀ sample 3 | | | | |
| $A_{\text{sample}}$ = mean | | | | |
| $A_{\text{BE}}$ | | | | |
| $A_{\text{BS}}$ | | | | |
| $A_{\text{corr}}$ (step 1) | | | | |
| $c$ (mg/mL) (step 2) | | | | |
| $m$ (mg) (step 3) | | | | |
| $n$ (µmol) (step 4) | | | | |
| **U/mL** (step 5) | | | | |
| Used? (inside curve?) | | | | |

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
| Main band on SDS-PAGE (kDa) | | | |

$$%\ \text{yield} = \frac{\text{Total U at this stage}}{\text{Total U at the previous stage}} \times 100 \qquad \%\ \text{purification} = \frac{\text{spec. act. at this stage}}{\text{spec. act. of stage 1}}$$

> **Before you fill in any yield, resolve `R5` items 1 and 2.** The source summary divides a total
> of 145.02 U (computed on a 49.8 mL extract) by a stage-1 total that its own procedure says came
> from only **20 mL**. Against the 20 mL actually processed, the same numbers produce a **171 %
> recovery** for a precipitation step — impossible, and a direct signal that one of the two
> volumes is wrong. Compute the denominator from the volume you actually precipitated.

## R3 Reference calculations

### R3.1 What the source optical data gives, recomputed without rounding

Using $a = 0.8305714$, $b = 0.0023810$, $M$(maltose) = 342.296 g/mol, $t = 10$ min,
$V_{\text{enzyme}} = 0.5$ mL, $V_{\text{total, pre-DNS}} = 1.0$ mL:

| Sample | $A_{\text{sample}}$ | $A_{\text{BE}}$ | $A_{\text{BS}}$ | $A_{\text{corr}}$ | $c$ (mg/mL) | $n$ (µmol) | $DF$ | **U/mL** |
| :--- | --: | --: | --: | --: | --: | --: | --: | --: |
| 1:5 | 0.868 | 0.020 | 0.020 | 0.828 | 0.994037 | 2.904029 | 5 | **2.904029** |
| 1:10 | 0.450 | 0.015 | 0.020 | 0.415 | 0.496789 | 1.451344 | 10 | **2.902689** |
| 1:20 | 0.238 | 0.010 | 0.020 | 0.208 | 0.247563 | 0.723243 | 20 | **2.892974** |
| Crude Enzyme 2 | 0.751 | 0.020 | 0.020 | 0.711 | 0.853171 | 2.492493 | 20 | **9.969973** |
| Gel pool | 0.511 | 0.010 | 0.020 | 0.481 | 0.576253 | 1.683492 | 5 | **1.683492** |

The three dilution levels agree to within **0.4 %** (2.892974–2.904029 U/mL) — the expected spread
for three independent dilutions of one sample, and good evidence the arithmetic is right. Their
disagreement is also informative: **the 1:20 level is the least trustworthy**, because it
contributes only 0.025 mL of original extract to the reaction (`25`) and is most sensitive to
the intercept term.

### R3.2 Standard curve reference data

| Tube | $x$ (mg/mL) | $A_{540}$ |
| :--- | --: | --: |
| S0 | 0 | Pre |
| S1 | 0.2 | 0.168 |
| S2 | 0.4 | 0.340 |
| S3 | 0.6 | 0.500 |
| S4 | 0.8 | 0.666 |
| S5 | 1.0 | 0.832 |

Least-squares fit: $A_{540} = 0.8305714\,x + 0.0023810$, $R^2 = 0.99992317$.

The slope is very slightly convex — 0.168, 0.340, 0.500, 0.666, 0.832 against 0.8306 × $x$ — a
marginal negative deviation at mid-range and a positive one at the top. Well within experimental
error, and not a reason to discard the linear fit.

### R3.3 Totals implied by the source summary — **and why they do not close**

| Stage | U/mL | Volume | Total U | Yield as printed |
| :--- | --: | --: | --: | :--- |
| Extract, as printed | 2.912 | 49.8 mL | 145.0176 U | — |
| Extract, the 20 mL actually precipitated | 2.912 | 20 mL | **58.24 U** | 100 % |
| Crude Enzyme 2 | 9.988 | 10 mL | 99.88 U | 68.87 % *(on 145.02 U)* |
| Crude Enzyme 2 | 9.988 | 9.9 mL | 98.88 U | **169.7 %** *(on 58.24 U)* |
| Gel pool | 1.687 | 20 mL | 33.74 U | 34.12 % *(on 98.88 U)* |

A precipitation step cannot recover more activity than was put into it. **69 % is the plausible
reading; 171 % is not.** Resolve `R5`, items 1–3 before quoting any of these in a report.

## R4 Acceptance criteria and troubleshooting

### R4.1 Accept the run only if

| # | Criterion | Why |
| :--: | :--- | :--- |
| 1 | Standard-curve $R^2 \geq 0.98$ | Below this the slope is not constant and every downstream value is biased |
| 2 | $A_{\text{BE}} \leq 0.03$ and $A_{\text{BS}} \leq 0.03$ | High blanks mean free sugar in the extract or hydrolysed starch |
| 3 | $A_{\text{sample}}$ inside the S0–S5 range | No extrapolation |
| 4 | Triplicate spread $\leq 10 \%$ | Larger than this is a pipetting or timing error, not real variation |
| 5 | Reacted samples stay brown/red-brown, never green or blue | Blue-green = DNS too alkaline or under-boiled |
| 6 | Elution profile is a single symmetric peak | Two peaks mean the column was overloaded or the resin under-equilibrated |

### R4.2 Symptom → cause

| Symptom | Likely cause | Fix |
| :--- | :--- | :--- |
| No colour change after boiling | DNS expired or added to the wrong tubes; sample off-scale | Fresh DNS; verify BE received DNS before enzyme |
| Green or blue final colour | Too alkaline, or the bath never reached 100 °C | Check bath temperature; immerse tubes to the liquid level |
| All readings identical across dilutions | Same dilution pipetted each time, or a flat curve | Re-make dilutions; confirm the standards span the range |
| Readings rise as you dilute | High blank contribution, or the 1:20 aliquot is the least reliable | Check $A_{\text{BE}}$; make 1:20 from the 1:5 stock (`25`) |
| $A_{\text{BE}}$ high | Extract left warm, or starch-rich tissue degraded | Keep everything on ice; re-prepare the starch |
| $A_{\text{BS}}$ high | Starch hydrolysed in storage, or added early and left warm | Prepare starch fresh; add DNS immediately after incubation |
| Split or channelled elution peak | Air in the slurry, disturbed bed surface, or overloading | Degas properly; never drain the bed dry; keep load ≤ 2 % of $V_c$ |
| High A₂₈₀ in every fraction, no peak | Load too large, or no equilibration | Reduce load to 1–2 % of $V_c$; equilibrate 3 CV |
| Recovery > 100 % | Wrong volume recorded somewhere | `R3.3`, `R5` — audit the volumes before believing it |
| No band on the SDS-PAGE | Protein too dilute, or ran off in the stacking gel | Load 20 µg; check the dye front stopped before the gel bottom |
| Band at ~100 kDa where 50–60 kDa expected | Dimer not fully reduced, or the gel ran too hot | Confirm β-ME in the Laemmli buffer; run cool |

### R4.3 Waste and cleanup

Dispose of all (NH₄)₂SO₄, DNS and Coomassie/destain solutions as **aqueous chemical waste** — none
of it goes down a sink. Chromium is absent here, but the Coomassie stain is methanol- and
acid-based and needs chemical collection. Gloves, gel casts and electrophoresis buffer are
chemical waste, not domestic.

### R4.4 How to round, when you must

Report **four significant figures** for activity and concentration. The inputs do not support
more: ± 0.002 A₅₄₀ alone is ± 0.48 % (`R1.4`). Carry $a$, $b$ and the saturation volumes at full
precision (PBS, `6`, `24`) and round only the final answer — never an intermediate.

## R5 Unresolved numbers — resolve before you run

| # | Issue | The conflict | What you must decide |
| :--: | :--- | :--- | :--- |
| 1 | **Stage-1 extract volume** | Summary uses 49.8 mL (→ 145.02 U); the procedure precipitates only 20 mL (→ 58.24 U) | Which volume was actually processed? Yield is undefined until this is fixed. |
| 2 | **Crude Enzyme 2 volume** | "Redissolve in 1 mL" vs "total volume 10 mL" vs "load 9.9 mL" | Record the real volume and use it in `R2.3` |
| 3 | **Standard-curve intercept** | Source quotes $b = 0.0017$; least squares on its own data gives $b = 0.0023810$ | Use your own regression (`24`) |
| 4 | **PBS phosphate ratio** | 10 mM Na₂HPO₄ + 1.8 mM KH₂PO₄ gives pH ≈ 7.95 unadjusted (≈ 7.55 at $pK_{a2}'$ = 6.8), not 7.4 | Keep 10 mM and **always** titrate (the PBS recipe predicts ≈ 2.8341 mL of 1 M HCl/L), or switch to the classical 8 mM / 1.8 mM |
| 5 | **Ca²⁺ dependence** | Plant β-amylases are Ca²⁺-dependent; both PBS and the assay buffer are Ca²⁺-free | Add CaCl₂ to 1 mM in the assay buffer and starch if β-amylase is the target |
| 6 | **Dilution volumes** | "2.7 mL out of 5 mL" does not reconcile with 4 levels × 2.0 mL | Use 2.5 mL per level (`25`) |
| 7 | **Void volume vs resin grade** | 25 mL on 80 mL gives $V_0/V_t$ = 0.3125 ⇒ G-50/G-75, the wrong resin for this enzyme | **Ask the instructor.** Published sweet potato β-amylase is a **tetramer, ~209–239 kDa native** (Chang et al. 1996) but ~64 kDa on SDS-PAGE. If the native form is ~220 kDa, G-100 (max 125 kDa) will **exclude it entirely** and it will elute in the void. You would need **G-200 or Sephacryl S-400** — which is what Chang et al. actually used. |
| 8 | **No protein assay** | Without Bradford/Lowry or an extinction coefficient, U/mg cannot be computed (`18`, step 3) | Add Bradford, or report activity only |
| 9 | **Electrophoresis not in the source** | `21`–`23` are a standard workflow inserted at your bench's instruction point | Confirm gel system and whether reducing / native / zymogram are all required |
| 10 | **Assay pH is unsettled** | The protocol uses pH 6.8, but Chang et al. (1996) report sweet potato β-amylase optimum at **pH 5**, while a 2022 study reports **pH 7.5** | Activity at the wrong pH can differ several-fold. **Ask the instructor** which pH the assay expects, and whether Ca²⁺ (1 mM) should be added — plant β-amylases are Ca²⁺-dependent and neither PBS nor the assay buffer contains it |
| 11 | **Are the source ODs real data or placeholders?** | Labelled "assumed values" | If placeholders, `R3` is a worked example only — do not report it as a result. See also item 12. |
| 12 | **20 g and the 1:3 ratio** | 20 g is a reasonable bench amount, but 3 mL/g is thinner than the 5–20 mL/g usual for plant tissue. More importantly, the worked example implies only **≈ 8.75 U per gram of tuber**, which is very low for a crop the USDA literature calls *"a rich source of β-amylase"* | If your own Extract 1 reads in that range, suspect the assay rather than the tissue. Check by measuring a commercial β-amylase standard in your own curve. Consider 1:5 extraction (20 g + 100 mL) if activity is low. |

## R6 Schedule

| Week | 5 h block | Hands-on |
| :--: | :--- | --: |
| **P1** | Safety · resin choice and hydration · collect all reagents | 0.5 h |
| **P2** | PBS 4 L · assay buffer 500 mL · maltose · DNS · saturated (NH₄)₂SO₄ overnight · chill mortar | 0.75 h |
| **Week 1** | Grind 20 g / 60 mL · filter · 20.0 mL aliquot · add 46.66667 mL sat. salt in 5 stages · stir 20–30 min · 2 × 10 000 × g / 10 min · redissolve in 1.0 mL · load dialysis bag into 1 L PBS | **3.50 h** |
| **Week 2** | Buffer change at 6 h · harvest · 2 × 10 000 × g / 10 min · decant fines · degas 15–20 min · pack to $V_c$ = 80 mL · equilibrate 2–3 CV · clarify 4000 × g · load 1.0–2.0 mL · elute void + 12 × 4.0 mL · split, label, freeze | **3.75 h** |
| **Week 3** | Starch batch A · A₂₈₀ all fractions · **cast + load gel, start run** · *screen DNS while it runs* · plot profile · pool peak · fix and stain gel | **≈ 3.5 h** |
| **Week 4** | Starch batch B · one standard curve for all 3 stages · dilution screen on Extract 1 only · re-run the selected level on stages 2 and 3 · calculate, fill `R2.3` · destain and image gel | **≈ 2.5 h** |
| **Week 5** | *Reserve.* Re-run anything that failed; finish the report | — |

**Why the gel sits in week 3, not week 4.** The original week 4 carried the quantitative DNS *and*
the whole electrophoresis, which times out at **≈ 7.1 h** — well over the 5 h block. Two changes fix
it without losing anything:

1. **The gel run is unattended.** Start it at the top of week 3 and screen the fractions while it
   runs. That converts ~1.5 h of standing at the tank into overlapping bench time.
2. **Screen four dilution levels on Extract 1 only** (`25`), then run just the winning level on
   Crude Enzyme 2 and the Gel pool. That is **30 tubes instead of 60**, saving ~1 h. It changes
   nothing scientifically — `25` already told you to pick the level inside the curve.

**Four week boundaries are physically forced:** dialysis must run overnight; gel-filtration elution
is 32–50 min of continuous real-time drainage; the DNS boiling batches are serial; and the cold
chain cannot be split across two lab days. Total hands-on bench time is ≈ 10 h.

**Week 5 is genuine spare, not a rescue slot** — the whole protocol now fits inside four weeks.

## R7 References

- Miller, G. L. (1959). Use of dinitrosalicylic acid for reducing sugars. *Analytical Chemistry* 31(3), 426–428.
- Bernfeld, L. (1955). Amylases, carbohydrases and maltases. *Methods in Enzymology* 1, 105–128.
- Hiromi, K. & Sato, M. (1960). Amylase. *Bulletin of the Institute for Physical and Chemical Research* 54, 362–400. (Sephadex fractionation ranges.)
- Sephadex G-25 / G-50 / G-75 / G-100 / G-150 product datasheets — fractionation ranges and swelling ratios.
- Voet, D. & Voet, J. (2011). *Biochemistry*, 5th ed., Wiley. (DNS chemistry; Henderson–Hasselbalch at physiological ionic strength.)
- Laemmli, U. K. (1970). Cleavage of structural proteins during heat-sodium dodecyl sulfate electrophoresis. *Nature* 227, 680–685.
- Nelson, N., Cox, J. D. & Lowe, C. V. (1957). A photometric method for measuring the breakdown of certain pyrazolamines. *Journal of Biological Chemistry* 228, 496–499.
- Course notes: `PROTOCOL LAB.docx`, `DNS METHOD TO DETERMINE ENZYME ACTIVITY.txt`.

---

## Appendix A — Quick reference card

```
REACTION      0.5 mL 1% starch  +  0.5 mL diluted enzyme      37 °C, 10 min
THEN          + 1.0 mL DNS  ->  boil 5 min  ->  ice cool  ->  + 8.0 mL water  ->  A540
BLANKS        BE: DNS BEFORE enzyme        BS: buffer replaces enzyme
CURVE         A540 = 0.8305714 x + 0.0023810     x in mg/mL of the 1.0 mL pre-DNS mixture
STEP 1        Acorr = Asample - ABE - ABS
STEP 2        c    = (Acorr - b) / a                      [mg/mL]
STEP 3        m    = c x Vtotal_preDNS      (1.0 mL here) [mg]
STEP 4        umol = m x 1000 / 342.296
STEP 5        U/mL = umol x DF / (10 x 0.5)     <-- 0.5 = ENZYME volume, not 1.0
STEP 6        U    = U/mL x Vstage

SCREEN FORMAT 0.1 mL fraction + 0.5 mL starch; + 1.0 mL DNS; + 2.0 mL water
              rebuild standards on a 0.6 mL pre-DNS basis, or results are 1.66667x too high
```

## Appendix B — Volumes

| Step | Volume | Week |
| :--- | --: | :--: |
| Extraction buffer | 30 mL to grind + 30 mL to rinse = **60 mL** for 20 g (1:3 w/v) | 1 |
| Extract 2 for precipitation | **20.0 mL** | 1 |
| Saturated (NH₄)₂SO₄ to add | **46.66667 mL** (10 + 10 + 10 + 10 + 6.66667) | 1 |
| Final precipitation volume | **66.66667 mL** | 1 |
| Pellet redissolved in | **1.0 mL** cold PBS | 1 |
| Dialysis buffer | **1 L**, changed at 2 h, 4 h, 6 h | 1–2 |
| Slurry | 150 mL PBS, 50–75 % (v/v) | 0, 2 |
| Column bed, $V_c$ | **80 mL** | 2 |
| Equilibration | 2–3 CV = **160–240 mL** | 2 |
| Column load | **1.0–2.0 mL** (1.25–2.5 % of $V_c$) | 2 |
| Void to discard, $V_0$ | 25 mL (G-75) / ≈ 30 mL (G-100) | 2 |
| Fractions | **12 × 4.0 mL**, continuing to tube 18 if needed | 2 |
| DNS reaction | 0.5 + 0.5 mL pre-DNS; + 1.0 mL DNS; + 8.0 mL water = 10.0 mL | 4 |
| Screen reaction | 0.1 + 0.5 mL pre-DNS; + 1.0 mL DNS; + 2.0 mL water = 3.6 mL | 3 |

## Appendix C — Daily checklist

**P1** (several days before Week 1) — resin weighed, chosen and hydrated · mortar, pestle and
60 mL of PBS into the fridge · every salt and chemical collected.

**P2** (the day before Week 1) — PBS made and at 4 °C · assay buffer, maltose stock and DNS made ·
saturated salt made and into the fridge overnight · dialysis tubing 6–12 kDa MWCO soaking.

**Week 1** — mortar and pestle on ice · 4 °C centrifuge · saturated salt in an ice bath ·
burette · dialysis tubing leak-tested · 1 L of cold PBS for the bag.

**Week 2** — resin hydrated and swelled · column mounted and levelled · stopcock fitted and
tested · fraction tubes numbered 1–18 and marked at 4.0 mL · conductivity probe · −20 °C freezer
space for the fractions.

**Week 3** — spectrophotometer warmed 15 min · ice bath · boiling bath at 100 °C · pipettes
calibrated · blanks and standards laid out in one row · **gel-casting kit, APS and TEMED fresh ·
1× running buffer · protein load estimated at 10–20 µg/lane · gloves and hood for β-ME.**

**Week 4** — stopwatch for the 10 min incubations · the week-3 gel soaking in destain.

---

*Compiled from `PROTOCOL LAB.docx` / `PROTOCOL LAB.txt` and `DNS METHOD TO DETERMINE ENZYME
ACTIVITY.txt`. Original files retained unmodified in `lab/`. Values carried at full precision per
`R4.4`; unresolved source conflicts are listed in `R5` and are not silently reconciled.*