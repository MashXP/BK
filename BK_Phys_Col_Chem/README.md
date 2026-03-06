# Physical & Colloid Chemistry Cheat Sheet

This repository contains the LaTeX source code for a comprehensive cheat sheet and formula summary for Physical and Colloid Chemistry. It is designed to be a modular, two-column reference guide, primarily based on the curriculum at HCMUT (Bach Khoa University).

## Project Overview

The main document, `phys_col_chem_main.tex`, aggregates various chapters into a single, cohesive PDF. It covers topics ranging from basic thermodynamics and chemical equilibrium to electrochemical cells and colloid chemistry.

## Directory Structure

*   **`phys_col_chem_main.tex`**: The master LaTeX file that compiles the entire document.
*   **`Sections/`**: Contains individual `.tex` files for each chapter/topic. This modular approach allows for easy maintenance and updates.
    *   `0a-BasicConcepts.tex`: Basic Thermodynamics Concepts
    *   `1b-FirstLaw.tex`: First Law of Thermodynamics
    *   `1c-SecondLaw.tex`: Second & Third Laws
    *   `1d-ChemicalEquilibrium.tex`: Chemical Equilibrium
    *   `4-Electrochemistry.tex`: Electrochemistry & Kinetics
    *   `5a-ColloidIntroduction.tex`: Introduction to Colloids
    *   ...and many others.
*   **`Images/`**: Stores images and graphics used in the document (e.g., university logo).
*   **`hcmut.sty`**: A custom LaTeX style package for formatting the document according to specific requirements.
*   **`INSTRUCTION.md`**: Internal guidelines for contributors on how to process source PDFs and add new content.

## Requirements

To compile this project, you need a standard LaTeX distribution (such as TeX Live or MiKTeX) with the following packages installed:

*   `graphicx`
*   `amsmath`, `amssymb`, `amsfonts`
*   `geometry`
*   `tabularx`, `booktabs`, `array`
*   `siunitx`
*   `chemformula`
*   `enumitem`
*   `xcolor`
*   `float`

## Compilation

You can compile the document using `pdflatex`. Run the following command in the root directory:

```bash
pdflatex -interaction=nonstopmode phys_col_chem_main.tex
```

It is recommended to run the command twice to ensure the table of contents and references (if any) are correctly resolved.