"""
SafePlate Kenya v6 - Master Mined Datasets
Includes Garissa Wholesale Market, Central-to-Garissa transit corridors,
pest & disease attribute mappings, active chemicals, PCPB biopesticides,
organic statistics, and alternatives register.
"""

MARKET_HOTSPOTS = [
    {
        "id": "githurai",
        "name": "Githurai Wholesale Market",
        "location": "Nairobi / Kiambu Border",
        "lat": -1.2015,
        "lng": 36.9185,
        "samples_tested": 142,
        "detectable_residue_pct": 81.2,
        "exceeding_eu_mrl_pct": 36.4,
        "primary_crop": "Tomatoes (Nyanya) & Sukuma Wiki",
        "crop_img": "assets/images/crop_tomatoes.png",
        "dominant_chemical": "Chlorfenapyr, Chlorpyrifos",
        "pests_diseases": "Tuta absoluta (Leafminer), Early Blight, Aphids",
        "mrl_status": "CRITICAL EXCEEDANCE",
        "phi_advice": "Enforce 14-day zero-synthetic spray window before harvest.",
        "transit_source": "Kirinyaga (Mwea) & Kiambu Farms"
    },
    {
        "id": "muthurwa",
        "name": "Muthurwa Central Market",
        "location": "Nairobi Central Wholesale",
        "lat": -1.2878,
        "lng": 36.8335,
        "samples_tested": 210,
        "detectable_residue_pct": 82.5,
        "exceeding_eu_mrl_pct": 38.1,
        "primary_crop": "Spinach & Cabbage",
        "crop_img": "assets/images/crop_spinach.png",
        "dominant_chemical": "Chlorfenapyr, Carbendazim, Acephate",
        "pests_diseases": "Downy Mildew, Black Rot, Cutworms",
        "mrl_status": "CRITICAL EXCEEDANCE",
        "phi_advice": "Wash in 1:3 vinegar solution prior to preparation.",
        "transit_source": "Nyandarua & Murang'a Farms"
    },
    {
        "id": "garissa",
        "name": "Garissa Wholesale Market",
        "location": "Garissa Central Town",
        "lat": -0.4532,
        "lng": 39.6460,
        "samples_tested": 95,
        "detectable_residue_pct": 79.4,
        "exceeding_eu_mrl_pct": 34.2,
        "primary_crop": "Tomatoes, Onions & Capsicum",
        "crop_img": "assets/images/crop_tomatoes.png",
        "dominant_chemical": "Chlorfenapyr, Acephate, Mancozeb",
        "pests_diseases": "Tuta absoluta, Thrips, Purple Blotch",
        "mrl_status": "HIGH EXCEEDANCE",
        "phi_advice": "Long-transit produce; soak in 2% salt water for 10 minutes.",
        "transit_source": "Kirinyaga & Thika Highway Transit Corridor"
    },
    {
        "id": "kangemi",
        "name": "Kangemi West Market",
        "location": "Nairobi West",
        "lat": -1.2642,
        "lng": 36.7450,
        "samples_tested": 118,
        "detectable_residue_pct": 76.5,
        "exceeding_eu_mrl_pct": 31.8,
        "primary_crop": "Spinach & Capsicum (Pilipili Hoho)",
        "crop_img": "assets/images/crop_capsicum.png",
        "dominant_chemical": "Acephate, Difenoconazole",
        "pests_diseases": "Aphids, Powdery Mildew, Spider Mites",
        "mrl_status": "HIGH EXCEEDANCE",
        "phi_advice": "Wash vegetables in 1% baking soda solution.",
        "transit_source": "Kiambu & Kajiado Farms"
    },
    {
        "id": "nakuru",
        "name": "Nakuru Main Wholesale",
        "location": "Nakuru Central",
        "lat": -0.2833,
        "lng": 36.0667,
        "samples_tested": 165,
        "detectable_residue_pct": 71.0,
        "exceeding_eu_mrl_pct": 25.5,
        "primary_crop": "Carrots & Peas",
        "crop_img": "assets/images/crop_carrots.png",
        "dominant_chemical": "Linuron, Lambda-Cyhalothrin",
        "pests_diseases": "Alternaria Leaf Blight, Root Knot Nematodes",
        "mrl_status": "MODERATE RISK",
        "phi_advice": "Peel carrot skins before consumption.",
        "transit_source": "Nyandarua & Mau Narok Farms"
    }
]

