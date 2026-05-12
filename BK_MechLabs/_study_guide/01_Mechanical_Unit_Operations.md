# Chapter 1: Mechanical Unit Operations (Grinding - Sieving - Mixing)

This chapter focuses on the physical manipulation of solids. You will learn how to reduce the size of materials, sort them by size, and blend them into a uniform mixture.

---

## 1. Hammermill Grinding
*How we break things down efficiently.*

### 🔍 What will you learn?
- How a **Hammermill** uses impact force to crush materials.
- Why the **Screw Feeder** is the "heartbeat" of the machine.
- How to measure if a machine is working at its peak efficiency.

### 💡 Core Concepts
- **Impact Grinding**: Unlike grinders that "squeeze" material, a hammermill hits it with high-speed rotors.
- **Bond’s Law**: The "Golden Rule" for predicting milling energy. It states that the work needed depends on the new cracks you create in the material.
  $$P = 19W_i \left(\frac{1}{\sqrt{D_{p2}}} - \frac{1}{\sqrt{D_{p1}}}\right) T$$
  > [!TIP]
  > **$D_{p}$ represents the "80% passing size"**. In engineering, we don't look at the biggest or smallest grain, but where 80% of the mass falls.

### 🛠️ Practical Laboratory Insight
> [!IMPORTANT]
> **How do you know when grinding is finished?**
> Watch the **Ammeter**. When you start, the current spikes (heavy load). As the material turns to powder and exits through the screen, the needle will drop back to its "No-Load" value. This tells you the chamber is empty.

### 🧪 Why was my efficiency low?
In the lab, you might find efficiency is around **19-20%**. This is normal!
- **Heat Loss**: Most energy turns into heat, not just breaking the material.
- **Material Loss**: Fine dust often escapes the collection bag or sticks to the screen.

---

## 2. Sieving Analysis
*Sorting by size using gravity and vibration.*

### 🔍 What will you learn?
- The proper "stacking" logic for sieves.
- How to calculate **Sieve Performance ($E$)**.

### 📐 The "Sieve Stack" Rule
Always assemble sieves from **Largest Aperture (Top)** to **Smallest Aperture (Bottom)**. 
- **Top**: Catches the "oversize".
- **Bottom**: The "Receiver" or "Pan" catches the finest dust.

### 💡 Key Formula: Sieve Efficiency ($E$)
$$E = \frac{J}{Fa} \times 100$$
- $J$: What actually passed through.
- $Fa$: What *should* have passed through theoretically.

> [!NOTE]
> **High Efficiency (>95%)** is common in the lab because we use dry materials. If the material was damp, particles would "blind" (clog) the mesh, and efficiency would crash.

---

## 3. Solid Mixing
*Achieving the perfect blend.*

### 🔍 What will you learn?
- How to tell if a mixture is truly "random" or still "segregated."
- Why sampling at different spots is critical.

### 💡 The Mixing Index ($I_s$)
Think of $I_s$ as a "Purity Score" for your mixture.
- **$I_s \approx 0$**: The beans are completely separated (Top vs. Bottom).
- **$I_s \to 1$**: The beans are perfectly mixed.

### 🛠️ The "Spatial Uniqueness" Rule
You cannot judge a mixture by looking at one spot. In the lab, we take **8 samples from 8 different positions**. This ensures we aren't just looking at a "lucky" spot where the beans happen to look mixed.

### ❓ Quick Check
**Q: Why does the Mixing Index fluctuate over time?**
*A: Because as the drum rotates, particles can "un-mix" (segregate) if their sizes are too different. The optimal mixing time is the point where $I_s$ hits its highest peak before dropping again.*

---

## Related Materials
- [[Mechanical_Lab_Study_Guide.md|Overview Guide]]
- [[GSM/3.GSM.tex|Source LaTeX Report]]
