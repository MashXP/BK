# Chapter 6: Processes - Sterilization - Recovery - Purification of fermentation products

## Overview
This chapter covers the essential processes required for successful industrial fermentation, divided into three main parts:
1. **Sterilization**
2. **Recovery of fermentation products**
3. **Purification of fermentation products**

---

## PART 1. STERILIZATION

### Introduction
The presence of foreign microorganisms in a fermentation process can lead to severe negative consequences:
1. **Loss of productivity**: Contaminants compete for nutrients.
2. **Outgrowth**: In continuous fermentations, contaminants may displace the production organism.
3. **Product contamination**: The final product may be impure.
4. **Extraction difficulties**: Contaminants can produce compounds that interfere with downstream processing.
5. **Product degradation**: Contaminants may break down the desired product.
6. **Phage contamination**: In bacterial fermentations, phages can cause culture lysis.

Overall, contamination impacts economic benefits, health, and the environment.

### Avoidance of Contamination
To achieve effective contamination control, the following measures are necessary:
- Effective design and construction of the fermentation plant.
- Use of a pure inoculum.
- Sterilization of the medium.
- Sterilization of the fermenter vessel.
- Sterilization of all materials added during fermentation.
- Maintenance of aseptic conditions throughout the process.
- Implementation of detailed Standard Operating Procedures (SOPs), sterilization protocols, aseptic maintenance, and staff training.

### Definition and Agent Selection
**Sterilization** is defined as the process to eliminate biological contamination (bacteria, yeast, fungi, bacteriophage) in the fermentation process.

Criteria for selecting sterilization methods/agents:
- Minimal impact on the quantity and quality of medium components.
- No production of inhibitory compounds.
- Safety for human health and the environment.
- Simplicity, ease of scaling up, and cost-effectiveness.

### Nutrient Quality Loss During Sterilization
Two main types of reactions contribute to the loss of nutrient quality during heat sterilization:
1. **Interactions between nutrients**: A common occurrence is the **Maillard-type browning reaction**, which causes discoloration, loss of nutrient quality, and accumulation of growth-inhibitory compounds.
2. **Degradation of heat-labile components**: Vitamins, amino acids, and proteins can be degraded during steam sterilization.

**Table: The Effect of Sterilization Time on Glucose Remaining (at 121°C)**
| Time at 121°C (min) | Amount of Added Glucose Remaining (%) |
| :--- | :--- |
| 30 | 64% |
| 40 | 46% |
| 60 | 35% |
*(Source: Corbett, 1985)*

### Rules to Prevent Contamination ("3" NOs)
1. **NO remaining**: Ensure equipment and medium are completely free of contaminated microbial cells before starting.
2. **NO entering**: Prevent external contamination from entering the system during operation.
3. **NO spreading**: Prevent contamination from spreading in the workspace if it occurs.

### Sources of Contamination
- **Equipment**: Inappropriate design, leakage, or malfunctioning sensors.
- **Operation**: Input flows (medium, aeration), sampling procedures, or carryover from previous fermentations.

### Types of Sterilization
Sterilization can be categorized based on the target:
1. **Media Sterilization**: 
   - Components sterilized together.
   - Components sterilized separately (for heat-labile ingredients).
2. **Equipment Sterilization**: Fermenters, pipes, and sensors.
3. **Product Sterilization**: Ensuring final products are free of contaminants.

---

### Sterilization Methods
Methods are broadly classified into **Physical**, **Filtration**, and **Chemical** methods.

#### 1. Physical Methods: Heat
Heat is the most popular sterilization method, suitable for media, equipment, and products.

**Kinetics of Cell Death**
The destruction of microorganisms by heat follows first-order kinetics:
$$-\frac{dN}{dt} = k \cdot N$$
Integrating this gives:
$$Ln\left(\frac{N_t}{N_o}\right) = -kt \implies N_t = N_o e^{-kt}$$
Where:
- $N$: Number of viable organisms ( $N_o$ at start, $N_t$ at time $t$).
- $t$: Time of sterilization (minutes).
- $k$: Specific death rate ($min^{-1}$), which depends on the species and its physiological state.

