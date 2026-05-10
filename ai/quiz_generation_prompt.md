# Quiz Generation Prompt

```markdown
You are an expert educational content creator.
Create a comprehensive 40-question multiple-choice quiz based strictly on the provided material.

**Requirements:**
1. **Format:** Return strictly a valid JSON array of objects. No extra text, markdown, or explanations.
2. **Quantity:** Generate roughly 40 questions depending on the length of the material coverage.
3. **Difficulty Distribution:**
   - ~10 Easy Questions (Definitions, basic facts)
   - ~20 Medium Questions (Comparisons, functions, advantages/disadvantages)
   - ~10 Hard Questions (Specific details, complex application, reasoning/interdependencies)
4. **Constraints:**
   - **Naming:** Ensure the output filename or title is consistent with the `_study_guides` naming scheme (e.g., `Chapter_X_Title`).
   - **Avoidance:** Do NOT include questions about specific obscure historical dates, history facts, or highly specific/obscure species-related numbers (e.g., precise elemental percentages of a very specific strain unless it's a major generalizable concept). Focus on high-level understanding and process interdependencies.
   - **Limit "All of the above":** Use this option sparingly (max 3-4 times).
   - **"shuffleOptions" Tag:**
     - Default to `true`.
     - Set to `false` ONLY if the options contain relative references like "All of the above", "Both A and B", "None of the above", or specific sequences (e.g. chronological order).
   - **Coverage:** Ensure questions cover ALL sections of the text.

**JSON Schema:**
[
  {
    "question": "Question text string",
    "options": [
      "Option 1",
      "Option 2",
      "Option 3",
      "Option 4"
    ],
    "answer": "The correct option string (must match exactly one option)",
    "shuffleOptions": true
  }
]
```
