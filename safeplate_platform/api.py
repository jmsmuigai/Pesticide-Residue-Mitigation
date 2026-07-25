"""
FastAPI REST API Service for SafePlate Kenya v2
Exposes 8 HTTP 200 REST Endpoints for Hydrology, Wash Calculations,
Chemical Active Databases, Alternatives Register, and Gemini Advisory Engine.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

from .hydrology import calculate_runoff, HydrologyModel
from .washing import calculate_wash_efficiency, WashingModel
from .datasets import (
    ACTIVE_CHEMICALS,
    PCPB_BIOPESTICIDES,
    ORGANIC_STATISTICS,
    ALTERNATIVE_BIOPESTICIDES,
    COUNTY_PRPI_INDEX,
    MARKET_HOTSPOTS
)
from .gemini_agent import SafePlateGeminiAgent, run_gemini_tasks

app = FastAPI(
    title="SafePlate Kenya v2 API",
    description="Pesticide Residue Mitigation, Hydrological Modeling & Organic Alternatives Service",
    version="2.0.0"
)

# --- Request / Response Models ---
class HydrologyRequest(BaseModel):
    precipitation_mm: float = Field(55.0, description="Precipitation in mm")
    curve_number: float = Field(79.0, description="SCS Curve Number (0-100)")

class WashRequest(BaseModel):
    chemical: str = Field("chlorfenapyr", description="Active ingredient name")
    solution_type: str = Field("cold_water", description="cold_water, salt_water, vinegar, baking_soda")
    soak_minutes: float = Field(5.0, description="Soak time in minutes")
    peeling: bool = Field(False, description="Whether skin is peeled")

class GeminiAdvisoryRequest(BaseModel):
    county: str = Field("Kirinyaga", description="County name")
    crop: str = Field("Tomatoes", description="Horticultural crop")
    target_lang: str = Field("kiswahili", description="kiswahili, kikuyu, dholuo, english")

# --- 8 REST Endpoints ---

@app.get("/health", summary="1. Health Check Endpoint")
def health_check():
    return {
        "status": "HEALTHY",
        "service": "SafePlate Kenya v2 FastAPI Platform",
        "hydrology_proof": calculate_runoff(55.0, 79.0),
        "wash_proof": calculate_wash_efficiency("chlorfenapyr", "cold_water", 5.0)
    }

@app.get("/actives", summary="2. Eight Active Chemicals & Toxicology")
def get_actives():
    return {
        "total_actives": len(ACTIVE_CHEMICALS),
        "actives": ACTIVE_CHEMICALS
    }

@app.get("/counties", summary="3. 47 County Residue Pressure Index (PRPI)")
def get_counties():
    return {
        "total_counties": len(COUNTY_PRPI_INDEX),
        "counties": COUNTY_PRPI_INDEX
    }

@app.get("/alternatives", summary="4. 12 Biopesticide Alternatives Register")
def get_alternatives():
    return {
        "total_alternatives": len(ALTERNATIVE_BIOPESTICIDES),
        "alternatives": ALTERNATIVE_BIOPESTICIDES
    }

@app.post("/hydrology/calculate", summary="5. SCS-CN Pesticide Runoff Calculator")
def post_hydrology(req: HydrologyRequest):
    q_val = calculate_runoff(req.precipitation_mm, req.curve_number)
    return {
        "precipitation_mm": req.precipitation_mm,
        "curve_number": req.curve_number,
        "runoff_Q_mm": q_val,
        "formatted_Q": f"{round(q_val, 2):.2f} mm",
        "is_benchmark": req.precipitation_mm == 55.0 and req.curve_number == 79.0 and round(q_val, 2) == 15.80
    }

@app.post("/wash", summary="6. Consumer Wash Efficiency Calculator")
def post_wash(req: WashRequest):
    wm = WashingModel()
    remaining = wm.calculate_remaining(
        chemical=req.chemical,
        solution_type=req.solution_type,
        soak_minutes=req.soak_minutes,
        peeling=req.peeling
    )
    return {
        "chemical": req.chemical,
        "solution_type": req.solution_type,
        "soak_minutes": req.soak_minutes,
        "peeling": req.peeling,
        "remaining_fraction": remaining,
        "remaining_percentage": f"{remaining * 100:.1f}%",
        "removed_percentage": f"{(1.0 - remaining) * 100:.1f}%"
    }

@app.get("/pcpb/biopesticides", summary="7. PCPB 109 Biopesticide Register & BioCOPPA")
def get_pcpb_info():
    return {
        "pcpb_summary": PCPB_BIOPESTICIDES,
        "organic_summary": ORGANIC_STATISTICS,
        "market_hotspots": MARKET_HOTSPOTS
    }

@app.post("/gemini/advisory", summary="8. Gemini Multilingual Advisory Engine")
def post_gemini_advisory(req: GeminiAdvisoryRequest):
    agent = SafePlateGeminiAgent()
    brief = agent.execute_task_4_county_briefs(req.county)
    trans = agent.execute_task_2_translate(brief["priority_action"], req.target_lang)
    return {
        "county": req.county,
        "crop": req.crop,
        "language": req.target_lang,
        "advisor_brief": brief,
        "translation": trans
    }
