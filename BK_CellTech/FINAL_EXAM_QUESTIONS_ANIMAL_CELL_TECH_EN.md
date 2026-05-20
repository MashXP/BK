# Final Exam Questions: Animal Cell Technology
*Translated & Formatted study reference from `CÂU HỎI CUỐI KỲ MÔN CÔNG NGHỆ TẾ BÀO ĐỘNG VẬT.txt`*

---

### 1. Describe how to isolate a target cell population expressing two simultaneous markers from the same tissue.

*   **Cell suspension preparation:** Centrifuge the suspension containing the cells at an appropriate speed $\rightarrow$ discard the supernatant and collect the single cells.
*   **Initial population assessment:** Measure the two parameters **FSC (Forward Scatter)** and **SSC (Side Scatter)** $\rightarrow$ classify the cell clusters based on the correlation between these two parameters $\rightarrow$ choose appropriate markers for labeling.
*   **Antibody labeling:** Add two fluorescently labeled antibodies (e.g., Ter119 and CD71) to diffuse into the single-cell suspension from the same tissue.
*   **Flow Cytometry analysis:** Run the mixture through a Flow Cytometer across a laser beam and read the signals. There are 4 possible cases:
    1.  Double-positive (expressing both markers)
    2.  Single-positive for marker 1
    3.  Single-positive for marker 2
    4.  Double-negative
    *Note: The excitation wavelength and binding positions on each cell will differ.*
*   **Interpretation & Sorting:** If the fluorescence intensity of the sample is higher than the negative control $\rightarrow$ the cell is positive for the fluorescently labeled antibody. (The further apart the two signal peaks on the histogram are, the clearer the positive result). Select and collect the double-positive population.

---

### 2. Describe the structure of a cultivation system of your choice.

#### **CELLine Bioreactor**
*   **Compartment Separation:** Designed with separate chambers for the growth medium and product collection, divided by a **10 kDa semi-permeable membrane**. This membrane allows continuous diffusion of nutrients into the cell compartment $\rightarrow$ providing the cells with a constantly fresh environment and minimizing contamination. Consequently, cell growth is less inhibited by secondary metabolites they produce.
*   **Gas Exchange:** Efficient gas transfer is ensured by a **silicone membrane** forming the base of the cell compartment. This membrane provides optimal $O_2$ supply and controls $CO_2$ levels by offering a short diffusion pathway directly into the cell space.
*   **Limitations:** Because cell seeding and product/cell harvesting share the same port, there is a high risk of contamination and an increased concentration of inhibitory compounds during manipulation.

---

### 3. Based on structure and function, at which levels can we interact to control animal cells?

*   **Intracellular level:** Using regulatory factors or transcription factors to regulate gene expression; adjusting ion channels to influence cellular activities.
*   **Cell-to-Cell level:**
    *   *Direct interaction:* Communication via receptor-ligand binding on the cell membranes.
    *   *Indirect interaction:* Hormones, cytokines, and other signaling molecules $\rightarrow$ activate or inhibit intracellular signal transduction pathways.
*   **Cell-to-Environment level:** Modifying environmental conditions (biochemistry, light, temperature, etc.) and growth factors.
*   **Molecular (Genetic) level:** Using CRISPR-Cas9 for gene editing $\rightarrow$ altering genetic characteristics; using siRNA, miRNA to reduce or knockdown target protein expression.

---

### 4. State the applications, advantages, and disadvantages of *in vitro* animal cell culture.

*   **Applications:** Gene therapy, stem cell therapy, production of biologically active compounds, regenerative medicine (e.g., artificial skin), and drug pharmacokinetic testing (assessing the effects of active drug compounds on target cells).
*   **Advantages:** Rejuvenated cell lines, genomic and phenotypic uniformity (due to being cultured in the same environment), and highly reproducible physiological activities, metabolic pathways, and division.
*   **Disadvantages:** Difficult long-term preservation, susceptibility to degeneration (due to continuous culture, rapid division, natural mutations, or external factors), and cultivation conditions must be strictly monitored.

---

### 5. Name and state the functions of basic equipment in animal cell culture.

