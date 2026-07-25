# 🥬 SafePlate Kenya v4 — Cell Anatomy, 3D Infographics, MOH Solution & Agrotech Portal

> **Official Response to Ministry of Health Advisory Ref: MOH/ADM/1/2/52 (PS Mary Muthoni Muriuki, 22nd July 2026)**

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-4.0.0-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-jmsmuigai%2FPesticide--Residue--Mitigation-green.svg)](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)

---

## 🏛️ Executive Summary & MOH Advisory Solution (MOH/ADM/1/2/52)

**SafePlate Kenya v4** is a comprehensive AI-driven geospatial and toxicological platform addressing the **Ministry of Health Advisory (Ref: MOH/ADM/1/2/52)** regarding pesticide residues in fresh produce across public markets.

### Key v4 Features:
1. **Pesticide-to-Cell Anatomy Diagram (`anatomy_diagram.png`)**: Labeled scientific diagram illustrating the 5-stage pathway of synthetic pesticides from crop spray $\rightarrow$ produce residue $\rightarrow$ gut ingestion $\rightarrow$ bloodstream transit $\rightarrow$ cell mitochondrial toxicity.
2. **Simple 10-Year-Old Explanation Guides**: Step-by-step kid-friendly procedures in English and Kiswahili explaining how salt/vinegar washing removes 60-70% of residues and how organic farming protects families.
3. **Python Trend Analytics Engine (`safeplate_platform/analytics.py`)**: Analyzes 2020–2026 time series trends and classifies Red Zones (Githurai, Muthurwa, Mwea Kirinyaga, Kangemi).
4. **Photorealistic Crop Gallery**: Real image assets for all 8 monitored commodities: Tomatoes, Sukuma Wiki/Kale, Spinach, Bulb Onions, Capsicum, Carrots, Cabbage, and Potatoes.
5. **Multi-Themed Web Portal**: Distinct visual themes for different sections (Agrotech Emerald, Cellular Purple, Household Mint, Crimson Warning, Azure Ocean, Golden Harvest).

---

## 🚀 Quick Start & Installation

```bash
git clone https://github.com/jmsmuigai/Pesticide-Residue-Mitigation.git
cd Pesticide-Residue-Mitigation
bash install.sh
```

### Server & Command Shortcuts
```bash
python3 safeplate_platform/analytics.py     # Compute 2020-2026 trend series & Red Zones
python3 generate_diagrams.py                # Re-synthesize anatomy diagrams & 3D infographics
make web                                     # Launch local web portal (http://localhost:8080)
make serve                                   # Launch FastAPI backend (http://localhost:8000/docs)
```

---

## 🔗 Project Links

- **GitHub Repository**: [https://github.com/jmsmuigai/Pesticide-Residue-Mitigation](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)
- **Live Local Web Portal**: [http://localhost:8080](http://localhost:8080)
- **FastAPI API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
