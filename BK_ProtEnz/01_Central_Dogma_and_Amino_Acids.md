# 01 — Central Dogma, Amino Acids & Peptides

**Module:** 01  
**Parent:** [[00_MOC_Prot_and_Enzyme|Index / MOC]] | **Next:** [[02_Protein_Structure_and_Folding|02 — Protein Structure & Folding]]  
**Topics:** Central Dogma, Amino Acid Properties, Classification, Ionization, Peptides & Conjugated Proteins

---

## 1. Central Dogma & Gene Expression

### 1.1 Classical vs. Modern View
* **Classical View (Linear):**
  $$\text{DNA} \xrightarrow{\text{Transcription}} \text{mRNA} \xrightarrow{\text{Translation}} \text{Protein}$$
* **Modern Detailed View (Dynamic Network):**
  $$\begin{aligned}
  &\text{DNA} \underset{\text{Reverse Transcr.}}{\overset{\text{Replication}}{\rightleftharpoons}} \text{RNA} \xrightarrow{\text{Translation}} \text{Polypeptide} \xrightarrow{\text{Folding / PTM}} \text{Functional Protein} \to \text{Phenotypic Traits}
  \end{aligned}$$
  * Includes reverse transcription (retroviruses), RNA-dependent RNA replication (RNA viruses), non-coding RNAs (regulatory RNAs), and extensive post-translational modifications.

### 1.2 Stages of Transcription
1. **Initiation:** Double helix unwound by helicase/polymerase complex; promoter recognition; transcription bubble formation.
2. **Elongation:** RNA Polymerase reads template strand in $3' \to 5'$ direction and synthesizes nascent mRNA in $5' \to 3'$ direction.
3. **Termination:** Termination sequences/signals reached; dissociation of RNA polymerase and transcript release.

---

## 2. Amino Acids ($\alpha$-Amino Acids)

Proteins are **linear heteropolymers** composed of L-$\alpha$-amino acids linked via peptide bonds.

### 2.1 General Structure
All amino acids (except proline) contain a central chiral $\alpha$-carbon ($\text{C}_\alpha$):

$$\text{H}_2\text{N}-\text{C}_\alpha(\text{H})(\text{R})-\text{COOH} \quad \xrightleftharpoons{\text{pH 7.4}} \quad \text{H}_3\text{N}^+-\text{C}_\alpha(\text{H})(\text{R})-\text{COO}^- \quad \text{(Zwitterion)}$$

* **Key Roles:**
  * Polymerization building blocks (condensation forming peptide backbone).
  * Acid-base buffering behavior.
  * Structural and physicochemical diversity via distinctive side chains ($\text{R}$).

### 2.2 Nomenclature & Stereochemistry
* **Carbon Numbering:**
  * Organic/IUPAC: $\text{C}_1 = -\text{COOH}$, $\text{C}_2 = \text{C}_\alpha$, $\text{C}_3 = \text{C}_\beta$, etc.
  * Greek lettering system starts from $\text{C}_\alpha$: $\alpha, \beta, \gamma, \delta, \varepsilon, \zeta, \eta$.
* **Chirality & Fischer Convention:**
  * All standard amino acids are chiral except **Glycine** ($\text{R} = -\text{H}$).
  * Position of $-\text{NH}_3^+$ on Fischer projection (with $-\text{COOH}$ at top):
    * **L-isomer:** $-\text{NH}_3^+$ on the **Left** (predominant in biological proteins).
    * **D-isomer:** $-\text{NH}_3^+$ on the **Right** (found in bacterial cell walls, peptide antibiotics).

### 2.3 Classification by Side Chain ($\text{R}$-group) Properties

