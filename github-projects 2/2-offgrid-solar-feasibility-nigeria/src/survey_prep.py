"""
Survey data preparation and indicator construction
for off-grid solar feasibility studies.
Author: Mohammed Tukur Saidu, PhD
"""

import pandas as pd
import numpy as np
from pathlib import Path


def generate_sample_survey(n: int = 420, seed: int = 7) -> pd.DataFrame:
    """
    Generate a realistic synthetic household survey dataset
    that mirrors the structure used in the Northern Nigeria pilots.
    """
    rng = np.random.default_rng(seed)

    communities = ["Kwarbai-A", "Kwarbai-B", "Samaru", "Basawa", "Shika"]
    gender = rng.choice(["Female", "Male"], size=n, p=[0.52, 0.48])
    hh_size = rng.integers(3, 12, size=n)
    monthly_income = rng.lognormal(mean=10.5, sigma=0.6, size=n)   # NGN
    monthly_energy_exp = rng.lognormal(mean=8.2, sigma=0.5, size=n)
    has_grid = rng.choice([0, 1], size=n, p=[0.78, 0.22])
    uses_generator = rng.choice([0, 1], size=n, p=[0.55, 0.45])
    uses_kerosene = rng.choice([0, 1], size=n, p=[0.35, 0.65])
    wtp_solar = rng.lognormal(mean=7.8, sigma=0.7, size=n)         # monthly WTP
    decision_maker = rng.choice(
        ["Female head / joint", "Male only", "Other"],
        size=n, p=[0.41, 0.48, 0.11]
    )
    education = rng.choice(
        ["None", "Primary", "Secondary", "Tertiary"],
        size=n, p=[0.22, 0.35, 0.28, 0.15]
    )

    df = pd.DataFrame({
        "hh_id": [f"HH{i:04d}" for i in range(1, n + 1)],
        "community": rng.choice(communities, size=n),
        "respondent_gender": gender,
        "hh_size": hh_size,
        "monthly_income_ngn": np.round(monthly_income, 0),
        "monthly_energy_exp_ngn": np.round(monthly_energy_exp, 0),
        "has_grid_connection": has_grid,
        "uses_generator": uses_generator,
        "uses_kerosene": uses_kerosene,
        "wtp_solar_monthly_ngn": np.round(wtp_solar, 0),
        "energy_decision_maker": decision_maker,
        "education_level": education,
    })
    return df


def construct_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build key analytical indicators used in the feasibility reports.
    """
    out = df.copy()
    out["energy_burden"] = out["monthly_energy_exp_ngn"] / out["monthly_income_ngn"]
    out["wtp_share_of_income"] = out["wtp_solar_monthly_ngn"] / out["monthly_income_ngn"]
    out["female_decision"] = (out["energy_decision_maker"] == "Female head / joint").astype(int)
    out["high_burden"] = (out["energy_burden"] > 0.10).astype(int)
    out["offgrid"] = (out["has_grid_connection"] == 0).astype(int)
    return out


def gender_disaggregated_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summary statistics by respondent gender – core of the gender-lens analysis."""
    cols = [
        "monthly_income_ngn", "monthly_energy_exp_ngn",
        "wtp_solar_monthly_ngn", "energy_burden", "wtp_share_of_income"
    ]
    return df.groupby("respondent_gender")[cols].agg(["mean", "median", "std"]).round(2)
