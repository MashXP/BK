# Chapter 1: Nucleic Acids Extraction and Purification

## Course Overview: Gene Technology
- **Instructor**: Assoc. Prof. Dr. Hoang Anh Hoang
  - Email: `hoang.a.hoang@hcmut.edu.vn`
  - Phone: 0906 318 412
- **Assessment / Evaluation Scheme**:
  - **Experiment (Lab)**: 30%
  - **Midterm Exam (Written Test)**: 10%
  - **Seminar**: 10%
  - **Final Exam (Written Test)**: 50%

### Course Syllabus Structure
1. **Chapter 1**: Nucleic acids extraction and purification
2. **Chapter 2**: PCR and electrophoresis
3. **Chapter 3**: Vectors and cloning
4. **Chapter 4**: Blotting methods
5. **Chapter 5**: Sequencing
6. **Chapter 6**: Gene transfer in microorganisms
7. **Chapter 7**: Gene transfer in other organisms
8. **Chapter 8**: Recombinant proteins and detection methods
- **Seminar**: Applications of gene technology

### Key References & Textbooks
- Primary: Lecture Slides
- Old, R.W. & Primrose, S.B. *Principles of Gene Manipulation*. Blackwell Scientific Publication, 2008.
- Sambrook, J., Fritsch, E.F. & Maniatis, T. *Molecular Cloning: A Laboratory Manual*, 3rd ed., Cold Spring Harbor Laboratory Press, 2001.
- Newton, C.R. & Graham, A. *PCR*. BIOS Scientific Publishers Limited, 1994.
- Glick, B.R. & Pasternak, J.J. *Molecular Biotechnology: Principles and Applications of Recombinant DNA*. ASM Press, 2010.
- Watson, J.D. et al. *Molecular Biology of the Gene*, 7th ed., Cold Spring Harbor Laboratory Press / Pearson, 2014.
- Gerstein, A.S. *Molecular Biology Problem Solver (A Laboratory Guide)*. Wiley-Liss, 2001.
- Gellissen, G. *Production of Recombinant Proteins*. Wiley-VCH, 2005.

---

## Chapter 1 Outline
1. **Section I**: Introduction
2. **Section II**: Extraction of Nucleic Acids
3. **Section III**: Quantification and Purification of Nucleic Acids
4. **Section IV**: Plasmid Extraction (Experiment / Laboratory Protocol)

---

## I. Introduction to Nucleic Acids Extraction

### 1. Biological Genomes & Composition
- **Genomic Material by Organism**:
  - **Prokaryotes & Eukaryotes**: Double-stranded DNA (dsDNA) serves as the primary genetic repository.
  - **Viruses**: Can possess either DNA or RNA genomes (single- or double-stranded, positive/negative sense).
- **Nucleic Acid Polymerization**:
  - Monomer: **Nucleotide** (composed of a pentose sugar, a nitrogenous base attached to C1', and phosphate group(s) attached to C5').
  - Phosphodiester bond formation: Condensation reaction releasing $\text{H}_2\text{O}$ between the 5'-phosphate of an incoming nucleotide and the 3'-OH group of the growing chain, forming a $5' \to 3'$ directionality.

### 2. Objectives and Applications of Nucleic Acid Extraction
- **Pathogen Detection**: Identification of viruses, bacteria, and fungi in clinical and environmental samples.
- **Molecular Diagnosis**: Identifying genetic mutations, hereditary disorders, and oncogenic markers.
- **General Testing**: Forensic testing, paternity testing, identity verification.
- **Food Safety & Environmental Monitoring**: Detecting foodborne pathogens, GMO verification, and environmental metagenomics.
- **Research & Development (R&D)**: Molecular cloning, gene editing, transcriptome analysis, and sequencing.