| Group | Count | Residues | Key Characteristics |
| :--- | :---: | :--- | :--- |
| **Nonpolar, Aliphatic** | 7 | Gly (G), Ala (A), Pro (P), Val (V), Leu (L), Ile (I), Met (M) | Hydrophobic core drivers; Proline has rigid cyclic pyrrolidine ring; Met has thioether. |
| **Aromatic** | 3 | Phe (F), Tyr (Y), Trp (W) | Hydrophobic; conjugated $\pi$ rings absorb UV light ($\lambda_{\max} \approx 280\text{ nm}$, predominantly $\text{Trp} > \text{Tyr}$). |
| **Polar, Uncharged** | 5 | Ser (S), Thr (T), Cys (C), Asn (N), Gln (Q) | Hydrophilic, form H-bonds; Cys forms covalent disulfide bonds ($-\text{S}-\text{S}-$). |
| **Positively Charged (Basic)** | 3 | Lys (K), Arg (R), His (H) | Net positive charge at physiological pH (~7.4); His ($\text{p}K_a \approx 6.0$) acts as general acid/base catalyst. |
| **Negatively Charged (Acidic)** | 2 | Asp (D), Glu (E) | Second carboxyl group ($-\text{COO}^-$); net negative charge at physiological pH. |

### 2.4 Ionization State & Isoelectric Point ($\text{pI}$)
Amino acids are amphoteric diprotic/triprotic electrolytes:

$$\underset{\text{Cation (Net +1)}}{\text{H}_3\text{N}^+-\text{CH}(\text{R})-\text{COOH}} \xrightarrow[\text{p}K_1]{\text{pH } \uparrow} \underset{\text{Zwitterion (Net 0)}}{\text{H}_3\text{N}^+-\text{CH}(\text{R})-\text{COO}^-} \xrightarrow[\text{p}K_2]{\text{pH } \uparrow} \underset{\text{Anion (Net -1)}}{\text{H}_2\text{N}-\text{CH}(\text{R})-\text{COO}^-}$$

* **Isoelectric Point ($\text{pI}$):** $\text{pH}$ where net molecular charge equals zero.
  $$\text{pI} = \frac{\text{p}K_1 + \text{p}K_2}{2}$$
  *(For residues with ionizable side chains, $\text{pI}$ is the average of the two $\text{p}K_a$ values flanking the neutral species).*

---

## 3. Peptides & Protein Architecture

### 3.1 Peptides
* **Size Boundary:** Molecular weight $< 10\text{ kDa}$ (typically $< 50$ amino acids).
* **Directionality:** Numbered and read strictly from **$\text{N}$-terminus $\to$ $\text{C}$-terminus** ($\text{H}_2\text{N}\text{--} \dots \text{--COOH}$).
* **Biological Roles:**
  * **Hormones / Pheromones:** Insulin ($5.8\text{ kDa}$), Oxytocin ($9$ aa), Glucagon.
  * **Neuropeptides:** Substance P (pain transmission mediator).
  * **Antibiotics:** Polymyxin B (disrupts Gram-negative membranes), Gramicidin.
  * **Toxins / Defense:** $\alpha$-Amanitin (RNA pol II inhibitor), Conotoxins (ion channel blockers).

### 3.2 Conjugated Proteins & Modifications
* **Polypeptide:** $> 10\text{ kDa}$ continuous amino acid chain.
* **Non-protein components:**
  * **Cofactors:** Inorganic ions ($\text{Mg}^{2+}, \text{Fe}^{2+}, \text{Zn}^{2+}, \text{Mn}^{2+}$) or complex chemical components.
  * **Coenzymes:** Complex organic or metallo-organic cofactors that function as transient carriers of functional groups (often derived from dietary vitamins).
  * **Prosthetic Groups:** Tightly or covalently bound cofactors/coenzymes essential for catalytic activity (e.g., Heme in myoglobin/hemoglobin).
  * **Post-Translational Modifications (PTMs):** Phosphorylation ($-\text{PO}_4^{2-}$), glycosylation, acetylation, methylation, lipidation.

### 3.3 Hydrogen Bonding Thermodynamics & Geometry
* **Interaction:** $\text{D}-\text{H}\cdots\text{A}$ (Donor $\text{D} = \text{O, N}$; Acceptor $\text{A} = \text{O, N}$).
* **Bond Strengths:**
  * Neutral–Neutral ($\text{N}-\text{H}\cdots\text{O}=\text{C}$): $4\text{--}6\text{ kJ/mol}$.
  * Charged Partner (Charge-assisted / salt-bridge linked): $6\text{--}10\text{ kJ/mol}$.
  * Max energy achieved when electrostatic alignment is optimized.
* **Geometry:** Highly directional; maximum strength occurs at **linear** alignment ($\angle \text{D}-\text{H}\cdots\text{A} \approx 180^\circ$).
