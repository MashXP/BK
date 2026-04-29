# Chapter 7: Some Basic Techniques

## 1. Cloning
Cloning is a fundamental technique in molecular biology used to create identical copies of DNA fragments. The general workflow involves:
1.  **Preparation**: Generating a PCR product (insert) and selecting a vector (plasmid).
2.  **Annealing/Ligation**: 
    - The insert and vector are digested with specific **Restriction Enzymes** (e.g., BamHI, EcoRI, SalI) to create compatible ends.
    - They are then joined together using DNA Ligase.
3.  **Transformation**: The recombinant vector is introduced into a host cell (e.g., *E. coli*).
4.  **Selection**: Antibiotics are used to select for cells that have successfully taken up the plasmid.
5.  **Verification**: Sequencing confirms the correct insert is present.
6.  **Expression & Purification**: The protein is expressed (small to large scale) and purified, often using **Affinity Chromatography**. Verifiction is often done via **SDS-PAGE** (protein gel).

### Example Vector: pET-28a(+)
- **Size**: 5369 bp
- **Markers**: Kanamycin resistance (Kan), lacI (for regulation).
- **Origins**: f1 origin, ori.
- **Multiple Cloning Site (MCS)**: Contains sites for XhoI, NotI, EagI, HindIII, SalI, SacI, EcoRI, BamHI, NheI, NdeI, NcoI.
- **Restriction Site Examples**:
    - **BamHI**: `5'...G G A T C C...3'`
    - **HindIII**: `5'...A A G C T T...3'`

---

## 2. PCR (Polymerase Chain Reaction)
PCR is used to amplify specific DNA sequences.

### Components
- **DNA Template**: The genetic code to be copied.
- **Nucleotides (dNTPs)**: AGCT, the building blocks for the new DNA strand.
- **Primers**: Short, specific DNA sequences that bracket the target region.
- **Reaction Buffer + Water**: Provides the chemical environment for the reaction.
- **Taq Polymerase**: A heat-stable enzyme that reads the original DNA and synthesizes the complementary copy.
- **Probes**: For specialized techniques (like qPCR/TaqMan), specially labelled probes are required.

### Routine PCR Thermocycling Conditions
| Step | Temperature | Time |
| :--- | :--- | :--- |
| Initial Denaturation | 95°C | 30 seconds |
| **30 Cycles** | | |
| - Denaturation | 95°C | 15-30 seconds |
| - Annealing | 45-68°C | 15-60 seconds |
| - Extension | 68°C | 1 minute/kb |
| Final Extension | 68°C | 5 minutes |
| Hold | 4-10°C | |

---

## 3. Molecular Hybridization (Blotting)
These techniques are used to detect specific macromolecules:
- **Southern Blot**: Detects **DNA**.
- **Northern Blot**: Detects **mRNA**.
- **Western Blot**: Detects **Proteins** (following protein synthesis/translation).

---