### 3. Cellular Barriers and Lysis Principles
- **Extraction Definition**: A fundamental biochemical process to isolate DNA or RNA from diverse biological sources (blood, animal/plant tissues, cell cultures, microorganisms).
- **Target Boundaries**:
  - **Animal Cells**: Enclosed only by a phospholipid bilayer plasma membrane.
  - **Plant Cells**: Enclosed by a rigid cellulose/pectin cell wall outside the cell membrane.
  - **Bacterial Cells**: Possess a peptidoglycan cell wall (Gram-positive: thick peptidoglycan; Gram-negative: outer membrane + thin peptidoglycan layer).
- **Lysis Sequence**:
  $$\text{Intact Cell} \xrightarrow{\text{Cell Wall / Membrane Lysis}} \text{Lysate} \xrightarrow{\text{Nuclear Membrane Lysis (Eukaryotes)}} \text{Nucleic Acid Release}$$
- **Core Biochemical Rationale**: DNA, RNA, and plasmids exhibit similar polyanionic and hydrophilic properties due to their negative phosphate backbones, allowing shared principles across extraction methods.

---

### 4. General Workflow Stages
The extraction pipeline universally consists of four major sequential steps:
1. **Sample Collection & Preparation**: Harvesting cells/tissues, mechanical homogenization if necessary.
2. **Cell Lysis**: Chemical/enzymatic breakdown of membranes and walls, releasing intracellular contents.
3. **Separation**: Partitioning nucleic acids away from cellular debris, denatured proteins, and lipids.
4. **Purification & Precipitation**: Desalting, washing, and concentrating the nucleic acid pellet.

```mermaid
flowchart LR
    A["Cell Suspension"] -->|"Lysis: Tris, EDTA, SDS"| B["Lysate"]
    B -->|"Protein Removal: Phenol/Chloroform or Salts"| C["Aqueous Phase (DNA/RNA)"]
    C -->|"Precipitation: Isopropanol / EtOH"| D["Purified Nucleic Acid Pellet"]
```

---

## II. Nucleic Acids Extraction Methods

### Classification of Extraction Methodologies
| Extraction Class | Specific Methods | Key Characteristics |
| :--- | :--- | :--- |
| **Liquid-Phase Extraction** | Phenol-Chloroform Extraction; Salting-out / Proteinase K method | High yield, cost-effective, but involves hazardous organics and manual phase-separation |
| **Solid-Phase Extraction** | Silica-membrane spin columns | Fast, standardized, eliminates toxic solvents, optimal for routine molecular biology |
| **Magnetic Bead Technology** | Paramagnetic silica/carboxyl beads | Highly scalable, automatable, ideal for robotic high-throughput processing |

---

### II.1. Liquid-Phase: The Phenol-Chloroform Method

#### Step 1: Reagents for Cell Lysis & Stabilization
- **SDS (Sodium Dodecyl Sulphate)**:
  - Anionic detergent that disrupts the phospholipid bilayer of the plasma membrane.
  - Solubilizes membrane lipids into mixed micelles and denatures cellular proteins.
- **Phenol-Chloroform Mixture**:
  - Strongly denatures polypeptides by disrupting secondary and tertiary protein structures.
  - Exposes hydrophobic residues, rendering proteins insoluble in the aqueous phase.
- **Tris Buffer (Tris-HCl)**:
  - Stabilizes and buffers pH (typically pH 8.0 for DNA partitioning into aqueous layer).
- **EDTA (Ethylenediaminetetraacetic acid)**:
  - Chelates divalent metal ions (notably $\text{Mg}^{2+}$ and $\text{Ca}^{2+}$).
  - Deprives endogenous nucleases (DNases/RNases) of essential catalytic cofactors, preventing nucleic acid degradation.

#### Step 2: Phase Separation
Following thorough mixing and centrifugation, the mixture resolves into three distinct stratified phases:

