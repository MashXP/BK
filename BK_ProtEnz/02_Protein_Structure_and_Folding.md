# 02 — Protein Structure & Folding

**Module:** 02  
**Parent:** [[00_MOC_Prot_and_Enzyme|Index / MOC]] | **Previous:** [[01_Central_Dogma_and_Amino_Acids|01 — Central Dogma, Amino Acids & Peptides]] | **Next:** [[03_Enzyme_Catalysis_and_Kinetics|03 — Enzyme Catalysis & Kinetics]]  
**Topics:** Thermodynamic Principles, Driving Forces, Peptide Bond Planarity, $\alpha$-Helix, $\beta$-Sheets, $\beta$-Turns, Tertiary & Quaternary Structure, Fibrous vs Globular ($\alpha$-Keratin)

---

## 1. Protein 3D Structure & Native State Folding

### 1.1 Thermodynamic Principles
* **Structure-Function Axiom:** 3D structure dictates specific biological function.
* **Native Fold:** The thermodynamically most stable, lowest free energy ($\Delta G < 0$) functional conformation.
* **Conformational Entropy Penalty:** Folding drastically decreases chain disorder ($\Delta S_{\text{chain}} \ll 0$). This conformational entropy cost must be overcome by favorable enthalpy ($\Delta H < 0$) and solvent entropy gain ($\Delta S_{\text{solvent}} \gg 0$).

### 1.2 Driving Forces for Folding & Stabilization

| Driving Force | Mechanism | Impact / Characteristics |
| :--- | :--- | :--- |
| **Hydrophobic Effect** | Nonpolar core burial | Water release $\to \uparrow \Delta S_{\text{solvent}}$; primary folding driver |
| **Electrostatic / Salts** | Salt bridges & dipole contacts | Strong stabilization when buried in low-dielectric core |
| **Van der Waals & H-Bonds** | Close atomic packing & $\text{N}-\text{H}\cdots\text{O}=\text{C}$ | Drives secondary structures ($\alpha$-helix, $\beta$-sheet) & core rigidity |

1. **Hydrophobic Effect (Primary Driving Force):**
   * Nonpolar side chains aggregate in the protein interior.
   * Collapsing hydrophobic residues releases structured, ordered clathrate water molecules into bulk solvent.
   * Yields a net positive entropy change in surrounding water ($\Delta S_{\text{water}} > 0$).
2. **Hydrogen Bonds:**
   * Backbone $\text{N}-\text{H}\cdots\text{O}=\text{C}$ interactions drive and stabilize secondary structures ($\alpha$-helices, $\beta$-sheets).
3. **Van der Waals (Dispersion) Interactions:**
   * Weak, short-range interactions between densely packed internal atoms; collectively provide massive stabilization to the folded core.
4. **Electrostatic Interactions & Salt Bridges:**
   * Long-range interactions between opposite charges ($\text{Arg}^+ / \text{Lys}^+$ and $\text{Asp}^- / \text{Glu}^-$).
   * **Buried Salt Bridges:** Significantly stabilize folded states when shielded from high dielectric solvent in hydrophobic cores.

---

## 2. Peptide Bond & Secondary Structures

### 2.1 Peptide Bond Characteristics
* **Resonance & Planarity:**
  * Significant resonance delocalization ($\sim 40\%$ double bond character between $\text{C}-\text{N}$).
  * Rotation around the peptide $\text{C}-\text{N}$ bond is strictly restricted.
  * Six atoms lie in a single rigid plane: $\text{C}_{\alpha1}-\text{C}(=\text{O})-\text{N}(\text{H})-\text{C}_{\alpha2}$.
* **Reactivity:** Significantly less reactive and more resistant to hydrolysis than aliphatic esters.
* **Conformation:** Almost exclusively in the ***trans*** conformation ($> 99.6\%$) to minimize steric clashes between consecutive $\text{R}$-groups (exception: Proline, where *cis* occurs at $\sim 6\%$).
* **Dipole Moment:** Uneven charge separation ($\text{O}^{\delta-}, \text{N}^{\delta+}$) imparts a large permanent dipole moment ($\approx 3.7\text{ Debye}$) along the peptide unit.

### 2.2 $\alpha$-Helix Architecture & Metrics

* **Helical Chirality:** Exclusively **right-handed** in standard proteins composed of L-amino acids.
* **Hydrogen Bonding Scheme:**
  * Regular intrachain H-bond between the carbonyl oxygen of residue $i$ and the amide proton of residue $i+4$:
    $$\text{C}=\text{O}_i \cdots \text{H}-\text{N}_{i+4}$$
  * All peptide dipoles align parallel to helix axis, generating an overall helix dipole (partial positive charge at $\text{N}$-terminus, partial negative charge at $\text{C}$-terminus).

```
        N-term (δ+) ──> [ C=O_i ······ H-N_(i+4) ] ──> C-term (δ-)
```

