# 🥬 SafePlate Kenya v5 — Pesticide Mitigation, Garissa Corridors & Organic Agrotech Platform

> **AI-Driven Pesticide Surveillance, SCS-CN Hydrology, Garissa Supply Vectors & Household Wash Guides**

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-5.0.0-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-jmsmuigai%2FPesticide--Residue--Mitigation-green.svg)](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)

---

## 📌 Executive Overview & Platform Features

**SafePlate Kenya v5** is a comprehensive, production-grade agrotech and food safety system designed for farmers, market traders, extension officers, and households across Kenya.

### Key Version 5 Highlights:
1. **Automated Hero Image Slideshow**: Automated animated carousel on the homepage rotating through all 15 photorealistic generated crop images and farm visuals (`crop_tomatoes.png`, `crop_sukuma.png`, `crop_spinach.png`, `crop_onions.png`, `crop_capsicum.png`, `crop_carrots.png`, `crop_cabbage.png`, `crop_potatoes.png`, `hero_banner.png`, `lab_testing.png`, `githurai_market.png`, `biopesticide_spray.png`, `organic_harvest.png`, `anatomy_diagram.png`, `infographic_wash_3d.png`).
2. **RAMANI Map 2.0 with Garissa & Supply Corridors**:
   - Clipped Kenya map boundaries.
   - **Garissa Wholesale Market** added alongside Nairobi (Githurai, Muthurwa, Kangemi), Nakuru, Mombasa, Kisumu, Eldoret, Nyeri, and Meru.
   - Supply movement vector polylines showing produce travel from Central Kenya (Kirinyaga, Kiambu, Nyandarua) $\rightarrow$ Nairobi wholesale hubs $\rightarrow$ Garissa Market!
   - Interactive click handler populating a detailed **Attribute Panel** with real crop images, dominant pests & plant diseases, pesticide risk levels, and action guides.
3. **Live Ticker Marquee Bar**: Header bar featuring real-time pesticide residue updates.
4. **Farmer's Step-by-Step Organic Guide**: Practical transition procedures for smallholders using PCPB 109 biopesticides (Neemol, Bt kurstaki, ICIPE 20 *Metarhizium*), pheromone traps, and KOAN PGS certification.
5. **Kitchen Wash & Cook Guide**: Color-coded household preparation guide removing **60–70% of pesticide residues** via 1:3 vinegar, 2% salt water, or 1% baking soda soak.
6. **Simple Step-by-Step Food Safety Guide**: Clear, easy-to-understand explanations for community members and families.
7. **Pesticide-to-Cell Anatomy Diagram**: Scientific labeled diagram illustrating the 5-stage pathway of synthetic pesticides into human cells and mitochondrial stress.

---

## 🚀 Quick Start & Installation

```bash
git clone https://github.com/jmsmuigai/Pesticide-Residue-Mitigation.git
cd Pesticide-Residue-Mitigation
bash install.sh
```

### Automation & Server Commands
```bash
python3 safeplate_platform/analytics.py     # Run 2020-2026 trend analytics & Red Zones
python3 generate_diagrams.py                # Re-synthesize anatomy diagrams & infographics
make web                                     # Launch local web portal (http://localhost:8080)
make serve                                   # Launch FastAPI REST backend (http://localhost:8000/docs)
```

---

## 🔗 Project Links

- **GitHub Repository**: [https://github.com/jmsmuigai/Pesticide-Residue-Mitigation](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)
- **Live Local Web Portal**: [http://localhost:8080](http://localhost:8080)
- **FastAPI API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
