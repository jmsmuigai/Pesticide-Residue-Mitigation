"""
FastAPI REST API Service for SafePlate Kenya v3
Exposes HTTP 200 REST Endpoints for Hydrology, Wash Calculations,
MOH Advisory Solutions (Ref: MOH/ADM/1/2/52), Chemical Active Databases, and Gemini Agent.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
import json
import os

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
from .mine_and_clean import process_and_clean_data

app = FastAPI(
    title="SafePlate Kenya v3 API",
    description="Official Response & Technical Solutions for MOH Advisory Ref: MOH/ADM/1/2/52 on Pesticide Residues",
    version="3.0.0"
)

class HydrologyRequest(BaseModel):
    precipitation_mm: float = Field(55.0, description="Precipitation in mm")
    curve_number: float = Field(79.0, description="SCS Curve Number (0-100)")

class WashRequest(BaseModel):
    chemical: str = Field("chlorfenapyr", description="Active ingredient name")
    solution_type: str = Field("vinegar", description="cold_water, salt_water, vinegar, baking_soda")
    soak_minutes: float = Field(5.0, description="Soak time in minutes")

@app.get("/health")
def health_check():
    return {
        "status": "HEALTHY",
        "service": "SafePlate Kenya v3 MOH Advisory Response Platform",
        "moh_ref": "MOH/ADM/1/2/52",
        "hydrology_proof": calculate_runoff(55.0, 79.0),
        "wash_proof": calculate_wash_efficiency("chlorfenapyr", "vinegar", 5.0)
    }

@app.get("/moh/advisory")
def get_moh_advisory_solution():
    cleaned = process_and_clean_data()
    return cleaned["moh_advisory_solution"]

@app.get("/actives")
def get_actives():
    return {"total_actives": len(ACTIVE_CHEMICALS), "actives": ACTIVE_CHEMICALS}

@app.get("/counties")
def get_counties():
    return {"total_counties": len(COUNTY_PRPI_INDEX), "counties": COUNTY_PRPI_INDEX}

@app.get("/alternatives")
def get_alternatives():
    return {"total_alternatives": len(ALTERNATIVE_BIOPESTICIDES), "alternatives": ALTERNATIVE_BIOPESTICIDES}

@app.post("/hydrology/calculate")
def post_hydrology(req: HydrologyRequest):
    q_val = calculate_runoff(req.precipitation_mm, req.curve_number)
    return {
        "precipitation_mm": req.precipitation_mm,
        "curve_number": req.curve_number,
        "runoff_Q_mm": q_val,
        "formatted_Q": f"{round(q_val, 2):.2f} mm"
    }

@app.post("/wash")
def post_wash(req: WashRequest):
    wm = WashingModel()
    remaining = wm.calculate_remaining(
        chemical=req.chemical,
        solution_type=req.solution_type,
        soak_minutes=req.soak_minutes
    )
    return {
        "chemical": req.chemical,
        "solution_type": req.solution_type,
        "soak_minutes": req.soak_minutes,
        "remaining_fraction": remaining,
        "remaining_percentage": f"{remaining * 100:.1f}%",
        "removed_percentage": f"{(1.0 - remaining) * 100:.1f}%"
    }