```
+-------------------------------------------------------+
|  1. UPPER LAYER (Aqueous Phase, Top)                 |
|     -> Contains dissolved hydrophilic Nucleic Acids   |
|        (DNA, RNA) and salts                           |
+-------------------------------------------------------+
|  2. MIDDLE LAYER (Interphase)                        |
|     -> Contains coagulated, denatured proteins and   |
|        cellular debris                                |
+-------------------------------------------------------+
|  3. BOTTOM LAYER (Organic Phase, Bottom)              |
|     -> Contains Phenol, Chloroform, lipids, and       |
|        hydrophobic cellular compounds                 |
+-------------------------------------------------------+
```
- **Operational Protocol**: Carefully pipet the upper aqueous phase into a clean microcentrifuge tube without disturbing the proteinaceous interphase. Extraction with chloroform/phenol can be repeated 1–3 times until the interphase is completely clear.

#### Step 3: Precipitation and Storage of Nucleic Acids
1. **Alcohol & Salt Precipitation**:
   - Monovalent cations (e.g., $\text{Na}^+$ from sodium acetate or $\text{NH}_4^+$) neutralize the repulsive negative charges of phosphate backbones.
   - Ethanol ($100\%$) or Isopropanol decreases the dielectric constant of the aqueous solvent, driving DNA/RNA out of solution to form a visible white precipitate.
2. **Washing**:
   - Centrifuge to pellet nucleic acids.
   - Wash pellet with **$70\%$ Ethanol** ($\text{EtOH}$): Solubilizes and removes co-precipitated salts without dissolving long nucleic acid chains.
3. **Drying & Resuspension**:
   - Air-dry or vacuum-dry pellet until residual ethanol evaporates completely.
   - Dissolve pellet in sterile nuclease-free $\text{H}_2\text{O}$ or **TE Buffer** ($10\text{ mM Tris-HCl}$, $1\text{ mM EDTA}$, $\text{pH } 8.0$).
4. **Storage Conditions**:
   - Short-term: $4^\circ\text{C}$
   - Long-term: $-20^\circ\text{C}$ to $-30^\circ\text{C}$ (or $-80^\circ\text{C}$ for RNA) in TE buffer.

---

### II.2. Liquid-Phase: The Enzymatic (Proteinase K) Method
- **Lysis Buffer Composition**:
  - **Tris-HCl**: Maintains optimal buffering capacity.
  - **EDTA**: Sequester divalent cations ($\text{Mg}^{2+}$) to protect DNA.
  - **SDS**: Solubilizes lipids and disrupts membranes.
  - **Proteinase K**: Replaces hazardous phenol-chloroform.
- **Biochemical Role of Proteinase K**:
  - Serine protease that cleaves peptide bonds adjacent to the carboxylic group of aliphatic and aromatic amino acids.
  - Remains catalytically active in the presence of SDS, EDTA, and elevated temperatures ($50^\circ\text{C}-65^\circ\text{C}$).
  - Inactivates endogenous nucleases (DNases, RNases) and frees genomic DNA tightly wrapped around histones and chromatin proteins.

#### Comparison: Proteinase K vs. Phenol-Chloroform

| Criteria | Proteinase K | Phenol-Chloroform |
| :--- | :--- | :--- |
| **Nucleic Acid Purity** | **Very high**, since proteins are thoroughly degraded. | **High**, but residual phenol/chloroform may remain if washing is insufficient $\to$ can affect PCR/enzymatic assays. |
| **Working Conditions** | Active in the presence of SDS, EDTA, salts.<br>Thermostable (up to $50-65^\circ\text{C}$). | Requires multiple steps (solvent addition, mixing, centrifugation).<br>Must be handled in a fume hood due to high toxicity. |
| **Advantages** | • Simple; enzyme acts automatically.<br>• Removes DNases/RNases.<br>• Suitable for many extraction kits. | • Strong, effective protein removal.<br>• Inexpensive and widely used. |
| **Disadvantages** | • Relatively expensive enzyme. | • Toxic, volatile solvents.<br>• Residual solvents may interfere with downstream analysis. |
| **Typical Applications** | Modern DNA/RNA extraction kits (spin columns, magnetic beads). | Traditional extraction method for DNA/RNA (phenol–chloroform extraction). |

---

### II.3. Solid-Phase Extraction: Silica Spin Column Method

