# AI Session Instructions: Physical & Colloid Chemistry Project

## Project Context
The goal is to maintain and expand a modular, two-column LaTeX document (`phys_col_chem_main.tex`) that summarizes formulas and theory from Physical and Colloid Chemistry lecture slides.

## Current Progress
- **Main Document**: Converted to a two-column layout using `hcmut.sty`.
- **Modular Structure**: Content is split into files within the `Sections/` directory.
- **PDF Assets**: All lecture slides in `downloads/` have been processed and split into parts of max 25 pages each (e.g., `*_part1.pdf`).
- **Authentication**: `cookies.txt` contains valid cookies for `lms.hcmut.edu.vn` if further downloads are needed.

## Style & Formatting Rules
1. **Two-Column Safety**:
   - Avoid `longtable`. Use `tabular` with specific column widths (e.g., `p{0.4\linewidth}`).
   - Escape all `&` characters in text or section titles (e.g., `Constants \& Units`).
2. **Formula Integrity**:
   - Use standard LaTeX math environments (`equation`, `align`).
   - Output final results directly without intermediate arithmetic.
3. **Modularity**:
   - **Complementation**: If a PDF contains content belonging to an existing section (e.g., Thermodynamics or Equilibrium), append/update the existing `.tex` file in `Sections/`.
   - **New Topics**: Create new files (e.g., `Sections/5-Colloids.tex`) for distinct chapters.
4. **Verification**: After every significant edit, run:
   `pdflatex -interaction=nonstopmode phys_col_chem_main.tex`

## PDFs Processed So Far
- `Chapter 0_NTS.pdf` -> `0a-BasicConcepts.tex`
- `Ch 1_NTS.pdf` -> `1b-FirstLaw.tex`
- `Ch 2_NTS.pdf` -> `1c-SecondLaw.tex`
- `Ch 3_NTS_part1 & part2.pdf` -> `1d-ChemicalEquilibrium.tex`
- `Ch 4_NTS_part1 & part2.pdf` -> `1e-PhaseEquilibrium.tex`
- `Ch 5_NTS_v2_part1 & part2.pdf` -> `1f-SolutionEquilibrium.tex`
- `Ch 6_NTS_v2.pdf` -> `2-LiquidSolid.tex`
- `Colloid chemistry - Chapter 1.pdf` -> `5a-ColloidIntroduction.tex`, `8-ElectricalColloids.tex`
- `Colloid chemistry - Chapter 2.pdf` -> `5-SurfaceAdsorption.tex`, `6-Curvature.tex`
- `Colloid chemistry - Chapter 3.pdf` -> `6-Curvature.tex`
- `Colloid chemistry - Chapter 4.pdf` -> `5-SurfaceAdsorption.tex`
- `Colloid chemistry - Chapter 5.pdf` -> `5-SurfaceAdsorption.tex`
- `Colloid chemistry - Chapter 6.pdf` -> `5b-LiquidAdsorptionIonExchange.tex`
- `Colloid chemistry - Chapter 7.pdf` -> `7-KineticColloids.tex`
- `Colloid chemistry - Chapter 8.pdf` -> `8-ElectricalColloids.tex`
- `Colloid chemistry - Chapter 9.pdf` -> `8-ElectricalColloids.tex`
- `Physical Chemistry 2_Electrochemical Cells and Electrodes.pdf` -> `4-Electrochemistry.tex`
- `Physical Chemistry 2_Kinetics of electrochemical processes.pdf` -> `4-Electrochemistry.tex`
- `Physical Chemistry 2_Surface phenomena and Adsorption.pdf` -> `5-SurfaceAdsorption.tex`, `5b-LiquidAdsorptionIonExchange.tex`
- `Polymer.pdf` -> `9-EmulsionsPolymers.tex`
- `hydrophilic-lipophilic_balance_m.pdf` -> `9-EmulsionsPolymers.tex`

## Next Steps for AI
1. **Sequential Processing**: Continue reading the remaining split PDFs in `downloads/` one by one (starting with `Colloid chemistry - Chapter 1_part1.pdf`).
2. **Deduplication**: Check `Sections/` for existing formulas before adding new ones to prevent redundancy.
3. **Colloid Integration**: Transition into the Colloid chemistry chapters, creating new modular files as the topics shift from pure Thermodynamics/Equilibrium.
4. **Main File Updates**: Ensure every new section file is added via `\input{...}` in `phys_col_chem_main.tex`.
