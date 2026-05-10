# Chapter 10: Bacterial Genetics

## 1. Bacterial Chromosome Structure
Most bacterial species contain a **single, circular chromosome** made of DNA and associated proteins.

### Key Features
- **Size**: Typically a few million base pairs (Mbp) in length.
- **Copy Number**: Usually one per cell, but some species can have multiple copies.
- **Gene Organization**: Several thousand different genes are interspersed throughout the chromosome.
- **Intergenic Regions**: Short regions between adjacent genes.
- **Origin of Replication**: Most bacterial chromosomes have a **single origin of replication** required to initiate DNA synthesis.
- **Repetitive Sequences**: May be interspersed throughout the chromosome and play roles in folding, DNA replication, gene regulation, and genetic recombination.

---

## 2. DNA Supercoiling
Bacterial DNA must be highly compacted to fit inside the cell.
- **Loop Domains**: The DNA is organized into loops that are held in place by proteins.
- **Supercoiling**: Further twisting of the DNA molecule to compact it further.
    - **Negative Supercoiling**: DNA is underwound. This is the most common form in bacteria as it aids in DNA strand separation during replication and transcription.
    - **Positive Supercoiling**: DNA is overwound.

---

## 3. Horizontal Gene Transfer (HGT)
Bacteria can exchange genetic material through three primary mechanisms:

### Conjugation
- **Mechanism**: Requires direct cell-to-cell contact through a **conjugation bridge**.
- **F Factor (Fertility Factor)**: A plasmid that allows a donor cell (**F+**) to transfer DNA to a recipient (**F-**).
- **Process**:
    1.  Relaxosome makes a cut at the **origin of transfer**.
    2.  T-DNA (single-stranded) is pumped into the recipient by an exporter.
    3.  Both cells replicate the DNA to become double-stranded F+ cells.
- **Hfr Cells (High Frequency of Recombination)**:
    - Occurs when an F factor integrates into the host chromosome via crossover at **Insertion Sequences (IS)**.
    - During conjugation, Hfr cells transfer a portion of their chromosome to the recipient.

### Transformation
- **Mechanism**: Uptake of DNA fragments from the environment (often from dead donor cells).
- **Competence**: The ability of a cell to take up extracellular DNA.
- **Cotransformation**: Simultaneous transfer of two or more genes. Frequency is higher for genes that are closer together.

### Transduction
- **Mechanism**: Genetic transfer mediated by a **bacteriophage** (virus).
- **Generalized Transduction**: Phage P1 fragments host DNA and occasionally packages a piece of bacterial DNA into a viral head (**transducing particle**).
- **Recombination**: The transducing DNA is incorporated into the recipient's chromosome.

---

## 4. Bacterial Genetic Mapping
Mapping the relative positions of genes on the circular chromosome.

### Time of Entry Mapping (Conjugation)
- Based on the duration of mating. Genes closer to the origin of transfer enter the recipient earlier.
- **Example**: In *E. coli*, `lacZ` enters at ~16 min, `galE` at ~25 min.

### Cotransduction Mapping
- Uses the frequency at which two genes are transduced together to determine distance.
- **Formula**: `Cotransduction frequency = (1 - d/L)³`
    - `d`: distance in minutes.
    - `L`: max DNA size a phage can carry (~2 min for P1).
- **Example**: A frequency of 0.42 corresponds to a distance of 0.5 minutes.

---

## 5. Other Genetic Elements
- **Insertion Sequences (IS)**: Simple transposable elements encoding only the enzymes for transposition (e.g., IS50).
- **Transposons (Tn)**: Complex elements that may carry additional genes like antibiotic resistance.
    - **Example (Tn5)**: Carries genes for resistance to neomycin (`neo-r`), bleomycin (`ble-r`), and streptomycin (`str-r`).
- **Integrons**: DNA elements that capture and express gene **cassettes** (often carrying resistance genes) using site-specific recombination.

---

## 6. Restriction Mapping Practice (Source: Page 55)
### Problem
A 7.5 kb linear DNA fragment is digested with two restriction enzymes, *Hind*III and *Sma*I. The resulting fragments are analyzed via gel electrophoresis:
- **HindIII alone**: 3.0 kb, 4.5 kb
- **SmaI alone**: 2.0 kb, 5.5 kb
- **Double Digest (HindIII + SmaI)**: 2.0 kb, 2.5 kb, 3.0 kb

### Mapping Logic
1.  **HindIII** cuts once ($3.0 + 4.5 = 7.5$).
2.  **SmaI** cuts once ($2.0 + 5.5 = 7.5$).
3.  **Double Digest** yields 3 fragments ($2.0 + 2.5 + 3.0 = 7.5$).
4.  Since SmaI produces a 2.0 kb fragment and the double digest also has a 2.0 kb fragment, the SmaI site must be 2.0 kb from an end.
5.  Since HindIII produces a 3.0 kb fragment and the double digest also has a 3.0 kb fragment, the HindIII site must be 3.0 kb from the opposite end.
6.  The remaining middle fragment is $7.5 - 2.0 - 3.0 = 2.5$ kb.

**Map**: `[End] --- 2.0 (SmaI) --- 2.5 (HindIII) --- 3.0 --- [End]`
