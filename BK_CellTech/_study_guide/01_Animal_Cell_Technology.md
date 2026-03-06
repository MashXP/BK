# Animal Cell Technology
**Date:** 2026-01-23
**Source:** Cell tech 1-23.pdf

## 1. Animal Cell Culture Overview
- **Definition:** Cells maintained as independent units, genetically identical (homogeneous population).
- **Purpose:**
    - Investigate normal physiology or biochemistry of cells.
    - Test effects of compounds on specific cell types.
    - Produce artificial tissue (e.g., skin).
    - Synthesize valuable products (e.g., viral vaccines, monoclonal antibodies, recombinant glycoproteins) from large-scale cultures.
- **Advantages:**
    - Reproducibility of results.
    - Cheap/Cost-effective relative to animal models.
    - Precise control of environmental factors.
- **Disadvantages:**
    - Cell characteristics can change after a period of continuous growth (differentiation loss).
    - Ethical concerns (specifically for primary cultures).

## 2. Basic Equipment
To maintain a sterile and controlled environment:
- **Laminar Flow Cabinet (Class I, II (for dangerous samples)):** Provides a sterile work area to prevent contamination.
- **Incubator:** Maintains optimal conditions (Temperature, CO2, Humidity).
- **Culture Vessels:**
    - Laboratory scale: T-flasks, multi-well plates, spinner bottles.
    - Materials: Treated plastic to allow adhesion (anchorage-dependent cells) or specific coatings.
- **Microscopy:** Inverted microscope (light source from top, objective from bottom) to view cells attached to the bottom of flasks.
- **Preservation:** Liquid nitrogen storage facilities for cryopreservation.
- **Other:** Centrifuge (for separating cells from media).

## 3. Culture Environment & Media
### Culture Conditions
- **Gas Phase:** 5–10% $CO_2$ is standard.
- **Buffering System:**
    - **Bicarbonate-CO2 Buffer:** Used to maintain pH (6.9–7.4). Requires the specific $CO_2$ atmosphere.
    - **HEPES:** Organic buffer used in conjunction or as an alternative.
    - *Disadvantages:* Bicarbonate media can become alkaline quickly if removed from the incubator.
- **pH Indicator:** Phenol Red is added to visually monitor pH.
    - **Yellow:** Acidic (bacterial contamination or overgrowth).
    - **Red:** Neutral (Optimal, pH 7.0–7.4).
    - **Pink/Purple:** Alkaline.

### Media Composition
1.  **Carbohydrates:** 
	- Glucose (Energy source, carbon source for biosynthesis).
	- Alt: Fructose, decrease lactic acid, stable pH.
2.  **Amino Acids:** 0.1–0.2 mM. 
	- Essential for protein synthesis. 
	- **Glutamine** is critical (carbon/nitrogen source) but unstable; decomposes to ammonia (toxic).
3.  **Salts:** Maintenance of osmolarity.
4.  **Vitamins & Hormones:** Growth co-factors.
5.  **Serum:**
    - Derived from blood (e.g., Fetal Bovine Serum - FBS).
    - Promotes cell growth.
    - **Disadvantages:** Expensive, potential source of contamination (viruses/prions), batch-to-batch variability.
6.  **Antibiotics:**
    - **Penicillin G (100 U/ml):** Inhibits Gram-positive bacteria.
    - **Streptomycin (50 mg/l):** Inhibits Gram-negative and Gram-positive bacteria.
    - **Amphotericin B (25 mg/l):** Antifungal agent.