The standard commercial methodology for rapid, column-based nucleic acid purification.

```mermaid
flowchart LR
    S1["1. Cell Lysis"] -->|"Chaotropic Salts + Prot K"| S2["2. Silica Binding"]
    S2 -->|"Ethanol Wash Buffers"| S3["3. Column Washing"]
    S3 -->|"Low-salt Buffer / Water"| S4["4. Elution"]
```

#### Core Process Stages
1. **Cell Lysis**:
   - Chemical lysis using detergents combined with Proteinase K digestion.
2. **Silica Binding Mechanism**:
   - Lysate is mixed with **chaotropic salts** (e.g., Guanidinium isothiocyanate, Guanidine hydrochloride).
   - **Mechanism**: Chaotropic agents disrupt the organized hydrogen-bonding network of water molecules and dehydrate the silica surface and phosphate backbone.
   - Positively charged salt cations form a **cation bridge** ($\text{Silica-O}^- \cdots \text{Na}^+ \cdots ^-\text{O-P-DNA}$), enabling tight physical adsorption of nucleic acids onto the silica membrane.
3. **Washing**:
   - Wash buffers containing alcohol ($70\%-80\%$ ethanol) selectively wash through the silica matrix.
   - Effectively removes unbound proteins, polysaccharides, lipids, and residual chaotropic salts while keeping DNA immobilized.
4. **Elution**:
   - Application of a **low-salt buffer** (e.g., $10\text{ mM Tris-Cl}$, $\text{pH } 8.5$ or TE) or nuclease-free water ($\text{pH} \ge 7.0$).
   - **Mechanism**: Low ionic strength and slightly alkaline pH restore the hydration shell, breaking the cation bridge interactions and releasing high-purity DNA into the collection tube.

$$\begin{aligned}
\text{\textbf{Adsorption (Binding)}} &\iff \text{High Chaotropic Salt Concentration} + \text{Acidic/Neutral pH } (\text{pH} \le 7.0) \\
\text{\textbf{Desorption (Elution)}} &\iff \text{Low Salt Concentration / Pure Water} + \text{Alkaline pH } (\text{pH} \ge 7.0 - 8.5)
\end{aligned}$$

---

### II.4. Magnetic Bead–Based Extraction
- **Nanoparticle Composition**: Superparamagnetic nanoparticles (e.g., $\text{Fe}_3\text{O}_4$ core) coated with silica shells or tailored surface functional groups.
- **Workflow**:
  1. Cells lysed in chaotropic buffer; nucleic acids adsorb to magnetic beads via cation bridging.
  2. A magnetic rack/wand applies a localized magnetic field, pulling beads to the vessel wall.
  3. Supernatant containing contaminants (denatured proteins, cell debris, salts) is aspirated without disturbance.
  4. Beads undergo automated wash cycles in $70\%$ EtOH while immobilized.
  5. Nucleic acids are eluted in low-salt buffer and recovered after magnet-assisted bead separation.
- **Key Advantages**:
  - **High Automation & Scalability**: Requires no centrifugation or vacuum manifolds; natively compatible with high-throughput 96/384-well robotic liquid handlers.
  - **Sample Versatility**: Compatible with blood, plasma, tissues, saliva, swabs, and microbial cultures.
  - **High Purity & Integrity**: Produces intact, shear-free DNA/RNA suitable for qPCR, NGS, and precision diagnostics.

---

### II.5. Comprehensive Comparison of Extraction Methodologies

