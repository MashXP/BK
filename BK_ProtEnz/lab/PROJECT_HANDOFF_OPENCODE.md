# Project Handoff & State Summary for OpenCode

**Workspace:** `/home/mashxp/Documents/MyVault/Atlas/BK/BK_ProtEnz`  
**Google Slides ID:** `1uuwojgbwZe2N0U5kFeph9hKU5B1c_TQhi0bgSpUhsUE`  
**Google Slides URL:** https://docs.google.com/presentation/d/1uuwojgbwZe2N0U5kFeph9hKU5B1c_TQhi0bgSpUhsUE/edit  
**External Tools Path:** `/home/mashxp/Documents/mcp-tools/google_slides_toolkit`  

---

## 1. Project Overview & Deliverables
This workspace contains coursework notes and a Group G3 course project presentation for **Fundamentals in Protein & Enzyme Engineering**.

* **Topic:** Protease-Accelerated Fish Sauce Production (Mechanistic Engineering).
* **Core Deliverable:** A 16-to-21 slide scientific and industrial presentation deck combining industrial application economics with rigorous active-site biochemistry (EC 3.4.21 catalytic triad, transition-state chemistry, halotolerance biophysics, and Ney's Q-rule debittering).

---

## 2. Vault Files Inventory

| File | Description | Status |
| :--- | :--- | :--- |
| `00_MOC_Prot_and_Enzyme.md` | Map of Content tracking modules and presentation tracker. | Complete |
| `01_Central_Dogma_and_Amino_Acids.md` | Central dogma, 20 amino acids, ionization, chirality, peptide properties. | Complete |
| `02_Protein_Structure_and_Folding.md` | Folding driving forces, peptide resonance, alpha-helices, beta-sheets, keratin hierarchy. | Complete |
| `03_Enzyme_Catalysis_and_Kinetics.md` | EC classes, Eyring rate theory, transition state stabilization, 4-step M-M derivation. | Complete |
| `_presentation/Slide_Deck_Plan_Fish_Sauce_Protease.md` | Complete 16-slide markdown plan with kickers, headlines, body, KPIs, and citations. | Complete |
| `_presentation/Necessary _citation_.txt` | Literature notes: Ney's Q-rule, 20–25% NaCl, <5% enzyme cost, endo/exo synergy. | Source data |
| `_presentation/protease.txt` | Literature citations (Lê et al., 2015; Okubo et al., 2022; Zhao et al., 2026; Valdivia et al., 2025). | Source data |

---

## 3. Live Google Slides Deck Structure (`21 Slides`)

### Agenda Blueprint (Slide 2)
The presentation is structured into 5 core narrative pillars:
1. `01. The Problem`: Traditional 12–18 month solar autolytic collapse and insoluble actomyosin/collagen matrix.
2. `02. How Enzymes Work`: Catalytic mechanism of Subtilisin (EC 3.4.21) and transition-state oxyanion hole stabilization.
3. `03. Taste & Salt Challenges`: Hydrophobic bitterness (Ney's Q), 20–25% NaCl halotolerance via acidic surface envelopes, and calcium loop autolysis resistance.
4. `04. Factory Process`: Two-stage decoupling (rapid enzymatic lysis -> salted microbial aging) and histamine safety (<200 ppm).
5. `05. Economics & Summary`: Enzyme cost ceiling (<5% batch OPEX), multi-criteria selection matrix, and roadmap.

### Slide-by-Slide Layout & Mapping

```
Slide 1:  Cover Slide (Hero Title)
Slide 2:  Master Agenda (Split Hero: Editorial List + KPI Cards)
──────────────────────────────────────────────────────────────────
SECTION 01: THE PROBLEM
  Slide 3: Industrial Context & The Autolytic Bottleneck (12–18 mo cycle)
  Slide 4: Substrate Architecture: Insoluble Protein Matrix (Actomyosin/Stroma)
──────────────────────────────────────────────────────────────────
Slide 5:  Divider Slide for Section 02 (Kicker: AGENDA | Headline: Overview)
SECTION 02: HOW ENZYMES WORK
  Slide 6: Biocatalytic Machinery: EC 3.4.21 Ser-His-Asp Triad (Process Flow)
  Slide 7: Transition-State Chemistry & Activation Energy (Split Hero)
──────────────────────────────────────────────────────────────────
Slide 8:  Divider Slide for Section 03 (Kicker: AGENDA | Headline: Overview)
SECTION 03: TASTE & SALT CHALLENGES
  Slide 9:  Active-Site Specificity & Bitterness (Process Flow)
  Slide 10: Sensory Biochemistry: Ney's Q-Rule Debittering (Split Hero)
  Slide 11: Enzymatic Synergy: Endo/Exo Ratio for AN/TN > 50% (Process Flow)
  Slide 12: Biophysical Stability: 20–25% NaCl Acidic Surface Hydration (Split Hero)
  Slide 13: Quantitative Hydrolysis Kinetics: Valdivia Log Model (Split Hero)
  Slide 14: Structural Engineering: Calcium Coordination Loops (Split Hero)
──────────────────────────────────────────────────────────────────
Slide 15: Divider Slide for Section 04 (Kicker: AGENDA | Headline: Overview)
SECTION 04: FACTORY PROCESS
  Slide 16: Two-Stage Fermentation Paradigm: Decoupling Lysis & Aging (Process Flow)
  Slide 17: Food Safety & Histamine Decarboxylase Control (<200 ppm Codex) (Split Hero)
──────────────────────────────────────────────────────────────────
[PENDING DIVIDER]: Section 05 Divider needed before Slide 18
SECTION 05: ECONOMICS & SUMMARY
  Slide 18: Industrial Scale-Up & Enzyme Cost Boundary (<5% OPEX) (Process Flow)
  Slide 19: Executive Blueprint & Selection Matrix (Styled Table Slide)
  Slide 20: Literature References (APA 7th Edition)
  Slide 21: Thank You / Q&A Slide
```

---

## 4. Current Work Done & State of Deck

1. **Agenda Restructuring**:
   * Slide 2 agenda items were simplified from overly academic terminology to direct, punchy anchors.
2. **Divider Repositioning**:
   * Previously, an extra divider was placed at Slide 11, awkwardly bisecting Section 03 between Debittering and Synergy.
   * That divider was moved to **Slide 15** (object ID `h6e97400d6ef0e45b_0_12`), positioning it immediately before Section 04 (*Process Bioengineering*).
3. **Divider Text Reset**:
   * Divider kickers are restored to **`AGENDA`** and headlines to **`Overview`**.
   * The unwanted `(Active)` text tags were completely purged from all shapes.

---

## 5. Immediate Problem: Bolding the Active Section on Dividers

### Root Cause
The `google-slides` MCP tool `slides_update_shape_text(presentation_id, shape_id, new_text)` executes:
```python
requests = [
    {"deleteText": {"objectId": shape_id, "textRange": {"type": "ALL"}}},
    {"insertText": {"objectId": shape_id, "text": new_text}},
]
```
It sends unformatted plain text. It does not parse markdown `**bold**` or send Google Slides API `updateTextStyle` requests.

### The Fix for OpenCode
In `/home/mashxp/Documents/mcp-tools/google_slides_toolkit/google_slides/engine.py`, replace `update_shape_text` with regex `**` parsing:

```python
def update_shape_text(self, presentation_id: str, shape_id: str, new_text: str):
    """Updates text of a specific shape in-place with markdown **bold** support."""
    import re
    bold_ranges = []
    clean_text_parts = []
    last_idx = 0
    current_len = 0

    for m in re.finditer(r"\*\*(.*?)\*\*", new_text, re.DOTALL):
        before = new_text[last_idx:m.start()]
        clean_text_parts.append(before)
        current_len += len(before)
        bold_text = m.group(1)
        bold_ranges.append((current_len, current_len + len(bold_text)))
        clean_text_parts.append(bold_text)
        current_len += len(bold_text)
        last_idx = m.end()

    clean_text_parts.append(new_text[last_idx:])
    clean_text = "".join(clean_text_parts)

    requests = [
        {"deleteText": {"objectId": shape_id, "textRange": {"type": "ALL"}}},
        {"insertText": {"objectId": shape_id, "text": clean_text}},
    ]
    for start, end in bold_ranges:
        requests.append({
            "updateTextStyle": {
                "objectId": shape_id,
                "textRange": {"startIndex": start, "endIndex": end, "type": "FIXED_RANGE"},
                "style": {"bold": True},
                "fields": "bold",
            }
        })
    self.slides.presentations().batchUpdate(presentationId=presentation_id, body={"requests": requests}).execute()
```

### Shape IDs on Dividers:
* **Slide 5 (Divider 02):** Shape `h6e97400d6ef0e45b_0_3` -> bold line `**02. How Enzymes Work**`
* **Slide 8 (Divider 03):** Shape `h6e97400d6ef0e45b_0_9` -> bold line `**03. Taste & Salt Challenges**`
* **Slide 15 (Divider 04):** Shape `h6e97400d6ef0e45b_0_15` -> bold line `**04. Factory Process**`
* **Add Section 05 Divider** before Slide 18 -> bold line `**05. Economics & Summary**`