**Dry Heat Sterilization**
Performed in drying ovens for glassware and metal equipment.
| Temperature | Time |
| :--- | :--- |
| $150^\circ\text{C}$ | 2 hours 30 min |
| $160^\circ\text{C}$ | 2 hours |
| $170^\circ\text{C}$ | 1 hour |
- **Advantages**: Simple to handle, fast.
- **Disadvantages**: High energy consumption, not suitable for liquids.

**Moist Heat (Steam) Sterilization**
Uses pressurized steam. The standard regime is **$121^\circ\text{C}$ at 15-20 minutes**.
- **Lab Scale**: Uses an autoclave.
- **Large Scale**: Sterilization occurs within the fermenter by heating the jacket or internal coils with steam. **Agitation** is critical for uniform heat distribution.

**Sterilization of Liquid Wastes**
Industrial processes must sterilize waste biomass before disposal. A typical continuous flow system includes:
`Sump Tank` $\to$ `Inactivation Tank` $\to$ `Heat Exchanger (Preheating)` $\to$ `Steam Injector` $\to$ `Holding Coil` $\to$ `Cooling` $\to$ `Neutralization (pH 7.0)`.

#### 2. Physical Methods: Radiation
- **Ultraviolet (UV)**: Wavelengths between $10^{-7}$ and $10^{-5}$ cm.
- **Ionizing Radiation**: X-rays and Gamma rays.

#### 3. Filtration Methods
Filtration is used for both liquids and gases. Microorganisms are removed via four primary mechanisms:
1. **Inertial Impaction**: Particles hit the filter fibers because they cannot follow the fluid's rapid changes in direction.
2. **Diffusion**: Extremely small particles (Brownian motion) collide with filter molecules and get trapped.
3. **Electrostatic Attraction**: Opposite charges between particles and the filter medium.
4. **Interception**: Physical blocking of particles larger than (and sometimes smaller than) the filter pores.

**Filter Types and Performance**
- **Surface Filter**: Pores are smaller than the particles. Particles deposit on the surface, forming a "cake."
- **Depth Filter**: Pores are larger than the particles; removal relies on mechanisms like inertial impaction and diffusion.
- **Classification by Retention Size**:
  | Type | Retention Range ($\mu m$) | Targeted Contaminants |
  | :--- | :--- | :--- |
  | Microfiltration (MF) | $0.10$ to $1.0$ | Bacteria |
  | Ultrafiltration (UF) | $0.01$ to $0.10$ | Viruses, Macromolecules, Colloids |
  | Nanofiltration (NF) | $0.001$ to $0.01$ | Proteins, Sugars, Dyes |
  | Reverse Osmosis (RO) | $0.0001$ to $0.001$ | Ions, Salts, Heavy Metals |

**Filter Sterilization Targets**
- **Liquids**: Bulk medium, nutrient feeds, water, pH control agents (acids/alkalis/buffers), and antifoams.
- **Inlet Air**: Crucial for aerobic processes. Uses **hydrophobic** membranes to repel water; must remove bacteria, fungi, and bacteriophages.
- **Exhaust Air**: Necessary for safety and containment, specially mandatory for recombinant organisms to prevent environmental release.

#### 4. Chemical Methods
Used for rapid surface or laboratory sterilization (e.g., using **formaldehyde**). They are fast but have limited applications due to potential toxicity or residue.

---

## PART 2. RECOVERY OF FERMENTATION PRODUCTS
**Downstream Processing (DSP)** refers to the recovery and purification of biosynthetic products from the fermentation broth.

### Introduction to Recovery
The primary goals of microbial fermentation are to obtain **microbial cells** or **metabolites** (intracellular or extracellular).