* **Spatial Dimensions & Geometry:**
  * **Residues per turn:** $3.6\text{ residues/turn}$.
  * **Pitch (rise per complete turn):** $5.4\text{ \AA}$ ($0.54\text{ nm}$).
  * **Rise per residue:** $1.5\text{ \AA}$ ($0.15\text{ nm}$).
  * **Core Packing:** Interior is tightly packed with backbone atoms; inner lumen is too small to accommodate water molecules or side chains.
  * **Side Chain Orientation:** $\text{R}$-groups project outward and slightly toward the $\text{N}$-terminus, preventing steric clash with the helical backbone.
  * **Helical Diameters:**
    * Backbone-only diameter: $4\text{--}5\text{ \AA}$.
    * Total outer diameter (including extended side chains): $10\text{--}12\text{ \AA}$.
* **Functional Feature (DNA Major Groove Binding):**
  * The outer diameter of an $\alpha$-helix ($10\text{--}12\text{ \AA}$) matches the width and depth of the major groove of B-form DNA ($\sim 12\text{ \AA}$).
  * Outward-pointing amino acid side chains directly contact nucleotide base pairs in sequence-specific DNA-binding proteins (e.g., transcription factors, zinc fingers, helix-turn-helix motifs).

### 2.3 $\alpha$-Helix Formation Propensity & Helix Dipole

* **Helix Formers vs. Breakers:**
  * **Strong Formers:** Alanine (Ala) and Leucine (Leu) — small, unbranched side chains with optimal helical propensity.
  * **Helix Breakers:**
    * **Proline (Pro):** Rigid pyrrolidine ring locks $\phi$ dihedral angle (~$-60^\circ$), lacks backbone amide $-\text{NH}$ for H-bonding, introducing a structural kink/bend.
    * **Glycine (Gly):** High conformational entropy/flexibility makes locking into rigid helical backbone energetically unfavorable.
* **Residue Spacing & Amphipathic Helices:**
  * Side chains 3–4 residues apart ($i$ and $i+3$ or $i+4$) align on the same helical face:
    * *Electrostatic stabilization/destabilization:* Oppositely charged residues (e.g., $\text{Glu}^- \cdots \text{Lys}^+$) stabilize; like charges repel and destabilize.
    * *Aromatic stacking:* Phe/Tyr/Trp stacking stabilizes.
  * Positioning hydrophobic residues every 3–4 residues generates an **amphipathic $\alpha$-helix** (polar face towards solvent, apolar face buried in core or membrane interfaces).
* **Macroscopic Helix Dipole:**
  * Parallel alignment of individual peptide dipole moments ($\text{N}^{\delta+}-\text{H} \cdots \text{O}^{\delta-}=\text{C}$) sums across the helix:
    * **$\text{N}$-terminus:** Partial positive charge ($\delta+$).
    * **$\text{C}$-terminus:** Partial negative charge ($\delta-$).
  * **Helix Capping:** Negatively charged residues ($\text{Asp}^-, \text{Glu}^-$) favored near $\text{N}$-terminus; positively charged residues ($\text{Lys}^+, \text{Arg}^+$) favored near $\text{C}$-terminus to neutralize terminal dipoles.

```
       (+) NH3-term [δ+] ──> [ C=O_i ······ H-N_(i+4) ] ──> [δ-] COO-term (-)
              ↑                                                     ↑
     Favors Asp-, Glu-                                     Favors Lys+, Arg+
```

---

### 2.4 $\beta$-Sheet Architecture & Variants

* **Backbone Conformation:** Fully extended zig-zag / pleated polypeptide chains ($\phi \approx -120^\circ \text{ to } -140^\circ, \psi \approx +120^\circ \text{ to } +140^\circ$).
* **Hydrogen Bonding:** Formed by inter-strand $\text{C}=\text{O} \cdots \text{H}-\text{N}$ hydrogen bonds between adjacent $\beta$-strands.
* **Side Chain Orientation:** $\text{R}$-groups alternate pointing strictly above and below the sheet plane across successive residues.

| Parameter | Antiparallel $\beta$-Sheet | Parallel $\beta$-Sheet |
| :--- | :--- | :--- |
| **Strand Direction** | Opposite ($\text{N} \to \text{C}$ adjacent to $\text{C} \to \text{N}$) | Same ($\text{N} \to \text{C}$ adjacent to $\text{N} \to \text{C}$) |
| **H-Bond Geometry** | **Linear / Perpendicular** ($\approx 180^\circ$, collinear) | **Bent / Angled** (distorted) |
| **Relative Stability** | **Higher stability** (optimized electrostatic overlap) | **Lower stability** |
| **Repeat Period** | $7.0\text{ \AA}$ (2 residues) | $6.5\text{ \AA}$ (2 residues) |

---

### 2.5 $\beta$-Turns & Proline Cis/Trans Isomerism

