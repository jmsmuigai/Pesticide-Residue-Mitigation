# 📖 SafePlate Kenya v2 — User Help & Step-by-Step Guide

Welcome to the **SafePlate Kenya v2 User Guide**. This document provides detailed instructions on how to use the platform, execute local servers, interact with all 11 Kiswahili-named boards, and run automated self-tests.

---

## 🛠️ Step 1: Environment Setup & Installation

### Option A: One-Step Automated Script
Run the installer script in your terminal:
```bash
bash install.sh
```
This script will:
1. Create a Python virtual environment (`.venv`).
2. Upgrade `pip` and install all required dependencies in editable mode (`pip install -e .`).
3. Execute self-tests for `hydrology.py`, `washing.py`, and `gemini_agent.py`.

### Option B: Manual Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt # or pip install -e .
```

---

## 🔑 Step 2: Configuring Gemini AI Agent (.env)

To enable live Gemini AI queries, prompt generation, and news mining:
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your Google Gemini API key:
   ```env
   GOOGLE_API_KEY=your_actual_gemini_api_key_here
   ```
3. If no key is set, the Gemini agent (`safeplate_platform/gemini_agent.py`) automatically runs in **Mock Manifest Mode**, printing task structures without making network calls.

---

## 🚀 Step 3: Running Servers & Dashboards

Use the provided `Makefile` shortcuts:

| Command | Action | URL |
| :--- | :--- | :--- |
| `make web` | Starts local web server for `index.html` | [http://localhost:8080](http://localhost:8080) |
| `make serve` | Launches FastAPI backend server | [http://localhost:8000/docs](http://localhost:8000/docs) |
| `make dashboard` | Launches Streamlit Control Room | [http://localhost:8501](http://localhost:8501) |
| `make test` | Executes byte-identical self-tests | Terminal output |

---

## 🗺️ Step 4: Navigating the 11 Kiswahili Boards

| Board Name | Description | Key Features |
| :--- | :--- | :--- |
| **1. RAMANI** | Living Leaflet Map | Click anywhere to find nearest county node, toggle hotspots, geolocate. |
| **2. SHAMBA** | Organic Switchboard | Build custom IPM crop season plans; view PCPB biopesticide data & yield gap limits. |
| **3. TAKWIMU** | Integrity Board | Review 7-principle charter; view 6-silo join map; export `safeplate_audit_trail.json`. |
| **4. SHINIKIZO** | PRPI County Index | Filter 47 county risk ranks, PRPI scores, and dominant chemicals. |
| **5. SUMU** | Eight Actives Matrix | Inspect WHO toxicity classes, EU MRL thresholds, half-lives, and wash reach. |
| **6. OSHO** | Hydrology Simulator | Adjust precipitation $P$ and Curve Number $CN$ to calculate runoff $Q$. Verified $Q(55, 79) = 15.80\text{ mm}$. |
| **7. OSHA** | Wash Calculator | Calculate residual yield after cold water, salt, vinegar, or baking soda rinses. Benchmark: $0.5734$ ($57.3\%$). |
| **8. PAYUKA** | Extension Advisory | Switch between Kiswahili, Kikuyu, Dholuo, and English advisories. |
| **9. SOKO** | Market Risk Radar | View wholesale market surveillance charts (Githurai, Muthurwa, Kangemi, Nakuru). |
| **10. TUTA** | IPM Alternatives | Browse 12 registered biopesticide alternatives with field-trial efficacy data. |
| **11. TAARIFA** | News & Agent Log | Grounded news updates on PCPB BioCOPPA pilot and Gemini agent telemetry. |

---

## ❓ Frequently Asked Questions (FAQ)

### Q1: How do I verify that Python and JavaScript formulas match?
- Run `python3 safeplate_platform/hydrology.py`. You will see `Q_mm = 15.7954` (formatted as `15.80 mm`).
- Open `index.html` in your browser and check Board 6 (**OSHO**). At $P=55$ and $CN=79$, the runoff display outputs `15.80 mm` with a green verification badge.

### Q2: Is my Gemini API key safe from git leak?
Yes. `.env` is explicitly listed in `.gitignore`. Only `.env.example` is tracked in version control.

### Q3: How do I export the audit trail?
Go to Board 3 (**TAKWIMU**) on the web portal and click the **Export Audit JSON** button.

---

## 📞 Support & Repository
For questions or issues, visit [https://github.com/jmsmuigai/Pesticide-Residue-Mitigation](https://github.com/jmsmuigai/Pesticide-Residue-Mitigation).