- **Costs**: Recovery can account for **15% to 70%** of total manufacturing costs.
- **Broth Complexity**: Fermentation broth contains the product at low concentrations (typically $0.1\text{--}5\ g/dm^3$), along with microorganisms, cell debris, medium components, and other metabolic by-products.

### Downstream Processing Flowchart
The path depends on whether the product is intracellular or extracellular:
1. **Fermenter** $\to$ **Solid-Liquid Separation**.
2. **Path A (Extracellular)**: Supernatant $\to$ Recovery $\to$ Purification $\to$ Crystallization and Drying.
3. **Path B (Intracellular)**: Cells $\to$ Cell disruption/rupture $\to$ Cell debris removal $\to$ Recovery $\to$ Purification $\to$ Crystallization and Drying.

### Choice of Recovery Process
Selection criteria include:
1.  **Target Product**: Cells or metabolites.
2.  **Location**: Intracellular or extracellular.
3.  **Concentration**: Amount of product in the broth.
4.  **Properties**: Physical and chemical properties of the desired product.
5.  **Intended Use**: Medical, food, or industrial application.
6.  **Purity**: Minimum acceptable standards.
7.  **Biohazard**: Safety requirements of the product or broth.
8.  **Impurities**: Nature of the impurities in the fermenter broth.
9.  **Economics**: Marketable price vs. recovery costs.

### Methods to Ease Recovery and Purification
- **Microorganism Selection**: Choose strains that do not produce pigments or undesirable metabolites.
- **Fermentation Modification**: Alter conditions to reduce unwanted by-products.
- **Harvest Timing**: Precise timing of harvesting ensures maximum product stability.
- **Post-Harvest Treatment**: Control pH and temperature immediately after harvesting.
- **Pre-treatment**: Addition of flocculating agents or enzymes to attack cell walls.

### Supporting Techniques
#### 1. Sedimentation
Particles in suspension settle out based on gravity.
- **Factors**: Cell concentration, salts/sugars, particle size, broth viscosity, pH, and temperature.

#### 2. Flocculation
Process where particles clump together as attractive forces overcome repulsive surface charges.
- **Objective**: Increase clarification efficiency by increasing average particle size.
- **Agents**:
    - **Inorganic Salts**: Positively charged ions like $Al^{3+}$ or $Fe^{3+}$ (e.g., $FeCl_3$).
    - **Soluble Polymers**: Cationic polyelectrolytes (e.g., **Chitosan**) that bridge negatively charged particles.

### Recovery Methods
#### 1. Filtration
- **Dead-end Filtration**: Flow is perpendicular to the membrane. Leads to rapid cake buildup and blockage, lowering productivity.
- **Cross-flow/Tangential Flow Filtration (TFF)**: Flow is parallel to the membrane.
    - **Benefits**: $>99.9\%$ cell retention, closed system (no aerosols), and density-independent separation.
    - **Membranes**: Microporous (pore size, e.g., $0.22\ \mu m$) or Ultrafiltration (based on Molecular Weight Cut-Off, **MWCO**).

#### 2. Centrifugation
Often more expensive than filtration but used when filtration is difficult or high hygiene standards are required.
- **Rotor Types**:
    - **Fixed-Angle ($20\text{--}30^\circ$)**: High separation efficiency; pellet forms along the wall and can be harder to recover.
    - **Swinging-Bucket ($90^\circ$)**: Predictable pellet location at the bottom; lower overall efficiency.

### Cell Disruption (For Intracellular Products)
Microorganisms possess tough cell walls that must be ruptured to release metabolites.
#### 1. Cell Wall Structural Differences
- **Gram Positive Bacteria**: Thick peptidoglycan layer.
- **Gram Negative Bacteria**: Outer membrane, periplasmic space, and a thin peptidoglycan layer.
- **Yeast and Fungi**: Thick polysaccharide walls ($100\text{--}200\ nm$). Layers include an outer wall (Mannan, proteins) and an inner wall ($\beta$-glucans and **Chitin**).
- **Bursting Forces**: $A. niger$ ($\sim 250\text{--}550\ \mu N$) requires much higher force than $E. coli$ ($1\text{--}9\ \mu N$).