| Parameter | Liquid-Phase (Phenol-Chloroform) | Enzymatic (Proteinase K / Salting-Out) | Solid-Phase (Silica Spin Column) |
| :--- | :--- | :--- | :--- |
| **DNA Yield / Quantity** | **$900 - 1000\text{ ng}$** (Highest) | $700 - 800\text{ ng}$ (High) | $100 - 400\text{ ng}$ (Moderate) |
| **Purity Ratio ($A_{260}/A_{280}$)** | $\sim 1.80 - 1.90$ | $\sim 1.70 - 1.90$ | $\sim 1.80 - 1.88$ (Consistent) |
| **Sample Input Volume** | $500\,\mu\text{L} - 1.5\text{ mL}$ | $500\,\mu\text{L} - 1.5\text{ mL}$ | **$100\,\mu\text{L} - 200\,\mu\text{L}$** (Low input) |
| **Extraction Time** | $\sim 2 - 4\text{ hours}$ (Labor-intensive) | $\sim 2 - 2.5\text{ hours}$ | **$\sim 30 - 45\text{ minutes}$** (Fast) |
| **Cost per Sample** | $+$ (Inexpensive reagents) | $+++$ (Moderate) | $+++++$ (Higher consumable cost) |
| **Hazard / Toxicity** | High (Toxic Phenol/Chloroform vapors) | Low / Safe | Minimal / Safe |
| **Automatability** | Difficult | Moderate | High (with robotic vacuum/spins) |

---

## III. Nucleic Acids Quantification and Quality Control

### 1. Fundamentals & Clinical/Research Importance
- **Definition**: The analytical measurement of the **concentration (yield)** and **purity** of extracted DNA or RNA.
- **Critical Importance**:
  - **Downstream Optimization**: Exact stoichiometry is mandatory for PCR/qPCR amplification efficiency, restriction endonuclease digestion, cloning ligation ratios, and next-generation sequencing library prep.
  - **Experimental Reproducibility**: Prevents sample-to-sample variability and baseline drift.
  - **Error Prevention**: Avoids false negatives, non-specific amplification, or enzyme inhibition caused by template overload or carryover contaminants.

### 2. Spectrophotometric Quantification (Beer-Lambert Law)

Spectrophotometry measures the attenuation of light at specific ultraviolet (UV) wavelengths passing through a sample solution.

$$\mathbf{A = \varepsilon \cdot c \cdot l}$$

Where:
- $A$: UV absorbance (dimensionless / Absorbance Units, $\text{AU}$)
- $c$: Nucleic acid concentration ($\mu\text{g/mL}$ or $\text{ng}/\mu\text{L}$)
- $\varepsilon$: Specific extinction coefficient ($\text{mL}/(\mu\text{g}\cdot\text{cm})$)
  - $\varepsilon_{\text{dsDNA}} = \mathbf{0.020\text{ mL}/(\mu g\cdot cm)}$
  - $\varepsilon_{\text{RNA}} = \mathbf{0.025\text{ mL}/(\mu g\cdot cm)}$
  - $\varepsilon_{\text{ssDNA}} \approx 0.030\text{ mL}/(\mu\text{g}\cdot\text{cm})$
- $l$: Light path length in centimeters ($l = 1.0\text{ cm}$ in standard cuvette)

#### Practical Concentration Formulas ($1\text{ cm}$ pathlength)
- **Double-Stranded DNA (dsDNA)**:
  $$c_{\text{dsDNA}} = \frac{A_{260}}{\varepsilon_{\text{dsDNA}}} = \frac{A_{260}}{0.020} = \mathbf{A_{260} \times 50\,\mu\text{g/mL}} \quad (\text{or } 50\,\text{ng}/\mu\text{L} \text{ per } 1.0\,A_{260})$$

- **Single-Stranded RNA (ssRNA)**:
  $$c_{\text{RNA}} = \frac{A_{260}}{\varepsilon_{\text{RNA}}} = \frac{A_{260}}{0.025} = \mathbf{A_{260} \times 40\,\mu\text{g/mL}} \quad (\text{or } 40\,\text{ng}/\mu\text{L} \text{ per } 1.0\,A_{260})$$

- **Single-Stranded DNA / Oligonucleotides**:
  $$c_{\text{ssDNA}} = \mathbf{A_{260} \times 33\,\mu\text{g/mL}}$$

---

### 3. Purity Assessment & Absorbance Ratios