SUPPLY_CORRIDORS = [
    {
        "name": "Central-to-Garissa Highway Corridor",
        "origin": "Kirinyaga / Thika Farms",
        "destination": "Garissa Wholesale Market",
        "coords": [[-0.500, 37.280], [-0.850, 37.100], [-1.033, 37.070], [-1.000, 37.400], [-0.4532, 39.6460]],
        "commodities": "Tomatoes, Capsicum, Watermelon",
        "transit_time_hrs": 6.5
    },
    {
        "name": "Aberdare-to-Nairobi Wholesale Corridor",
        "origin": "Nyandarua & Kiambu Farms",
        "destination": "Githurai & Muthurwa Markets",
        "coords": [[-0.400, 36.500], [-0.783, 37.150], [-1.171, 36.835], [-1.2015, 36.9185], [-1.2878, 36.8335]],
        "commodities": "Kale (Sukuma Wiki), Spinach, Cabbage, Potatoes",
        "transit_time_hrs": 3.0
    }
]

ACTIVE_CHEMICALS = [
    {"name": "Chlorfenapyr", "who_class": "Class II", "eu_mrl_ppm": 0.01, "prevalence_pct": 28.4, "half_life_days": 14.2, "washing_reach_pct": 42.7},
    {"name": "Chlorpyrifos", "who_class": "Class II", "eu_mrl_ppm": 0.01, "prevalence_pct": 24.1, "half_life_days": 30.0, "washing_reach_pct": 38.2},
    {"name": "Acephate", "who_class": "Class II", "eu_mrl_ppm": 0.02, "prevalence_pct": 19.8, "half_life_days": 6.5, "washing_reach_pct": 25.0},
    {"name": "Lambda-Cyhalothrin", "who_class": "Class II", "eu_mrl_ppm": 0.02, "prevalence_pct": 16.5, "half_life_days": 21.0, "washing_reach_pct": 44.0},
    {"name": "Difenoconazole", "who_class": "Class II", "eu_mrl_ppm": 0.05, "prevalence_pct": 15.2, "half_life_days": 18.0, "washing_reach_pct": 32.0},
    {"name": "Linuron", "who_class": "Class II", "eu_mrl_ppm": 0.01, "prevalence_pct": 12.7, "half_life_days": 45.0, "washing_reach_pct": 35.0},
    {"name": "Carbendazim", "who_class": "Class Ib", "eu_mrl_ppm": 0.01, "prevalence_pct": 11.3, "half_life_days": 40.0, "washing_reach_pct": 28.0},
    {"name": "Imidacloprid", "who_class": "Class II", "eu_mrl_ppm": 0.01, "prevalence_pct": 10.5, "half_life_days": 35.0, "washing_reach_pct": 20.0}
]

ALTERNATIVE_BIOPESTICIDES = [
    {"name": "Azadirachtin 0.03% EC (Neemol)", "target_pests": "Tuta absoluta, Aphids, Whiteflies", "phi_days": 0, "efficacy_pct": 84.5},
    {"name": "Bacillus thuringiensis (Bt kurstaki)", "target_pests": "Caterpillars, Diamondback Moth", "phi_days": 0, "efficacy_pct": 88.0},
    {"name": "ICIPE 20 (Metarhizium anisopliae)", "target_pests": "Thrips, Spider Mites", "phi_days": 0, "efficacy_pct": 82.0},
    {"name": "Beauveria bassiana (Real Metarhizium)", "target_pests": "Whiteflies, Mealybugs", "phi_days": 0, "efficacy_pct": 80.5}
]

PCPB_BIOPESTICIDES = {"total_registered": 109, "applied_volume_share_pct": 2.0}
ORGANIC_STATISTICS = {"certified_hectares": 171298, "certified_farms": 62626, "koan_pgs_farmers": 1634}

COUNTY_PRPI_INDEX = [
    {"county": "Kirinyaga", "prpi_score": 88.5, "risk_category": "CRITICAL", "primary_crop": "Tomatoes (Mwea)", "lat": -0.500, "lng": 37.280},
    {"county": "Kiambu", "prpi_score": 85.2, "risk_category": "CRITICAL", "primary_crop": "Kale & Spinach", "lat": -1.171, "lng": 36.835},
    {"county": "Murang'a", "prpi_score": 79.4, "risk_category": "HIGH", "primary_crop": "French Beans", "lat": -0.783, "lng": 37.150},
    {"county": "Nyandarua", "prpi_score": 76.8, "risk_category": "HIGH", "primary_crop": "Potatoes & Cabbage", "lat": -0.400, "lng": 36.500},
    {"county": "Nakuru", "prpi_score": 74.1, "risk_category": "HIGH", "primary_crop": "Carrots & Peas", "lat": -0.283, "lng": 36.067},
    {"county": "Garissa", "prpi_score": 79.4, "risk_category": "HIGH", "primary_crop": "Tomatoes & Onions", "lat": -0.4532, "lng": 39.6460}
]
