# Recombinant Glycoprotein
**Date:** 2026-01-23

## 1. What is a Recombinant Glycoprotein?
- **Definition:** A protein that has carbohydrate chains (glycans) attached to it (glycosylation), produced using genetic engineering techniques (recombinant DNA technology) in a host cell.
- **Structure:**
    - **Protein Backbone:** Determined by the DNA sequence.
    - **Glycan Chains:** Sugars attached to specific amino acid residues (e.g., Asparagine for N-linked, Serine/Threonine for O-linked).
- **Importance:**
    - Many therapeutic proteins (e.g., antibodies, erythropoietin) are glycoproteins.
    - **Function:** Glycans affect protein stability, solubility, half-life in the blood, and biological activity.
    - **Immunogenicity:** Incorrect glycosylation can be recognized as "foreign" by the human immune system, causing reactions.

## 2. How to Get It (Production)
The production process involves inserting the gene for the protein into a cell that has the machinery to attach the sugars (glycosylation).

### A. Host Systems
Not all cells glycosylate proteins the same way.
- **Mammalian Cells (Gold Standard):**
    - **Examples:** CHO (Chinese Hamster Ovary), HEK293 (Human Embryonic Kidney), NS0.
    - **Why?** They produce human-like glycosylation patterns, reducing the risk of immune rejection.
    - **Disadvantage:** Expensive, slower growth, lower yields compared to bacteria.
- **Bacteria (e.g., E. coli):** Generally **do not** perform glycosylation (unless genetically modified to do so).
- **Yeast/Insect Cells:** Perform glycosylation but patterns differ from humans (e.g., high mannose in yeast) which can cause immune issues or rapid clearance.

### B. The Process
1.  **Cloning:** The DNA gene for the desired protein is inserted into a vector (plasmid).
2.  **Transfection:** The vector is introduced into the mammalian host cell.
3.  **Selection:** Cells that successfully incorporated the gene are isolated.
4.  **Expression:** The cell machinery reads the DNA and makes the protein backbone.
5.  **Post-Translational Modification (Glycosylation):** As the protein moves through the ER and Golgi apparatus, enzymes (glycosyltransferases and glycosidases) add and trim sugar chains.

## 3. How to Control It
Glycosylation is not template-driven (unlike DNA->RNA->Protein); it depends on the availability of enzymes and substrates in the cell. Therefore, it causes **Heterogeneity** (mixture of different glycoforms). Controlling this is critical.

### A. Process Parameters (Culture Conditions)
Changing the environment changes the enzyme activity inside the cell.
- **Nutrients:**
    - **Glucose:** Low levels can reduce glycosylation (site occupancy).
    - **Ammonia:** Accumulation (from Glutamine metabolism) inhibits sialylation (a critical terminal sugar).
- **pH & Temperature:** Affect the activity of glycosyltransferase enzymes.
- **Dissolved Oxygen (DO):** Variations can alter the glycan profile.

### B. Genetic Engineering (Glycoengineering)
Modifying the host cell's genome to produce specific glycans.
- **Overexpression:** Adding genes for specific enzymes (e.g., to increase sialylation).
- **Knock-out:** Removing genes for enzymes that add unwanted sugars (e.g., removing fucose to enhance antibody cytotoxicity).

### C. Monitoring & Quality Control
- **Analysis:** Techniques like Mass Spectrometry and HPLC are used to verify the glycan structures.
- **Consistency:** The goal is to maintain a "Consistent Glycan Profile" across batches to ensure safety and efficacy.

### D. Purification
- To obtain the final product.

---

# Viral Vaccines
**Date:** 2026-01-23

## 1. What is a Viral Vaccine?
- **Definition:** A biological preparation that provides active acquired immunity to a particular viral disease. It contains an agent that resembles the disease-causing virus.
- **Goal:** To stimulate the body's immune system to recognize the agent as a threat, destroy it, and "remember" it (immunological memory), so the immune system can more easily recognize and destroy any of these microorganisms that it later encounters.
- **Types of Viral Vaccines:**
    - **Live Attenuated:** Weakened form of the virus (e.g., Measles, Mumps, Rubella - MMR). Strong, long-lasting immunity but risk of reversion.
    - **Inactivated (Killed):** Virus is destroyed (e.g., Polio, Hepatitis A). Safer, but often requires boosters.
    - **Subunit:** Contains only specific parts (antigens) of the virus (e.g., Hepatitis B).
    - **Viral Vector:** Uses a harmless virus to deliver viral genes (e.g., Ebola, some COVID-19 vaccines).

## 2. How to Get It (Production)
Traditional methods used chicken eggs, but **Animal Cell Technology** is now the preferred modern method for scalability and safety.

### A. Host Systems
- **Primary Cells:** Cells derived directly from tissue (e.g., Monkey Kidney cells for Polio). Risk of contamination from donor animal.
- **Diploid Cell Strains:** Normal human cells (e.g., WI-38, MRC-5). Finite lifespan, well-characterized, safe.
- **Continuous Cell Lines:** Immortal cells (e.g., Vero cells - African Green Monkey Kidney, MDCK, PER.C6).
    - **Advantage:** Can be grown in large bioreactors (suspension or microcarriers), high yields.
    - **Concern:** Tumorigenic potential (require rigorous purification to remove DNA).

