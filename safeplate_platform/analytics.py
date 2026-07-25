"""
SafePlate Kenya v4 - Python Trend Analytics Engine
Computes 2020-2026 historical residue time series, Red Zone market heatmaps,
and cellular toxicity impact metrics.
"""

import json
import os
from typing import Dict, Any, List

TREND_SERIES_DATA = [
    {"year": 2020, "detectable_residue_pct": 62.4, "exceeding_mrl_pct": 21.0, "organic_ha": 94000, "biopesticides_count": 52},
    {"year": 2021, "detectable_residue_pct": 65.8, "exceeding_mrl_pct": 24.2, "organic_ha": 112000, "biopesticides_count": 64},
    {"year": 2022, "detectable_residue_pct": 71.0, "exceeding_mrl_pct": 27.5, "organic_ha": 135000, "biopesticides_count": 78},
    {"year": 2023, "detectable_residue_pct": 74.2, "exceeding_mrl_pct": 29.8, "organic_ha": 148000, "biopesticides_count": 89},
    {"year": 2024, "detectable_residue_pct": 76.5, "exceeding_mrl_pct": 31.4, "organic_ha": 159000, "biopesticides_count": 98},
    {"year": 2025, "detectable_residue_pct": 77.2, "exceeding_mrl_pct": 32.5, "organic_ha": 166000, "biopesticides_count": 104},
    {"year": 2026, "detectable_residue_pct": 77.8, "exceeding_mrl_pct": 33.0, "organic_ha": 171298, "biopesticides_count": 109}
]

RED_ZONES_HEATMAP = [
    {
        "zone_name": "Githurai Wholesale Hub",
        "county": "Kiambu / Nairobi Border",
        "risk_tier": "CRITICAL RED ZONE",
        "score": 92.4,
        "detectable_pct": 81.2,
        "mrl_exceed_pct": 36.4,
        "primary_crops": ["Tomatoes", "Sukuma Wiki (Kale)"],
        "top_active": "Chlorfenapyr (28.4%)"
    },
    {
        "zone_name": "Muthurwa Central Market",
        "county": "Nairobi County",
        "risk_tier": "CRITICAL RED ZONE",
        "score": 90.1,
        "detectable_pct": 82.5,
        "mrl_exceed_pct": 38.1,
        "primary_crops": ["Tomatoes", "Cabbage"],
        "top_active": "Carbendazim & Acephate"
    },
    {
        "zone_name": "Mwea Irrigation Belt",
        "county": "Kirinyaga County",
        "risk_tier": "CRITICAL RED ZONE",
        "score": 88.5,
        "detectable_pct": 84.0,
        "mrl_exceed_pct": 35.2,
        "primary_crops": ["Tomatoes", "French Beans"],
        "top_active": "Chlorfenapyr & Lambda-Cyhalothrin"
    },
    {
        "zone_name": "Kangemi West Market",
        "county": "Nairobi West",
        "risk_tier": "HIGH RED ZONE",
        "score": 85.2,
        "detectable_pct": 76.5,
        "mrl_exceed_pct": 31.8,
        "primary_crops": ["Spinach", "Capsicum"],
        "top_active": "Acephate & Chlorpyrifos"
    },
    {
        "zone_name": "Nakuru Main Wholesale",
        "county": "Nakuru County",
        "risk_tier": "MODERATE WARNING ZONE",
        "score": 74.1,
        "detectable_pct": 71.0,
        "mrl_exceed_pct": 25.5,
        "primary_crops": ["Carrots", "Peas"],
        "top_active": "Linuron"
    }
]

CELL_TOXICITY_PATHWAY = [
    {
        "stage": 1,
        "title": "1. Field Crop Application",
        "title_sw": "1. Kunyunyizia Shambani",
        "description": "Synthetic chemical (e.g. Chlorfenapyr, Chlorpyrifos) sprayed onto vegetable leaves."
    },
    {
        "stage": 2,
        "title": "2. Produce Residue Transport",
        "title_sw": "2. Usafirishaji wa Mboga Zenye Sumu",
        "description": "Unwashed produce transported to markets carrying surface and systemic residues."
    },
    {
        "stage": 3,
        "title": "3. Human Ingestion & Gut Absorption",
        "title_sw": "3. Kula na Kuingia Tumboni",
        "description": "Unwashed vegetables consumed; residues pass through stomach lining into intestinal bloodstream."
    },
    {
        "stage": 4,
        "title": "4. Bloodstream Transit",
        "title_sw": "4. Kupita Kwenye Damu",
        "description": "Lipophilic compounds (log Kow > 4.0) circulate via plasma proteins to body tissues."
    },
    {
        "stage": 5,
        "title": "5. Cellular Penetration & Stress",
        "title_sw": "5. Kuingia Kwenye Seli na Kuleta Athari",
        "description": "Pesticides uncouple mitochondrial oxidative phosphorylation, triggering cellular oxidative stress."
    }
]

def generate_analytics_data() -> Dict[str, Any]:
    print("=== Generating Python Trend Analytics & Red Zone Data ===")
    payload = {
        "metadata": {
            "version": "4.0.0",
            "timeframe": "2020-2026",
            "total_markets_analyzed": 47
        },
        "trend_series": TREND_SERIES_DATA,
        "red_zones_heatmap": RED_ZONES_HEATMAP,
        "cell_toxicity_pathway": CELL_TOXICITY_PATHWAY
    }
    
    out_path = os.path.join(os.path.dirname(__file__), "trend_analytics_data.json")
    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2)
        
    print(f"Trend analytics payload written successfully to: {out_path}")
    return payload

if __name__ == "__main__":
    generate_analytics_data()
