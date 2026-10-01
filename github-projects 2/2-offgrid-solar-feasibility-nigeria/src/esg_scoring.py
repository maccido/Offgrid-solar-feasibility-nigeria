"""
World Bank E&S and gender-lens scoring helpers (simplified operationalisation).
Author: Mohammed Tukur Saidu, PhD
"""

import pandas as pd
import numpy as np


def gender_action_score(df: pd.DataFrame) -> pd.Series:
    """
    Composite gender-action indicator (0–100) based on:
    - female decision-making power
    - female respondent share (proxy for inclusion)
    - education gap
    """
    female_share = (df["respondent_gender"] == "Female").mean()
    female_decision_rate = df["female_decision"].mean()
    # Simple scoring – real projects used more elaborate matrices
    score = 40 * female_share + 40 * female_decision_rate + 20 * 0.6  # placeholder education weight
    return pd.Series({"gender_action_score": round(score * 100, 1)})


def es_risk_screen(community_stats: dict) -> dict:
    """
    Lightweight Environmental & Social risk screen
    (illustrative of the World Bank checklist applied in the pilots).
    """
    risks = {
        "land_acquisition": "Low" if community_stats.get("displaced_hh", 0) == 0 else "Medium",
        "biodiversity": "Low",
        "water_resources": "Low",
        "cultural_heritage": "Low",
        "labour_influx": "Medium" if community_stats.get("contractor_workers", 0) > 20 else "Low",
        "gender_based_violence": "Low–Medium (mitigation plan required)",
    }
    overall = "Category B (Moderate Risk)" if "Medium" in risks.values() else "Category C (Low Risk)"
    return {"risk_ratings": risks, "overall_category": overall}
