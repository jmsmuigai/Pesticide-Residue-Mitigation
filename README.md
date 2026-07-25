# 🥬 SafePlate Kenya v6 — Research Library, Assistant Bot & Agrotech Portal

> **Integrated Agrotech Platform featuring MAKTABA 46-Reference Library, MSAIDIZI Bot, MAWAKALA Agents, and Garissa Supply Corridors**

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-6.0.0-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-jmsmuigai%2FPesticide--Residue--Mitigation-green.svg)](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)

---

## 📌 Executive Overview & Platform Features

**SafePlate Kenya v6** is a comprehensive, production-grade agrotech research and food safety platform.

### Key Version 6 Highlights:
1. **MAKTABA Research Library (46 References)**:
   - 26 peer-reviewed studies, 11 reviews, 3 regulatory instruments, 4 reports, 2 datasets.
   - Filterable by 34 topic tags and study types, with copy-citation, CSV, and BibTeX export capabilities.
   - Featured studies: Springer *Environmental Monitoring & Assessment* (French bean/tomato/kale), Monte Carlo bifenthrin 35.7%, Kanario et al. 2025 (Nyandarua potatoes), Tharaka Nithi bio-insecticide field trial, and PCPB withdrawal decrees.
2. **MSAIDIZI Consumer & Farmer Assistant Bot**:
   - Local, deterministic tool execution engine chaining 8 tools (`get_active_profile`, `get_county_risk`, `get_alternatives`, `calc_wash`, `calc_hydrology`, `search_literature`, `get_market_risk`, `generate_advisory`).
   - Runs offline with zero API key dependencies, showing full source attribution.
   - CLI tool entry point: `python3 -m safeplate_platform.assistant` or `safeplate-assistant`.
3. **MAWAKALA Agent Operations Suite**:
   - 8 active in-page execution agents with an auditable 28-line run log.
   - Core enforcement finding: **Chlorpyrifos and Acephate were already withdrawn in Kenya yet detected in market produce** (enforcement gap, not rule gap).
4. **Structured Research Abstract & Live Cross-Validation**:
   - 6-paragraph academic paper abstract with keywords.
   - Live cross-validation card computing $Q(P=55, CN=79) = \mathbf{15.80\text{ mm}}$ and wash remaining $\mathbf{0.5734}$ ($57.3\%$) with a **✓ agreement badge**.
5. **RAMANI Map 2.0 & Garissa Corridors**:
   - Clipped Kenya map with supply movement vector polylines from Central Kenya to Garissa Wholesale Market.

---

## 🚀 Quick Start & Installation

```bash
git clone https://github.com/jmsmuigai/Pesticide-Residue-Mitigation.git
cd Pesticide-Residue-Mitigation
bash install.sh
```

### Automation & Server Commands
```bash
python3 -m safeplate_platform.assistant      # Run MSAIDIZI assistant CLI tool chain
python3 safeplate_platform/agents.py         # Run MAWAKALA agent sweep & generate run log
make web                                      # Launch local web portal (http://localhost:8080)
make serve                                    # Launch FastAPI REST backend (http://localhost:8000/docs)
```

---

## 🔗 Project Links

- **GitHub Repository**: [https://github.com/jmsmuigai/Pesticide-Residue-Mitigation](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)
- **Live Local Web Portal**: [http://localhost:8080](http://localhost:8080)
- **FastAPI API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
