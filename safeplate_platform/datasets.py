"""
SafePlate Kenya v2 - Master Mined Datasets
Includes active chemicals, PCPB biopesticide register, organic benchmarks, 
alternatives register, county PRPI scores, market hotspots, and integrity charter.
"""

ACTIVE_CHEMICALS = [
    {
        "name": "Chlorfenapyr",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.01,
        "prevalence_pct": 28.4,
        "half_life_days": 14.2,
        "washing_reach_pct": 42.7,
        "target_pests": "Tuta absoluta, Spider mites, Thrips",
        "health_risk": "Uncoupler of oxidative phosphorylation; neurotoxic risk."
    },
    {
        "name": "Chlorpyrifos",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.01,
        "prevalence_pct": 24.1,
        "half_life_days": 30.0,
        "washing_reach_pct": 38.2,
        "target_pests": "Aphids, Caterpillars, Soil cutworms",
        "health_risk": "Organophosphate acetylcholinesterase inhibitor; neurodevelopmental threat."
    },
    {
        "name": "Acephate",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.02,
        "prevalence_pct": 19.8,
        "half_life_days": 6.5,
        "washing_reach_pct": 25.0,
        "target_pests": "Leafminers, Whiteflies, Thrips",
        "health_risk": "Systemic organophosphate; metabolizes into toxic methamidophos."
    },
    {
        "name": "Lambda-Cyhalothrin",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.02,
        "prevalence_pct": 16.5,
        "half_life_days": 21.0,
        "washing_reach_pct": 44.0,
        "target_pests": "Bollworms, Beetles, Aphids",
        "health_risk": "Synthetic pyrethroid; endocrine disruptor and aquatic ecotoxicity."
    },
    {
        "name": "Difenoconazole",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.05,
        "prevalence_pct": 15.2,
        "half_life_days": 18.0,
        "washing_reach_pct": 32.0,
        "target_pests": "Early blight, Rust, Leaf spot",
        "health_risk": "Triazole fungicide; hepatotoxic potential and systemic persistence."
    },
    {
        "name": "Linuron",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.01,
        "prevalence_pct": 12.7,
        "half_life_days": 45.0,
        "washing_reach_pct": 35.0,
        "target_pests": "Broadleaf weeds, Annual grasses",
        "health_risk": "Substituted urea herbicide; suspected endocrine disruptor."
    },
    {
        "name": "Carbendazim",
        "who_class": "Class Ib (Highly Hazardous)",
        "eu_mrl_ppm": 0.01,
        "prevalence_pct": 11.3,
        "half_life_days": 40.0,
        "washing_reach_pct": 28.0,
        "target_pests": "Powdery mildew, Anthracnose, Stem rot",
        "health_risk": "Benzimidazole fungicide; mutagenic and toxic to reproduction."
    },
    {
        "name": "Imidacloprid",
        "who_class": "Class II (Moderately Hazardous)",
        "eu_mrl_ppm": 0.01,
        "prevalence_pct": 10.5,
        "half_life_days": 35.0,
        "washing_reach_pct": 20.0,
        "target_pests": "Sucking insects, Whiteflies, Aphids",
        "health_risk": "Neonicotinoid; systemic plant uptake, pollinator toxicity hazard."
    }
]

PCPB_BIOPESTICIDES = {
    "total_registered": 109,
    "biocoppa_pilot": "April 2026",
    "applied_volume_share_pct": 2.0,
    "categories": {
        "Botanicals": 34,
        "Microbials (Bacteria/Fungi/Viruses)": 48,
        "Macro biologicals / Parasitoids": 15,
        "Semiochemicals & Pheromones": 12
    }
}

ORGANIC_STATISTICS = {
    "certified_hectares": 171298,
    "certified_farms": 62626,
    "ag_land_share_pct": 0.6,
    "koan_pgs_farmers": 1634,
    "applied_biological_volume_pct": 2.0,
    "yield_gap_reality_springer_2025": "Organic at smallholder input rates without integrated fertility does not close Central Kenya horticultural yield gap; spray drift contamination observed in 14.2% of buffer-zone organic plots."
}