#### Characteristic Absorption Wavelengths
- **$\mathbf{260\text{ nm}}$ (Peak Absorbance)**: Maximum absorption by purine (Adenine, Guanine) and pyrimidine (Cytosine, Thymine, Uracil) aromatic ring systems in nucleic acids.
- **$\mathbf{280\text{ nm}}$ (Protein Contamination)**: Maximum absorption by aromatic amino acids (Tryptophan, Tyrosine, Phenylalanine) present in proteins.
- **$\mathbf{230\text{ nm}}$ (Chemical / Salt Contamination)**: Absorption by organic compounds, chaotropic salts (e.g., guanidine thiocyanate, guanidine hydrochloride), EDTA, carbohydrates, peptides, and residual phenol.

#### Standard Quality Purity Thresholds
| Parameter | Pure DNA | Pure RNA | Contaminant Indicated if Lower |
| :--- | :--- | :--- | :--- |
| **$\mathbf{A_{260} / A_{280}}$ Ratio** | **$\sim 1.80$** (Acceptable: $1.70 - 1.90$) | **$\sim 2.00$** (Acceptable: $1.90 - 2.10$) | Protein contamination, aromatic solvents, or phenol carryover ($< 1.6$) |
| **$\mathbf{A_{260} / A_{230}}$ Ratio** | **$\sim 1.80 - 2.00$** (Acceptable: $> 1.80$) | **$\sim 2.00 - 2.20$** (Acceptable: $> 1.80$) | Chaotropic salts, residual guanidine, EDTA, polysaccharides, or phenol ($< 1.8$) |

> [!NOTE]
> RNA exhibits a higher theoretical $A_{260}/A_{280}$ ratio ($\sim 2.0$) than DNA ($\sim 1.8$) due to the higher intrinsic absorbance of Uracil compared to Thymine at $260\text{ nm}$.

---

## IV. Plasmid Extraction (Experiment Module Overview)

- **Target**: Isolation of extrachromosomal circular plasmid DNA from host bacterial cells (*E. coli*).
- **Core Principle (Alkaline Lysis - Birnboim & Doly method)**:
  1. **Resuspension (Solution I)**: Glucose/Tris/EDTA + RNase A (stabilizes cells, chelates $\text{Mg}^{2+}$, digests RNA).
  2. **Alkaline Lysis (Solution II)**: $\text{NaOH} + \text{SDS}$ (denatures chromosomal DNA, plasmid DNA, and proteins).
  3. **Neutralization (Solution III)**: Potassium acetate ($\text{KOAc}$, $\text{pH } 4.8 - 5.5$) (covalently closed circular plasmids renature rapidly, while large genomic DNA precipitates with $\text{K-SDS}$ protein complex).
  4. **Centrifugation & Recovery**: High-speed spin pellets genomic DNA/protein complexes; clear supernatant containing plasmid DNA is collected and purified via silica column or alcohol precipitation.

*(Detailed bench protocol, volume titrations, and troubleshooting are expanded in the laboratory experiment guide).*

---

## Key Takeaway Summary Checklist
- [x] **Extraction Core**: 4 sequential stages — Cell Lysis $\to$ Phase Separation $\to$ Washing $\to$ Elution/Precipitation.
- [x] **Lysis Reagents**: SDS (membrane lipid solubilization), Tris (pH control), EDTA (cation chelation & nuclease arrest), Proteinase K (protein digestion).
- [x] **Silica Matrix Chemistry**: High chaotropic salt + low pH promotes cation bridge formation ($\text{Si-O}^- \cdots \text{Na}^+ \cdots ^-\text{O-P-DNA}$); low ionic buffer + alkaline pH elutes DNA.
- [x] **Quantification**: $[ \text{dsDNA} ] = A_{260} \times 50\,\mu\text{g/mL}$; $[ \text{RNA} ] = A_{260} \times 40\,\mu\text{g/mL}$.
- [x] **Purity Metrics**: Pure DNA $A_{260}/A_{280} \approx 1.8$, $A_{260}/A_{230} \approx 1.8-2.0$; Pure RNA $A_{260}/A_{280} \approx 2.0$.