*   **Biosafety Cabinet (Class II or higher):** Provides a sterile working area to prevent contamination and protect the operator.
*   **Standard & $CO_2$ Incubators:** Maintain optimal growth conditions (temperature, humidity, and $CO_2$).
*   **Inverted Microscope:** Visualizes cells attached to the bottom of the vessel (light source is at the top, objective lens is at the bottom).
*   **Centrifuge:** Separates cells from the media.
*   **Liquid Nitrogen Storage Tank:** Long-term cryopreservation of cells.
*   **Laboratory-scale Culture Vessels:** T-flasks, multi-well plates, etc.

---

### 6. State the components and functions of animal cell culture media.

*   **Glucose:** Primary energy source and precursor for biosynthesis.
*   **Fructose:** Alternative carbohydrate source, reduces lactic acid production, and helps stabilize pH.
*   **Amino Acids (0.1 – 0.2 mM):** Essential precursors for protein synthesis.
*   **Salts:** Maintain osmotic pressure.
*   **Bicarbonate / HEPES:** Buffer systems to stabilize pH.
*   **Vitamins and Hormones:** Act as co-factors for metabolism; cells recognize growth-promoting signals via binding.
*   **Phenol Red (pH Indicator):** Monitors pH changes visually (e.g., turning from red to yellow indicates acidic pH, often due to bacterial contamination or overgrowth).
*   **Serum:** Promotes cell growth by providing growth factors, hormones, and cell attachment factors.
*   **Antibiotics:** Penicillin G (inhibits Gram-positive bacteria), Streptomycin (inhibits Gram-negative bacteria), and Amphotericin B (antifungal agent).

---

### 7. Primary cell culture?

*   Selection of specific cell types for culture.
*   Allowing cell proliferation. Fast-growing cell types might eventually dominate the population.
*   Controlling growth medium composition: adding specific growth factors or growth inhibitors.
*   Separating/isolating cells using gradient centrifugation: **Ficoll** and **Percoll**.

---

### 8. Differentiate between primary animal cells and cell lines. How do you develop a primary cell culture into a cell line?

#### **Comparison Table**

| Feature | Primary Cells | Cell Lines |
| :--- | :--- | :--- |
| **Source** | Taken directly from living tissue/organ using mechanical or enzymatic disaggregation | Derived from primary cells via genetic transformation or repeated selection/subculture |
| **Lifespan** | Short (approx. 30–50 generations before senescence) | Indefinite/Infinite (continuous cell division) |
| **Contamination** | Higher risk of contamination | Lower risk of contamination due to continuous passages |
| **Homogeneity** | Heterogeneous (consisting of multiple cell types) | Homogeneous (clonal population from a single cell) |
| **Division Capacity** | Limited | Unlimited/Continuous division |

#### **Steps to develop primary cells into a cell line:**
1.  Harvest the target tissue or organ sample.
2.  Process the tissue (mechanical mincing and enzymatic digestion with trypsin to disrupt intercellular junctions).
3.  Cultivate cells under appropriate conditions and perform continuous subculturing (passages).
4.  Cells proliferate and divide $\rightarrow$ creating populations sharing the same origin.
5.  Introduce genetic transformations to induce immortalization.
6.  Select target cell lines.
7.  Characterize and verify the genotype, biological properties, and functional activity of the cell line.
8.  Cryopreserve.

---

### 9. Describe the SV40 cell immortalization system.

*   **Rb pathway inhibition:** SV40 Large T-antigen binds to the tumor suppressor **pRb** in the active $Rb/E2F$ complex $\rightarrow$ releases the active transcription factor **E2F** $\rightarrow$ drives S-phase-specific gene transcription.
*   **Cell Cycle Progression:** After entering the S phase, CDK2 phosphorylates Rb, causing its degradation. Free E2F binds to the promoter of target genes $\rightarrow$ enhances transcription.
*   **p53 inactivation:** T-antigen also binds to and inactivates the tumor suppressor protein **p53**, preventing cell cycle arrest and apoptosis.

---

### 10. Describe the HPV E6/E7 cell immortalization system.
*(Question listed in source file without body text)*

---

### 11. Describe the Myc cell immortalization system and how Myc expression is regulated.
*(Question listed in source file without body text)*

---

### 12. Describe the Ras cell immortalization system and how Ras expression is managed.
*(Question listed in source file without body text)*