#### 2. Disruption Methods
| Method Class | Specific Techniques | Key Features |
| :--- | :--- | :--- |
| **Physico-mechanical** | **Bead Milling** | Simple; uses $0.1\text{--}3\ mm$ beads; can break DNA samples. |
| | **High Pressure Homogenizer** | High efficiency/purity; large scale ($3000\ L/h$); expensive. Works by **liquid shear**. |
| | **Ultrasonication** | $15\text{--}40\ kHz$; uses **cavitation** and shock waves; small scale ($5\text{--}500\ mL$). |
| **Chemical** | **Detergents** | **SDS** (anionic) disorganizes membranes; **Triton X-100** (nonionic) solubilizes proteins. |
| **Biological** | **Enzymatic** | Gentle; **Glycosidases** (bacteria), **Glucanases/Chitinase** (yeast/fungi), **Cellulases** (algae). |
| | **Phages** | Uses viral lysis cycles for cell rupture. |

### Purification of Products
Following recovery, products are purified using techniques prioritized by the required purity level:
1. **Chromatography**
2. **Distillation**
3. **Membrane Processes** (Ultrafiltration, Reverse Osmosis)
4. **Drying** (Final stage)

#### 1. Chromatography
Used to isolate and purify low concentrations of metabolic products by separating solutes based on charge, polarity, size, or affinity.
- **Gel Permeation (Gel Filtration)**:
    - **Mechanism**: Separates molecules based on size. Smaller molecules diffuse into the gel matrix; larger molecules are excluded and **elute first**.
    - **Matrices**: Crosslinked dextrans (**Sephadex**, Sephacryl) or crosslinked agarose (Sepharose).
    - **Application**: Vaccine purification; can achieve 10-fold concentration.
- **Ion-Exchange Chromatography**:
    - **Mechanism**: Reversible exchange of ions between a solid resin phase and a liquid phase.
    - **Resins**: Contain active groups like sulfonic acid, carboxylic acid, or phosphonic acid.
    - **Elution**: Sequentially washed off using buffers of increasing **pH** or **ionic strength**.
- **Other types**: Adsorption, Affinity, Reverse Phase, and HPLC (High Performance Liquid Chromatography).

#### 3. Membrane Processes
Utilize semipermeable membranes to separate molecules based on size.
- **Ultrafiltration (UF)**:
    - **Mechanism**: High molecular weight solutes are retained while solvent and low MW solutes are forced through fine pores ($1\text{--}100\ nm$) via hydraulic pressure ($2\text{--}10\ atm$).
    - **Cut-offs**: $500\text{--}500,000\ Daltons$.
    - **Purpose**: Separation of macromolecules (proteins, enzymes, hormones, viruses).
- **Reverse Osmosis (Hyperfiltration)**:
    - **Mechanism**: Applied pressure forces solvent against the concentration gradient through a semi-permeable membrane.
    - **Application**: Removal of "small" molecules (salts) that cannot be separated by ultrafiltration.
    - **Example**: Production of non-alcoholic wine (Concentration $\to$ Distillation to remove alcohol $\to$ Re-addition of water).

#### 4. Drying
The final removal of water or solvents from a product to ensure stability while minimizing loss of viability, activity, or nutritional value.
- **Benefits**: Reduced transport costs, easier handling/packaging, and convenient dry-state storage.
- **Spray Dryer**:
    - **Usage**: Most common for biological materials starting as liquids or pastes.
    - **Atomization**: Material is turned into small droplets ($10\text{--}500\ \mu m$).
    - **Temperature**: High inlet temp ($150\text{--}250\ ^\circ C$) but low residence time ($\sim 0.01\ s$) and cooler exhaust ($75\text{--}100\ ^\circ C$) protects products.
    - **Economics**: Most economical method for handling large volumes.
    - **Equipment**: Includes atomizing nozzles, a drying chamber, and a **cyclone separator** for product discharge.
