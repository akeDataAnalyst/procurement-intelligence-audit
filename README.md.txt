procurement-intelligence-audit

# Strategic Procurement & Supplier Intelligence Scorecard (2024–2025)
---

## Project Description

This project is a high-fidelity Forensic Procurement Audit and Performance Dashboard designed for a technical supply chain environment.

It analyzes 300+ simulated procurement transactions (2024–2025) to evaluate supplier performance across:

- Internal house brands (Dayliff)
- International OEMs (Grundfos, Pedrollo)
- Local Ethiopian vendors  

The project transforms raw ERP-style procurement data into strategic, decision-ready insights for supply chain leaders.

---

## The Problem

Technical procurement in East Africa faces three critical “silent killers” of profitability:

### 1. Price Creep  
Suppliers gradually increase final invoice prices compared to original Purchase Orders (POs), reducing margin visibility.

### 2. Logistics Volatility  
Unpredictable international shipping lead times disrupt project timelines and risk critical path delays.

### 3. Brand Dilution  
Lack of data-driven comparison makes it difficult to justify the value of internal brands (e.g., Dayliff) over external suppliers.

---

## The Solution

This project implements a three-stage analytical pipeline:

### 1. Forensic Audit Engine
- Detects data anomalies (e.g., negative lead times)
- Calculates price variance (%) per transaction
- Flags suspicious supplier behavior

### 2. Weighted Scoring Model
A multi-factor supplier ranking system based on:

- Reliability (50%) ? On-time delivery performance  
- Cost Stability (30%) ? Price variance consistency  
- Volume Capacity (20%) ? Ability to fulfill large orders  

Outputs a Supplier Performance Score for ranking and segmentation.

### 3. Interactive Control Tower Dashboard
Built using Streamlit, featuring:

- 4-Quadrant Value vs Reliability Matrix
- Supplier tier classification (Strategic / Risky / Tactical / Low Value)
- Real-time filtering and drill-down analysis

---

## Strategic Recommendations

Based on 2024–2025 audit findings:

### Protect the Core
- Dayliff (Global) maintained 0% price variance
- Recommended as a primary hedge against inflation and volatility

### Audit External OEMs
- Some international suppliers showed >1.5% price creep
- Recommend activating Right-to-Audit clauses in future contracts

### Mitigate Local Risks
- Local vendors exhibit high short shipment rates
- Recommend implementing:
  - Pre-Delivery Inspection (PDI) protocols
  - Supplier quality scorecards

---

## Tech Stack

| Category          | Tools                         |
|-------------------|-------------------------------|
| Language          | Python 3.10+                  |
| Data Wrangling    | Pandas, NumPy                 |
| Visualization     | Plotly Express (Dark Theme)   |
| Web Framework     | Streamlit (Custom CSS)        |
| Environment       | Jupyter Notebook, VS Code     |

---
**Developed by:** Aklilu Abera