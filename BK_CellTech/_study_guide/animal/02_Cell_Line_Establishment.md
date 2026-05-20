# Cell Line Establishment
**Date:** 2026-02-06
**Source:** AlCellTech.pdf (Chapter 2, Slides 25-38)

## 1. Process of Establishment
The transition from tissue to a continuous cell line involves several stages:
1.  **Tissue/Organ Fragment**: Starting material.
2.  **Primary Culture**: Cells proliferate after outgrowth/attachment.
3.  **Subculture**: Passage of cells.
4.  **Cell Line**:
    *   **Senescence**: Normal cells eventually stop dividing (finite lifespan).
    *   **Immortalization**: Leads to a continuous cell line.
5.  **Continuous Cell Line**:
    *   Can become a **Transformed Cell Line** via loss of growth control.

## 2. Normal vs. Transformed Cells

| Feature | Normal Cells | Transformed Cells |
| :--- | :--- | :--- |
| **Anchorage** | Anchorage dependent (except haemopoietic) | Reduced dependence (can grow in agar) |
| **Inhibition** | Density-dependent / Contact inhibition | Reduced contact inhibition / Density inhibition |
| **Lifespan** | Finite (10-100 doublings) | Infinite (Immortal) |
| **Genetics** | Stable | Unstable (Heteroploid/Aneuploid) |
| **Growth Factors** | High requirement | Reduced requirement (less serum needed) |
| **Doubling Time** | Standard | Reduced (Faster growth) |

## 3. The Cell Cycle
The cell cycle consists of four distinct phases:
*   **G1 Phase**: Preparation for DNA replication. (Synthesize proteins/enzymes).
*   **S Phase**: DNA Replication (Synthesis).
*   **G2 Phase**: Preparation for mitosis.
*   **M Phase**: Mitosis (Cell division).

*Regulation involves Cyclins and Cyclin-Dependent Kinases (CDKs).*

## 4. Telomeres and Telomerase
### Telomeres
*   **Function**:
    *   Protect chromosome ends from degradation.
    *   Facilitate chromosome movement during meiosis.
    *   Compensate for the loss of terminal sequences during DNA replication ("End replication problem").
*   **In Vitro Aging**:
    *   As normal cells divide, telomeres shorten.
    *   **Characteristics of aging fibroblasts**: Increased doubling time, decreased adhesion, altered cytoskeleton, shortened telomeres.

### Telomerase
*   **Function**: Enzyme that synthesizes chromosome ends (extends telomeres), preventing shortening.
*   **Activity**: Active in germ cells, stem cells, and cancer cells (immortalized cells). Inactive in most somatic cells.

## 5. Cell Immortalization Systems
Immortalization allows cells to bypass senescence.

### Mechanisms
*   **hTERT Expression**: Reactivation of Telomerase Reverse Transcriptase.
*   **Oncogene Expression**: c-myc, ras.
*   **Tumor Suppressor Inactivation**: pRB, p53, SEN6.

### Viral Immortalization Systems
Viral systems bypass senescence by targeting the cell cycle "guardians": **p53** and **pRb**.

#### 1. SV40 (Simian Virus 40) Large T-Antigen
The most common system for mammalian cells.
*   **Mechanism vs. pRb**: T-antigen binds **pRb**, releasing the transcription factor **E2F**. Free E2F induces S-phase gene transcription.
*   **Mechanism vs. p53**: T-antigen sequesters and inactivates **p53**, blocking apoptosis and G1 arrest.
*   **Efficiency**: Very high, but can lead to genomic instability (aneuploidy).

#### 2. HPV (Human Papillomavirus) E6/E7
Preferred for epithelial cells; more targeted than SV40.
*   **E6 (p53 Destroyer)**: Recruits ubiquitin ligase to **p53** for proteasomal degradation. Also induces **hTERT** (telomerase) expression.
*   **E7 (pRb Inactivator)**: Binds to **pRb**, displacing **E2F**. Can also trigger pRb degradation.

#### 3. EBV (Epstein-Barr Virus)
The gold standard for creating **human B-lymphocytes** (LCLs).
*   **LMP-1**: Mimics a constitutively active CD40 receptor, triggering NF-κB and PI3K/Akt survival pathways.
*   **EBNA-2**: Transcriptional activator of host genes like *c-myc*.

#### 4. Myc Immortalization System
*c-Myc* is a transcription factor that drives expression of genes needed for cell-cycle entry (Cyclin D, CDK4, E2F targets).

**Immortalization mechanism:**
*   Overexpressed Myc suppresses p21/p27 (CDK inhibitors) and activates **hTERT** (telomerase), bypassing replicative senescence.
*   Used in combination with p53/Rb inactivation (e.g., SV40 or E6/E7) to prevent **Oncogene-Induced Senescence (OIS)**.

**Regulating Myc expression:**
*   **Transcriptional control:** Wnt, Notch, and MAPK/ERK growth factor pathways induce *c-myc* transcription; withdrawal of growth signals suppresses it.
*   **Post-translational stability:**
    *   **Phospho-S62 (stabilizing):** Activated by Ras/ERK → protects Myc from degradation.
    *   **Phospho-T58 (destabilizing):** Activated by GSK-3β → recruits Fbxw7 ubiquitin ligase → proteasomal degradation.
    *   **MycT58A mutant**: T58A substitution prevents GSK-3β phosphorylation → constitutively stable Myc used for robust immortalization.
*   **Inducible systems:** Tet-On (doxycycline-controlled) promoters allow researchers to switch Myc expression on/off experimentally.

#### 5. Ras Immortalization System
Ras is a **GTPase signal transducer** located downstream of growth factor receptors; it propagates proliferative signals via **MAPK/ERK** and **PI3K/Akt** pathways.

**Immortalization mechanism:**
*   Normal Ras cycles between GTP-bound (active) and GDP-bound (inactive) states.
*   **RasV12 (G12V mutant):** Point mutation abolishes intrinsic GTPase activity → Ras is locked in the GTP-bound active state → constitutive proliferative signaling.
*   Downstream: MAPK/ERK drives cyclin D expression; PI3K/Akt inhibits apoptosis.

**Managing Ras expression:**
*   **GEFs (Guanine nucleotide Exchange Factors):** Promote GDP→GTP exchange → activate Ras.
*   **GAPs (GTPase-Activating Proteins):** Stimulate GTP hydrolysis → inactivate Ras. (RasV12 is insensitive to GAPs.)
*   **Inducible expression systems (Tet-On/Tet-Off):** Allow conditional activation/silencing of RasV12 to study its effects or avoid OIS during establishment.
*   **Combination with p53 inactivation:** Required because constitutive Ras signaling triggers p53-dependent OIS in normal cells; combining RasV12 with SV40 T-antigen or E6/E7 overcomes this.
*   **Downstream inhibitors:** MEK inhibitors (e.g., PD98059) or PI3K inhibitors can be used to titrate signaling output experimentally.
