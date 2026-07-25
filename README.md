# 🥬 SafePlate Kenya v3 — Ministry of Health Advisory Solution & AI Agrotech Platform

> **Direct Technical Response & System Solution for Ministry of Health Advisory Ref: MOH/ADM/1/2/52 (22nd July 2026)**

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-3.0.0-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-jmsmuigai%2FPesticide--Residue--Mitigation-green.svg)](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)

---

## 🏛️ Executive Summary & MOH Advisory Solution (MOH/ADM/1/2/52)

On **22nd July 2026**, PS Mary Muthoni Muriuki (Ministry of Health, State Department for Public Health & Professional Standards) issued an official advisory (**Ref: MOH/ADM/1/2/52**) to all County Executive Committee Members (CECM-Health), County Directors of Health (CDH), and Chief Officers for Health (COH) regarding pesticide residues in fresh produce across public markets.

**SafePlate Kenya v3** serves as the primary technical solution and digital intelligence system addressing all directives in the advisory:

### Solutions to the 5 Mandatory County Actions:
1. **Market Surveillance**: RAMANI 2.0 real-time market risk radar mapping high-probability contamination nodes across Githurai, Muthurwa, Kangemi, and Nakuru wholesale markets.
2. **Public Communication & Household Preparation**: OSHA Household Wash Calculator and visual guides demonstrating **60–70% residue reduction** via thorough washing, soaking in 1:3 vinegar or 2% salt water, and peeling.
3. **Trader & Producer Coordination**: SHAMBA Organic Switchboard generating crop-specific 14-day Pre-Harvest Interval (PHI) compliance calendars and MRL compliance checklists.
4. **County Reporting Portal**: TAKWIMU Automated Digital Reporting Portal compiling county inspection capacity logs into standardized JSON audit reports for Ministry submission.
5. **Inter-Agency Referral Gateway**: One-click digital referral gateway dispatching lab violation flags directly to PCPB and KEPHIS inspectorships.

---

## 🎨 Visual Assets & Crop Gallery

SafePlate Kenya v3 incorporates real photorealistic image assets generated via Gemini API / Nano banana for ALL monitored horticultural commodities:
- 🍅 **Tomatoes (Nyanya)** (`crop_tomatoes.png`): MRL 0.01 ppm, PHI 14 days.
- 🥬 **Sukuma Wiki / Kale** (`crop_sukuma.png`): Multi-residue load up to 7 active compounds.
- 🍃 **Spinach** (`crop_spinach.png`): Acephate & Chlorpyrifos monitoring.
- 🧅 **Bulb Onions / Kitunguu** (`crop_onions.png`): Low-risk baseline crop.
- 🫑 **Capsicum / Pilipili Hoho** (`crop_capsicum.png`): Acephate pressure.
- 🥕 **Carrots** (`crop_carrots.png`): Linuron residue tracking.
- 🥬 **Cabbage** (`crop_cabbage.png`): Lambda-cyhalothrin.
- 🥔 **Potatoes / Viazi** (`crop_potatoes.png`): Copper & difenoconazole late-blight spray schedules.

---

## 🧮 Verified Math Engines

- **SCS-CN Hydrology Runoff**: $Q(P=55\text{ mm}, CN=79) = \mathbf{15.80\text{ mm}}$ (byte-identical in Python and JS).
- **Household Wash Mitigation**: Benchmark 1:3 vinegar soak yields **68.0% residue reduction** (0.3200 remaining fraction), satisfying the Ministry's 60–70% reduction target.

---

## 🚀 Quick Start & Installation

```bash
git clone https://github.com/jmsmuigai/Pesticide-Residue-Mitigation.git
cd Pesticide-Residue-Mitigation
bash install.sh
```

### Server & Command Shortcuts
```bash
python3 safeplate_platform/mine_and_clean.py # Run surveillance data mining
make test                                    # Run byte-identical self-tests
make web                                     # Launch local web portal (http://localhost:8080)
make serve                                   # Launch FastAPI backend (http://localhost:8000/docs)
```

---

## 🔗 Project Links

- **GitHub Repository**: [https://github.com/jmsmuigai/Pesticide-Residue-Mitigation](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation)
- **Live Local Web Portal**: [http://localhost:8080](http://localhost:8080)
- **FastAPI API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
