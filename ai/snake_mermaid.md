# Mermaid Block-Beta: Snake Flow Principles

The "Snake Flow" pattern allows for a multi-row, continuous process path within a fixed-width grid, ideal for long procedural workflows.

## 1. Grid Configuration
- **Columns:** Define an odd number of columns (e.g., `columns 5`) to allow for a central node or balanced spacing.
- **Spacers:** Use `space:5` (matching the column count) between content rows to create vertical separation and prevent connection lines from overlapping text blocks.

## 2. Row Directionality (The "Snake" Logic)
To maintain a continuous flow, odd and even rows must be populated in reverse order relative to the connection sequence:
- **Row 1 (Left to Right):** `Node A`, `space`, `Node B`, `space`, `Node C` (Indices 1, 3, 5).
- **Row 3 (Right to Left):** `Node F`, `space`, `Node E`, `space`, `Node D` (Indices 1, 3, 5). 
  - *Logic:* Even though the code lists F, E, D, the connections `C --> D --> E --> F` create the visual "backwards" movement.
- **Row 5 (Left to Right):** `Node G`, `space`, `Node H`, `space`, `Node I` (Indices 1, 3, 5).

## 3. Positioning and Spacing
- **Vertical Spacing:** Use `space:n` (where n = total columns) to create empty rows.
- **Horizontal Offsets:** Use `space:n` (where n < total columns) to push a single node to the end of a row (e.g., `space:4` followed by `Node J` to place J in the 5th column).

## 4. Styling and Formatting
- **Internal Padding:** Use HTML divs inside node labels to control text layout:
  ```mermaid
  A["<div style='padding-bottom:15px;'>Top Text<br>Bottom Text</div>"]
  ```
- **Font Scaling:** Set global font size in the init block:
  ```mermaid
  %%{init: {'themeVariables': { 'fontSize': '22px'}}}%%
  ```

## 5. Connections
Define all logic at the bottom of the block. The snake effect is achieved by the sequence of definitions (C to D, F to G) which bridge the right-most and left-most columns of adjacent rows.

```mermaid
block-beta
  columns 5
  A --> B --> C
  space:5
  F <-- E <-- D
  C --> D
  space:5
  G --> H --> I
  F --> G
```