### B. The Process
1.  **Cell Growth:** Host cells are expanded in bioreactors (from small scale to thousands of liters) using optimized media.
2.  **Infection (Inoculation):** The "Seed Virus" is added to the culture when cell density is optimal.
3.  **Viral Replication:** The virus enters the cells, hijacks the machinery, and replicates. Conditions (Temp, pH, DO) are controlled to maximize viral yield.
4.  **Harvesting:**
    - **Lytic Viruses:** Cells burst open; harvest the supernatant.
    - **Non-lytic Viruses:** Virus is secreted; harvest the supernatant or lyse cells mechanically.
5.  **Downstream Processing:**
    - **Clarification:** Remove cell debris (Centrifugation/Filtration).
    - **Purification:** Ultrafiltration/Chromatography to isolate the virus.
    - **Inactivation (if applicable):** Chemical (Formalin, Beta-propiolactone) or Physical (UV/Gamma radiation) treatment to kill the virus while preserving structure.

## 3. How to Control It (Quality & Safety)
Ensuring the vaccine is safe and effective is paramount.

### A. In-Process Controls
- **Cell Substrate:** Must be free from adventitious agents (bacteria, fungi, mycoplasma, other viruses).
- **Growth Parameters:** Monitoring pH, DO, temperature, and nutrient levels to ensure consistent viral replication.
- **Viral Titer:** Measuring the amount of virus produced during the process (e.g., Plaque Assay, TCID50).

### B. Final Product Testing
- **Sterility:** No bacterial or fungal contamination.
- **Identity:** Confirming it is the correct virus (PCR, Serological tests).
- **Potency:** Measuring the ability to induce an immune response (Animal models or In vitro assays).
- **Purity:**
    - Removal of Host Cell Proteins (HCP).
    - **Residual DNA:** For continuous cell lines, host DNA must be reduced to safe levels (<10 ng/dose) to prevent potential oncogenic risks.
- **Safety/Inactivation:** Verifying that *no* live virus remains (for inactivated vaccines).

---

# Monoclonal Antibodies (mAbs)
**Date:** 2026-01-23

## 1. What are Monoclonal Antibodies?
- **Definition:** Antibodies that are identical clones derived from a single parent immune cell. They bind to the same specific part (epitope) of an antigen.
- **Structure:** Y-shaped proteins (Immunoglobulins) consisting of two heavy chains and two light chains. The tips of the "Y" are the variable regions that determine specificity.
- **Applications:**
    - **Therapeutic:** Treating cancer (targeting tumor cells), autoimmune diseases, and infectious diseases.
    - **Diagnostic:** Pregnancy tests, detecting pathogens.
    - **Research:** Identifying specific proteins in cells.

## 2. How to Get It (Production)
There are two main technologies: the traditional Hybridoma method and the modern Recombinant method.

### A. Hybridoma Technology (Traditional)
1.  **Immunization:** Inject a mouse with the specific antigen.
2.  **Isolation:** Harvest B-cells (plasma cells) from the mouse spleen. These produce antibodies but die quickly in culture.
3.  **Fusion:** Fuse B-cells with Myeloma cells (cancerous B-cells that live forever but don't produce antibodies) using PEG (Polyethylene Glycol).
4.  **Selection:** Grow in **HAT Medium**.
    - Unfused Myeloma cells die (cannot survive in HAT).
    - Unfused B-cells die (short lifespan).
    - Only **Hybridomas** survive (Immortal + Antibody producing).
5.  **Screening:** Test individual clones to find the one producing the desired antibody.
6.  **Cloning:** Isolate the single best cell and expand it.

### B. Recombinant Technology (Modern/Industrial)
Used for large-scale production and making "Humanized" or "Fully Human" antibodies (to prevent immune rejection of mouse antibodies).
1.  **Gene Isolation:** Identify the DNA sequence for the antibody (Heavy and Light chains).
2.  **Vector Construction:** Insert genes into expression vectors.
3.  **Host Cells:** **CHO (Chinese Hamster Ovary)** and **NS0** cells are the industry standard because they perform proper folding and glycosylation.
4.  **Transfection & Selection:** Introduce vectors into host cells and select for high producers (often using gene amplification systems like GS or DHFR).
5.  **Production:** Large-scale fed-batch culture in bioreactors (up to 20,000L).

## 3. How to Control It
Consistency and purity are critical for safety and efficacy.

### A. Product Quality (Characterization)
- **Specificity:** Must bind *only* to the target antigen.
- **Glycosylation:** Critical for effector function (ADCC/CDC) and half-life. Must be monitored closely (e.g., afucosylation enhances killing of cancer cells).
- **Aggregates:** Antibodies sticking together can cause immune reactions. Must be minimized.

### B. Impurity Control
- **Process-Related Impurities:** Host cell proteins (HCP), Host cell DNA, Leached Protein A (from purification), Media components.
- **Product-Related Impurities:** Fragments, Aggregates, Oxidized variants.

### C. Purification (Downstream Processing)
Standard platform process:
1.  **Harvest:** Centrifugation/Filtration.
2.  **Protein A Affinity Chromatography:** specifically binds the Fc region of the antibody (captures >95% purity).
3.  **Viral Inactivation:** Low pH hold.
4.  **Polishing:** Ion Exchange Chromatography (to remove aggregates, DNA, HCP).
5.  **Viral Filtration:** Removes any remaining viruses.