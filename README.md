# 🥬 SafePlate Kenya v2 — AI-Driven Pesticide Residue Mitigation Platform

> **Empirical Agrochemical Surveillance, SCS-CN Hydrological Modeling, Organic Alternatives Transition & 11 Kiswahili Interactive Boards**

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-2.0.0-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-jmsmuigai%2FPesticide--Residue--Mitigation-green.svg)](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)

---

## 📌 Executive Overview

**SafePlate Kenya v2** is a production-grade, AI-powered geospatial and toxicological platform designed to solve pesticide residue contamination in Kenya's horticultural supply chain. Grounded in landmark laboratory surveillance (UoN, KOAN, SGS Kenya) and hydro-geospatial science, SafePlate Kenya connects analytical lab data, precipitation runoff models, regulatory registers (PCPB), and consumer safety calculators into an integrated web portal and Python package.

### Key Highlights & Mined Research Data:
- **Residue Prevalence**: **77.8%** of fresh produce sampled in Nairobi (Githurai, Muthurwa, Kangemi) and Nakuru markets contained detectable residues; **33.0%** exceeded EU Maximum Residue Limits (MRLs).
- **Eight Active Compounds**: Chlorfenapyr, Chlorpyrifos, Acephate, Lambda-Cyhalothrin, Difenoconazole, Linuron, Carbendazim, and Imidacloprid/Tebuconazole.
- **PCPB Biopesticides & BioCOPPA Index**: PCPB has registered **109 biopesticides** and launched the **BioCOPPA Index pilot in April 2026**.
- **Organic Baseline**: Certified organic land stands at **171,298 ha / 62,626 certified farms** (~0.6% of ag land), with KOAN PGS at 1,634 farmers, while biological inputs account for **~2.0%** of total applied volume.
- **Honest Limits (Springer 2025)**: Organic practices at smallholder input rates without integrated nutrient management do not close the Central Kenya yield gap; spray drift contamination was detected in 14.2% of buffer plots.
- **12 Biopesticide Alternatives**: Registered field-trial evidence for Azadirachtin 0.03%, Bt kurstaki, ICIPE 20 (*Metarhizium*), *Beauveria bassiana*, and Tuta absoluta pheromone traps (threshold: 2–3 moths/trap/week).

---

## 🧮 Mathematical Proofs & Engine Parity

Python (`safeplate_platform`) and JavaScript (`index.html`) share identical formula implementations:

### 1. SCS-CN Hydrology & Runoff Model
Given Precipitation $P$ (mm) and Curve Number $CN$:
$$S = \frac{25400}{CN} - 254$$
$$I_a = 0.2 S$$
$$\text{If } P > I_a: \quad Q = \frac{(P - I_a)^2}{P - I_a + S}$$

- **Self-Test Verification**: For $P = 55.0\text{ mm}$ and $CN = 79.0$:
  $$S = 67.519\text{ mm}, \quad I_a = 13.504\text{ mm}$$
  $$Q = \mathbf{15.80\text{ mm}}$$
  *(Byte-identical output between Python `hydrology.py` self-test and browser console).*

### 2. Consumer Wash Efficacy Model
Calculates residual pesticide fraction after washing:
- Benchmark Chlorfenapyr + Cold Water 5-minute rinse returns **0.5734** (**57.3%** remaining, **42.7%** removed). Parity verified against FastAPI `/wash` endpoint.

---

## 🗺️ The 11 Kiswahili-Named Interactive Boards

1. **RAMANI (Living Map)**: Interactive Leaflet/OpenStreetMap radar with county pressure halos, market diamonds (Githurai, Muthurwa, Kangemi, Nakuru), transit supply routes, geolocate button, and click-anywhere nearest-node calculation.
2. **SHAMBA (Organic Switchboard)**: Season-plan generator mapping 12 biopesticide alternatives, PCPB data, and honest yield-gap limits.
3. **TAKWIMU (Statistical Integrity Board)**: NSO/spatial-statistics position carrying the 7-principle integrity charter, 6-silo join map, and JSON audit log export.
4. **SHINIKIZO (County Residue Pressure Index PRPI)**: Risk rank table and heatmaps for 47 counties.
5. **SUMU (Eight Chemical Actives Matrix)**: Toxicological explorer for WHO hazard classes, EU MRLs, half-lives, and water washability.
6. **OSHO (Hydrology Simulator)**: Live SCS-CN runoff calculator with $Q(P=55, CN=79) = 15.80\text{ mm}$ verification badge.
7. **OSHA (Washing Calculator)**: Consumer wash mitigation calculator returning exact remaining residue (e.g. 0.5734 / 57.3%).
8. **PAYUKA (AI Multilingual Extension Advisory Engine)**: Extension advice in Kiswahili, Kikuyu, Dholuo, and English.
9. **SOKO (Public Market Risk Radar)**: Lab surveillance breakdowns for Githurai, Muthurwa, Kangemi, and Nakuru.
10. **TUTA (Biopesticide Alternatives Register)**: Searchable 12-alternative IPM register with field-trial efficacy and costs.
11. **TAARIFA (County Briefs & Gemini Telemetry)**: News mining feed (PCPB BioCOPPA updates) and Gemini agent log.

---

## 🚀 Installation & Quick Start

### One-Step Automated Setup (`install.sh`)
```bash
git clone https://github.com/jmsmuigai/Pesticide-Residue-Mitigation.git
cd Pesticide-Residue-Mitigation
bash install.sh
```

### Automation via Makefile
```bash
make test             # Runs byte-identical self-tests
make serve            # Launches FastAPI REST server (http://localhost:8000/docs)
make dashboard        # Launches Streamlit control room (http://localhost:8501)
make web              # Launches local web server for index.html (http://localhost:8080)
make all              # Re-runs tests and image pipeline
```

---

## 🤖 Gemini AI Delegation Agent (`gemini_agent.py`)

The Gemini agent (`safeplate_platform/gemini_agent.py`) automates 7 core tasks:
1. **Photoreal Image Prompts & Asset Pipeline**: 22 visual assets.
2. **Multilingual Translation**: Kiswahili, Kikuyu, Dholuo, English.
3. **Grounded News Mining**: PCPB BioCOPPA pilot updates.
4. **47 County Advisory Briefs**.
5. **Independent QA Fact-Checker**: Applies `UNVERIFIED` tag to unconfirmed claims.
6. **Public Market Risk Diagnostics**.
7. **Execution Audit Manifest Logger**.

*Security Note*: API keys are safely configured via `.env` (`GOOGLE_API_KEY`) and excluded from version control via `.gitignore`.

---

## 🔗 Project Links

- **GitHub Repository**: [https://github.com/jmsmuigai/Pesticide-Residue-Mitigation](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)
- **Interactive Web Portal**: Open `index.html` locally or run `make web` to access `http://localhost:8080`.
- **FastAPI Documentation**: Run `make serve` to access `http://localhost:8000/docs`.

---

## 📜 License
MIT License. SafePlate Kenya Team 2026.