*Note: For detailed mechanisms of questions 10, 11, and 12, refer to the expanded study guide:* [[02_Cell_Line_Establishment#Cell Immortalization Systems|02_Cell_Line_Establishment]]

---

### 13. List some cell analysis methods.
*(Question listed in source file without body text)*

*Note: For detailed cell counting and viability assays, refer to the study guide:* [[03_Cell_Analysis|03_Cell_Analysis]]

---

### 14. Analyze the advantages and disadvantages of using serum, and list some alternatives to serum.

*   **Advantages:** Promotes cell growth (contains growth factors, hormones, etc.); high albumin content acts as a protectant, shielding cells from shear stress and pH fluctuations common in large-scale systems.
*   **Disadvantages:** Undefined chemical composition and variable concentration; high protein content makes downstream purification of recombinant products difficult; ethical concerns regarding collection.
*   **Alternatives:** Peptide hydrolysates, EGF, synthetic growth factors, and chemically defined formulations.

---

### 15. Adherent cell culture protocol and cell detachment methods.

*   **Cultivation:** Grow cells in a horizontal T-flask containing a substrate. Once attached, cells divide and grow until they occupy **~80% of the culture surface (confluence)**.
*   **Cell Detachment:** Add trypsin enzyme and incubate at **37°C for 10 minutes** $\rightarrow$ trypsin hydrolyzes intercellular/substrate protein links, causing cells to round up. Under gentle mechanical agitation, cells detach completely into suspension.
*   **Harvesting:** Aspirate the cell suspension $\rightarrow$ centrifuge $\rightarrow$ wash cells with growth medium (if sensitive) or PBS buffer to neutralize and remove trypsin residues.
*   **Seeding:** Count cells using a hemocytometer to determine density $\rightarrow$ seed into a new flask at a density of **2 – 5 × 10⁵ CFU/ml**.

---

### 16. Suspension cell culture protocol.

*   **Monitoring:** Monitor cell density visually by color change (e.g., purple medium $\rightarrow$ cells are in stationary phase and do not need to divide/be split).
*   **Harvesting:** Trypsin treatment is **not required**. Aspirate the cell suspension $\rightarrow$ centrifuge $\rightarrow$ wash cells with growth medium or PBS buffer.
*   **Seeding:** Count cells using a hemocytometer $\rightarrow$ determine cell density $\rightarrow$ culture cells in a **vertical T-flask** at an appropriate density.

---

### 17. Cell cryopreservation method and thawing method. What are their advantages and disadvantages?

*   **Cryopreservation (Freezing):** Harvest cells $\rightarrow$ determine density $\rightarrow$ add cryoprotectant (e.g., DMSO) slowly $\rightarrow$ place in a refrigerator/pre-cooling container $\rightarrow$ transfer to a -80°C freezer $\rightarrow$ store in liquid nitrogen at **-196°C** (keeps cells viable for over 20 years). Care must be taken to avoid rapid intracellular crystal formation.
*   **Thawing:** Thawing must occur **rapidly** $\rightarrow$ place vial in a 37°C water bath with gentle shaking $\rightarrow$ transfer to fresh medium (volume must be at least double the cell suspension volume to dilute the cryoprotectant) $\rightarrow$ centrifuge gently $\rightarrow$ wash to remove the cryoprotectant $\rightarrow$ return cells to culture.

---

### 18. Describe the cell cultivation process.

*   **Bioreactor Cultivation:** Equilibrate and stabilize culture parameters (pH, DO, temperature) prior to seeding. Ensure cells are in log phase and exist as single cells. Inoculum should occupy **1/3 of the total volume**; stir at the lowest speed to keep microcarriers in a homogeneous suspension. Once cells attach, top up the remaining volume.
*   **Cell Detachment:** Use enzymes (trypsin, protease), EDTA, hypotonic solutions, or a combination of these.
*   **Carrier Separation:** Settling/sedimentation, filtration using a **100 µm mesh**, or density-gradient centrifugation.
*   **Cell Encapsulation:** Enclose cells in capsules $\rightarrow$ protects cells from high concentrations of inhibitory metabolites or secondary products, and shields them from the host immune response.
