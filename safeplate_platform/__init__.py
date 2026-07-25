"""
SafePlate Kenya v2 - Pesticide Residue Mitigation & Organic Alternatives Platform
"""

__version__ = "2.0.0"
__author__ = "SafePlate Kenya Engineering Team"

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

__all__ = [
    "calculate_runoff",
    "HydrologyModel",
    "calculate_wash_efficiency",
    "WashingModel",
    "ACTIVE_CHEMICALS",
    "PCPB_BIOPESTICIDES",
    "ORGANIC_STATISTICS",
    "ALTERNATIVE_BIOPESTICIDES",
    "COUNTY_PRPI_INDEX",
    "MARKET_HOTSPOTS",
    "SafePlateGeminiAgent",
    "run_gemini_tasks"
]