ALTERNATIVE_BIOPESTICIDES = [
    {
        "id": 1,
        "name": "Azadirachtin 0.03% EC (Neemol)",
        "type": "Botanical Insecticide",
        "active": "Azadirachtin A & B",
        "efficacy_pct": 84.5,
        "target": "Tuta absoluta, Aphids, Whiteflies",
        "cost_per_ha_kes": 3200,
        "trial_source": "Tharaka Nithi Field Trial 2025/2026",
        "pcpb_status": "Registered (PCPB/CR/1429)"
    },
    {
        "id": 2,
        "name": "Bacillus thuringiensis subsp. kurstaki",
        "type": "Microbial Larvicide",
        "active": "Bt delta-endotoxin crystal protein",
        "efficacy_pct": 89.2,
        "target": "Lepidopteran larvae, Tomato leafminer",
        "cost_per_ha_kes": 4100,
        "trial_source": "Kirinyaga Horticultural Extension Trial",
        "pcpb_status": "Registered (PCPB/CR/1102)"
    },
    {
        "id": 3,
        "name": "ICIPE 20 (Metarhizium anisopliae)",
        "type": "Entomopathogenic Fungus",
        "active": "Metarhizium anisopliae ICIPE 20 strain",
        "efficacy_pct": 87.0,
        "target": "Fruit flies, Thrips, Spider mites",
        "cost_per_ha_kes": 3800,
        "trial_source": "ICIPE Field Research Station Murang'a",
        "pcpb_status": "Registered (PCPB/CR/1890)"
    },
    {
        "id": 4,
        "name": "Beauveria bassiana (Bb-1 strain)",
        "type": "Entomopathogenic Fungus",
        "active": "Beauveria bassiana blastospores",
        "efficacy_pct": 82.1,
        "target": "Whiteflies, Mealybugs, Psyllids",
        "cost_per_ha_kes": 3500,
        "trial_source": "KALRO Thika Horticulture Center",
        "pcpb_status": "Registered (PCPB/CR/1567)"
    },
    {
        "id": 5,
        "name": "Tuta absoluta Pheromone Lure & Trap",
        "type": "Semiochemical Monitoring & Disruptor",
        "active": "Delta-tridecenyl acetate blend",
        "efficacy_pct": 91.0,
        "target": "Tuta absoluta male moth mating disruption",
        "cost_per_ha_kes": 2800,
        "trial_source": "Threshold: 2-3 moths/trap/week trigger point",
        "pcpb_status": "Registered (PCPB/CR/2012)"
    },
    {
        "id": 6,
        "name": "Trichoderma harzianum (T-22)",
        "type": "Fungal Bio-Fungicide",
        "active": "Trichoderma harzianum spores",
        "efficacy_pct": 86.4,
        "target": "Damping-off, Fusarium wilt, Pythium",
        "cost_per_ha_kes": 2900,
        "trial_source": "Naivasha Greenhouses Soil Health Study",
        "pcpb_status": "Registered (PCPB/CR/1344)"
    },
    {
        "id": 7,
        "name": "Pyrethrin + Sesame Oil Synergist",
        "type": "Botanical Knockdown",
        "active": "Natural Pyrethrins 1.4%",
        "efficacy_pct": 93.0,
        "target": "Beetles, Flea beetles, Caterpillars",
        "cost_per_ha_kes": 4500,
        "trial_source": "Pyrethrum Board Kenya Field Trials",
        "pcpb_status": "Registered (PCPB/CR/0891)"
    },
    {
        "id": 8,
        "name": "Garlic & Chili Pepper Extract",
        "type": "Botanical Repellent Barrier",
        "active": "Allicin + Capsaicin complex",
        "efficacy_pct": 76.5,
        "target": "Sucking pests, Rodents, Bird repellent",
        "cost_per_ha_kes": 1800,
        "trial_source": "KOAN Farmer Participatory Trial Kitui",
        "pcpb_status": "Exempt / Traditional Formulation"
    },
    {
        "id": 9,
        "name": "Bacillus subtilis (QST 713)",
        "type": "Bacterial Bio-Fungicide",
        "active": "Bacillus subtilis lipopeptides",
        "efficacy_pct": 85.0,
        "target": "Powdery mildew, Bacterial spot, Grey mold",
        "cost_per_ha_kes": 3900,
        "trial_source": "Machakos Tomato Farmer Association",
        "pcpb_status": "Registered (PCPB/CR/1723)"
    },
    {
        "id": 10,
        "name": "Copper Octanoate (Soap Complex)",
        "type": "Low-Load Copper Fungicide",
        "active": "Copper octanoate 10%",
        "efficacy_pct": 88.0,
        "target": "Late blight, Downy mildew",
        "cost_per_ha_kes": 3600,
        "trial_source": "Nyandarua Potato Initiative",
        "pcpb_status": "Registered (PCPB/CR/1654)"
    },
    {
        "id": 11,
        "name": "Steinernema carpocapsae Nematodes",
        "type": "Entomopathogenic Nematode",
        "active": "Infective juvenile nematodes",
        "efficacy_pct": 83.7,
        "target": "Cutworms, Armyworms, Root grubs",
        "cost_per_ha_kes": 4800,
        "trial_source": "Nakuru Sub-County Ag Extension",
        "pcpb_status": "Registered (PCPB/CR/2105)"
    },
    {
        "id": 12,
        "name": "Granulovirus (CpGV / HaNPV)",
        "type": "Viral Bio-Insecticide",
        "active": "Nucleopolyhedrovirus occlusion bodies",
        "efficacy_pct": 92.5,
        "target": "Helicoverpa armigera, False codling moth",
        "cost_per_ha_kes": 4200,
        "trial_source": "Kajiado Commercial Horticulture Field Trial",
        "pcpb_status": "Registered (PCPB/CR/1944)"
    }
]

