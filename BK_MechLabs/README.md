# BK MechLabs – Lab Reports

**Faculty:** Chemical Engineering | **University:** HCMUT

This repository contains LaTeX lab reports for the Mechanical Processing course. Each report lives in its own subfolder and is fully self-contained.

---

## Reports

| Folder | Report | Status |
|---|---|---|
| [`Drying/`](Drying/) | Drying Convection | ✅ Complete |

---

## Repository Structure

```
BK_MechLabs/
├── .venv/                  # Shared Python virtual environment
├── .vscode/                # Shared VS Code / LaTeX Workshop settings (XeLaTeX)
├── README.md
└── Drying/                 # Drying Convection report
    ├── 2.DRYING.tex        # Main LaTeX entry point (compile with XeLaTeX)
    ├── hcmut.sty           # HCMUT style sheet
    ├── commands.tex        # Shared LaTeX macros
    ├── generate_plots.py   # Master script: regenerates all plots
    ├── Sections/           # Modular section files (0-Title … 8-References)
    ├── Scripts/            # Python plot generators
    │   ├── plot_curves.py            # Theoretical curves (Theory §2.8)
    │   ├── plot_exp_curves.py        # Exp. drying curves (Report §5.3.1)
    │   └── plot_exp_rate_curves.py   # Exp. rate curves (Report §5.3.2)
    └── Images/             # Generated PDF plots + logo
```

---

## Compilation

All reports use **XeLaTeX** (required for Unicode/Vietnamese support).

```bash
cd Drying/
xelatex 2.DRYING.tex
```

VS Code with LaTeX Workshop will compile automatically using the workspace `.vscode/settings.json`.

---

## Generating Plots

Activate the shared virtual environment from the repo root, then run from inside the report folder:

```bash
source .venv/bin/activate.fish
cd Drying/
python generate_plots.py
```

### Dependencies

```bash
uv pip install numpy matplotlib
```
