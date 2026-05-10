# Chapter 11: Viral Genetics

## 1. Life Cycles of Bacteriophages
Viruses that infect bacteria (bacteriophages) generally follow two life cycles:
- **Lytic Cycle**: The virus replicates rapidly and lyses (kills) the host cell to release new viral particles.
- **Lysogenic Cycle**: The viral DNA integrates into the host chromosome as a **prophage** and is replicated along with the bacterial DNA. It can later be induced to enter the lytic cycle.

---

## 2. Viral Genetic Mapping
Mapping can be performed within viruses to determine the relative order and distance of mutations.

### Intragenic Mapping (Fine Structure Mapping)
- Used to establish distances between two or more mutations located **within the same gene**.
- **Experiment (Benzer)**: Coinfect *E. coli* B with two different non-complementing mutants (e.g., `r103` and `r104`).
- **Mechanism**: Rare recombination within the gene produces wild-type phages and double mutants.
- **Measurement**: 
    - Total phages are measured by infecting *E. coli* B.
    - Recombinant (wild-type) phages are measured by infecting *E. coli* K12(lambda), where only wild-type can grow.
- **Calculation**:
    - `Frequency of recombinants = 2 * [Wild-type plaques in E. coli K12(λ)] / [Total number of plaques in E. coli B]`
    - **Rationale**: The factor of 2 accounts for the double mutants which are not detected but produced in equal numbers to wild-type.
    - **Example (Source: Page 69)**:
        - Wild-type plaques on K12: $11 \times 10^6$
        - Total plaques on B: $6.6 \times 10^9$
        - $RF = \frac{2 \times (11 \times 10^6)}{6.6 \times 10^9} = 3.3 \times 10^{-3} = 0.0033$

### Complementation Test
- Used to determine if two different mutations are in the same gene or in different genes.
- **Method**: Coinfect a host cell with two different mutant phage strains.
    - **Noncomplementation**: If mutations are in the **same gene**, no functional protein is produced, and no viral plaques form (the cell is unable to produce viral particles).
    - **Complementation**: If mutations are in **different genes**, the two genomes provide the missing functions for each other. Functional viral particles are produced, and viral plaques form on the bacterial lawn.

---

## 3. Restriction Mapping
A technique to determine the locations of restriction enzyme cleavage sites on a DNA molecule.

### Practice Problem (Source: Page 55)
- **DNA Fragment**: 7.5 kb (linear)
- **Digestion Results**:
    - *Hind*III: 3.0 kb, 4.5 kb (One site)
    - *Sma*I: 2.0 kb, 5.5 kb (One site)
    - *Hind*III + *Sma*I: 2.0 kb, 2.5 kb, 3.0 kb
- **Logic**:
    - *Sma*I cuts at 2.0 kb from one end (leaving 5.5 kb).
    - *Hind*III cuts at 3.0 kb from the **other** end (leaving 4.5 kb).
    - The middle fragment is $7.5 - 2.0 - 3.0 = 2.5$ kb.
- **Map**: `[End] --2.0kb-- (SmaI) --2.5kb-- (HindIII) --3.0kb-- [End]`

---