### Types of Media
- **BME (Basal Medium Eagle):** Originally designed for mouse L and HeLa cells. Simple, essential amino acids.
- **EMEM (Eagle's Minimum Essential Medium):** Used for a wide variety of cell lines; has 2x the amino acids/vitamins of BME.
- **DMEM (Dulbecco's modification of Eagle's medium):** Has 4x the amino acid/vitamin concentration of BME. High glucose.
- **GMEM (Glasgow's modification of Eagle's medium):** Has 2x the amino acid/vitamin concentration of BME.
- **RPMI 1640:** Roswell Park Memorial Institute medium; used for lymphocyte and hybridoma cultures.
- **Leibovitz:** Used for fibroblast growth in the absence of a CO2-enriched atmosphere.
- **Ham's F-12:** Has a complex composition and used for a variety of cell lines.
- **199:** Extremely complex medium (61 components); can support cell growth without serum.

## 4. Characteristics of Cells in Culture

### A. Primary Culture
- **Origin:** Cells derived directly from tissue (mechanical or enzymatic disaggregation).
- **Lifespan:** Finite. Survives 30–50 generations before senescence (Crisis phase).
- **Isolation Methods:**
    - Dissection -> Mincing -> Enzymatic digestion (Trypsin/Collagenase).
    - **Selection:** Use selective media, growth inhibitors, or gradient centrifugation (Ficoll/Percoll) to isolate specific cell types.
- **Morphology:**
    1.  **Fibroblastic:** Bipolar or multipolar, elongated, grow attached to substrate.
    2.  **Epithelial-like:** Polygonal, grow in attached discrete patches.
    3.  **Lymphoblast-like:** Spherical, grow in suspension (do not attach).

### B. Cell Lines (Continuous/Immortalized)
- **Origin:** Primary cultures that have undergone transformation (spontaneous or induced via viral/chemical mutagens).
- **Characteristics:**
    - "Unlimited" cell division (Immortal).
    - Genetically uniform (homogenous).
    - Often tumor-derived.
- **Examples:**
    - **HeLa:** Human cervical carcinoma (Epithelial).
    - **CHO:** Chinese Hamster Ovary (Epithelial).
    - **BHK:** Baby Hamster Kidney (Fibroblast).
- **Growth Curve:**
    1.  **Lag Phase:** Adaptation, no increase in number.
    2.  **Log (Exponential) Phase:** Rapid division.
    3.  **Stationary Phase:** Plateau (confluence/nutrient depletion).
    4.  **Decline/Death Phase:** Accumulation of waste/toxins.

## 5. Cell Identity & Isolation Techniques
To classify or sort cells based on markers or physical properties.

### Flow Cytometry
- Analyzes cells in a fluid stream using lasers.
- **Parameters:**
    - **FSC (Forward Scatter):** Correlates with **Size**.
    - **SSC (Side Scatter):** Correlates with **Granularity/Internal complexity**.
- **Biomarkers (Immunophenotyping):** Uses fluorescently labeled antibodies.
    - Example: T-cell identification.
    - T-cells: `CD3+`
    - T-helper: `CD3+`, `CD4+`
    - T-cytotoxic: `CD3+`, `CD8+`

#### Apoptosis Analysis (Annexin V / PI)
- **The Axes**:
    - **X-Axis (Annexin FITC)**: Measures Annexin V (binds to cells in early apoptosis).
    - **Y-Axis (PI)**: Measures Propidium Iodide (stain for dead/dying cells with broken membranes).
- **The Quadrants**:
    - **Bottom Left (LL)**: Live, Healthy Cells (Negative for both).
    - **Bottom Right (LR)**: Early Apoptosis (Annexin positive, PI negative).
    - **Top Right (UR)**: Late Apoptosis / Necrosis (Positive for both).
- **Comparison Example**:
    - **Plot A (Untreated)**: Control; most dots clustered in the bottom-left (Live).
    - **Plot B (Treated - 10nM Doc)**: Significant shift right and up, indicating cell death progression.

### Magnetic Cell Sorting (MACS)
- Uses antibodies conjugated to magnetic microbeads.
- **Process:**
    1.  Label cells with magnetic antibodies.
    2.  Pass through a column in a magnetic field.
    3.  **Positive Selection:** Labeled cells stick to the column; elute after removing magnet.
    4.  **Negative Selection (Depletion):** Unlabeled cells flow through; labeled unwanted cells stay in column.