* **Function & Geometry:** Reverses chain direction by $180^\circ$ across **4 amino acid residues**; connects antiparallel $\beta$-strands and secondary motifs.
* **Stabilization:** Intramolecular H-bond between carbonyl oxygen of residue $i$ and amide proton of residue $i+3$ ($\text{C}=\text{O}_i \cdots \text{H}-\text{N}_{i+3}$).
* **Conserved Positions:**
  * **Position 2:** Frequently **Proline** (readily accommodates required tight cis/trans turn geometry).
  * **Position 3:** Frequently **Glycine** (small $-\text{H}$ side chain avoids steric clash in tight loop).
* **Proline Peptide Bond Isomerism:**
  * Standard peptide bonds: $> 99.6\%$ *trans* configuration.
  * $\text{X}-\text{Pro}$ peptide bonds: $\approx 6\%$ exist in ***cis*** configuration (steric clashes in *cis* vs *trans* are comparable with pyrrolidine ring).
  * *cis*-Proline bonds predominate in type II/VI $\beta$-turns.
  * **Peptidyl Prolyl Cis-Trans Isomerases (PPIases):** Enzymes catalyzing interconversion between *trans* and *cis* forms during protein folding (rate-limiting step).

---

## 3. Tertiary Structure & Protein Classification

### 3.1 Definition & Stabilization Forces
* **Definition:** Complete three-dimensional spatial conformation of a single polypeptide chain.
* **Spatial Proximity:** Amino acid residues distant in linear primary sequence are brought into intimate contact via folding.
* **Stabilizing Interactions:**
  1. **Hydrophobic interactions:** Core burial of apolar side chains.
  2. **Electrostatic interactions / Salt bridges:** Buried or surface ion pairing.
  3. **Hydrogen bonds:** Side-chain to side-chain & side-chain to backbone contacts.
  4. **Van der Waals contacts:** Dense spatial packing.
  5. **Covalent Disulfide Bonds ($-\text{S}-\text{S}-$):** Formed between adjacent Cysteine thiol groups; provides major structural rigidity in extracellular/secreted proteins.

### 3.2 Structural Classes: Fibrous vs. Globular

| Feature | Fibrous Proteins | Globular Proteins |
| :--- | :--- | :--- |
| **Shape** | Long, elongated, filamentous, rod-like | Compact, spherical, folded |
| **Solubility** | Insoluble in water (high nonpolar surface) | Soluble in aqueous solutions |
| **Structure** | Single dominant secondary structural element | Complex mixture of $\alpha$-helices, $\beta$-sheets, and loops |
| **Primary Role** | Structural integrity, mechanics, protection | Catalytic (enzymes), regulatory, transport, defense |
| **Examples** | $\alpha$-Keratin, Collagen, Silk Fibroin | Hemoglobin, Myoglobin, Proteases, Lysozyme |

### 3.3 Fibrous Protein Architecture: $\alpha$-Keratin Hierarchy

```
[ α-Helix Monomer ]
       │
       ▼ (2 parallel helices wrap left-handed)
[ Two-Chain Coiled Coil ]
       │
       ▼ (Staggered antiparallel pairs)
[ Protofilament (20–30 Å) ]
       │
       ▼ (Assembly of multiple protofilaments)
[ Protofibril ] ──> [ Intermediate Filament / Hair Macrofibril ]
```

* **Step 1 — $\alpha$-Helix:** Right-handed $\alpha$-helix with hydrophobic heptad repeat ($a\text{--}g$, hydrophobic at $a$ and $d$).
* **Step 2 — Two-Chain Coiled Coil:** Two parallel right-handed $\alpha$-helices intertwine in a **left-handed supercoil** via hydrophobic strip interlocking.
* **Step 3 — Protofilament:** Paired coiled-coils associate in a staggered, antiparallel fashion ($D = 20\text{--}30\text{ \AA}$).
* **Step 4 — Protofibril:** Higher-order lateral assembly of protofilaments.
* **Stabilization:** Extensively reinforced and cross-linked by covalent **disulfide bonds** ($-\text{S}-\text{S}-$), conferring high tensile strength, insolubility, and hardness.

---

## 4. Quaternary Structure
* **Definition:** Spatial arrangement and non-covalent (or disulfide-linked) association of two or more discrete polypeptide chains (subunits or protomers) into a functional multi-subunit oligomeric protein complex.
* **Subunit Configurations:**
  * *Homo-oligomers:* Composed of identical subunits (e.g., homodimers, homotetramers).
  * *Hetero-oligomers:* Composed of distinct polypeptide subunits (e.g., Hemoglobin $\alpha_2\beta_2$ heterotetramer).
* **Functional Advantages:**
  * **Allosteric regulation & Cooperativity:** Conformational changes in one subunit modulate substrate affinity in neighboring subunits.
  * **Genetic economy & Efficiency:** Smaller coding sequences minimize transcription/translation errors compared to single massive polypeptides.
  * **Metabolic channeling:** Direct substrate transfer between adjacent active sites in multi-enzyme complexes.