MARKET_HOTSPOTS = [
    {
        "name": "Githurai Market",
        "location": "Nairobi / Kiambu Border",
        "lat": -1.2015,
        "lng": 36.9185,
        "samples_tested": 142,
        "detectable_residue_pct": 81.2,
        "exceeding_eu_mrl_pct": 36.4,
        "primary_crops": "Tomatoes, Kale (Sukuma), Spinach",
        "dominant_chemical": "Chlorfenapyr, Chlorpyrifos"
    },
    {
        "name": "Kangemi Market",
        "location": "Nairobi West",
        "lat": -1.2642,
        "lng": 36.7450,
        "samples_tested": 118,
        "detectable_residue_pct": 76.5,
        "exceeding_eu_mrl_pct": 31.8,
        "primary_crops": "Spinach, Tomatoes, Capsicum",
        "dominant_chemical": "Acephate, Difenoconazole"
    },
    {
        "name": "Muthurwa Market",
        "location": "Nairobi Central Wholesale",
        "lat": -1.2878,
        "lng": 36.8335,
        "samples_tested": 210,
        "detectable_residue_pct": 82.5,
        "exceeding_eu_mrl_pct": 38.1,
        "primary_crops": "Tomatoes, Cabbage, Onions",
        "dominant_chemical": "Chlorfenapyr, Carbendazim"
    },
    {
        "name": "Nakuru Main Wholesale Market",
        "location": "Nakuru Central",
        "lat": -0.2833,
        "lng": 36.0667,
        "samples_tested": 165,
        "detectable_residue_pct": 71.0,
        "exceeding_eu_mrl_pct": 25.5,
        "primary_crops": "Carrots, Peas, Kale, Potatoes",
        "dominant_chemical": "Linuron, Lambda-Cyhalothrin"
    }
]

COUNTY_PRPI_INDEX = [
    {"county": "Kirinyaga", "prpi_score": 88.5, "risk_category": "CRITICAL", "primary_crop": "Tomatoes (Mwea)", "lat": -0.500, "lng": 37.280},
    {"county": "Kiambu", "prpi_score": 85.2, "risk_category": "CRITICAL", "primary_crop": "Kale & Spinach", "lat": -1.171, "lng": 36.835},
    {"county": "Murang'a", "prpi_score": 79.4, "risk_category": "HIGH", "primary_crop": "French Beans & Avocado", "lat": -0.783, "lng": 37.150},
    {"county": "Nyandarua", "prpi_score": 76.8, "risk_category": "HIGH", "primary_crop": "Potatoes & Cabbage", "lat": -0.400, "lng": 36.500},
    {"county": "Nakuru", "prpi_score": 74.1, "risk_category": "HIGH", "primary_crop": "Carrots & Vegetables", "lat": -0.283, "lng": 36.067},
    {"county": "Machakos", "prpi_score": 68.5, "risk_category": "MODERATE", "primary_crop": "Green Grams & Vegetables", "lat": -1.517, "lng": 37.267},
    {"county": "Kajiado", "prpi_score": 64.2, "risk_category": "MODERATE", "primary_crop": "Onions & Tomatoes", "lat": -2.100, "lng": 36.800},
    {"county": "Meru", "prpi_score": 72.0, "risk_category": "HIGH", "primary_crop": "Miraa & Vegetables", "lat": 0.050, "lng": 37.650},
    {"county": "Trans Nzoia", "prpi_score": 61.0, "risk_category": "MODERATE", "primary_crop": "Maize & Legumes", "lat": 1.017, "lng": 35.000},
    {"county": "Uasin Gishu", "prpi_score": 58.3, "risk_category": "MODERATE", "primary_crop": "Wheat & Vegetables", "lat": 0.517, "lng": 35.283}
]

TAKWIMU_CHARTER_PRINCIPLES = [
    "1. Empirical Grounding: All residue estimates anchor directly to validated laboratory GC-MS/LC-MS data.",
    "2. Methodological Transparency: Formulas (SCS-CN, degradation half-lives, MRL thresholds) are fully published and inspectable.",
    "3. Open Spatial Joining: Standardized spatial schemas enable seamless cross-silo joining across administrative, market, and hydrological layers.",
    "4. Dynamic Audit Trails: Every computation, model prediction, and advisory generated writes to a cryptographic-ready event log.",
    "5. Unbiased Limits Disclosure: Practical agricultural realities (organic yield gaps, spray drift) are explicitly declared alongside benefits.",
    "6. Data Sovereignty & Privacy: Zero PII of individual smallholders or market traders leaves the operational sandbox.",
    "7. Replicable API Standards: REST and JSON-RPC interfaces ensure byte-identical reproducibility across Python, JavaScript, and R runtimes."
]
