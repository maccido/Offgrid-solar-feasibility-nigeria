"""
Simple techno-economic model for off-grid solar mini-grids / SHS.
Author: Mohammed Tukur Saidu, PhD
"""

import numpy as np
import pandas as pd


def lcoe(
    capex: float,
    opex_annual: float,
    annual_generation_kwh: float,
    lifetime: int = 20,
    discount_rate: float = 0.10,
    degradation: float = 0.005,
) -> float:
    """
    Levelised Cost of Electricity (USD/kWh or NGN/kWh – units must be consistent).
    """
    years = np.arange(1, lifetime + 1)
    generation = annual_generation_kwh * (1 - degradation) ** (years - 1)
    discounted_gen = generation / (1 + discount_rate) ** years
    discounted_opex = opex_annual / (1 + discount_rate) ** years
    total_cost = capex + discounted_opex.sum()
    total_gen = discounted_gen.sum()
    return total_cost / total_gen if total_gen > 0 else np.nan


def npv(
    cashflows: np.ndarray,
    discount_rate: float = 0.10,
) -> float:
    """Net Present Value of a cash-flow series (year 0 = CAPEX)."""
    years = np.arange(len(cashflows))
    return np.sum(cashflows / (1 + discount_rate) ** years)


def sensitivity_table(
    base_capex: float,
    base_opex: float,
    base_gen: float,
    param_ranges: dict,
) -> pd.DataFrame:
    """
    One-way sensitivity on LCOE.
    param_ranges example:
        {"capex": [0.8, 0.9, 1.0, 1.1, 1.2],
         "discount_rate": [0.08, 0.10, 0.12, 0.14]}
    """
    results = []
    for param, values in param_ranges.items():
        for v in values:
            kwargs = {
                "capex": base_capex,
                "opex_annual": base_opex,
                "annual_generation_kwh": base_gen,
                "discount_rate": 0.10,
            }
            if param == "capex":
                kwargs["capex"] = base_capex * v
            elif param == "opex":
                kwargs["opex_annual"] = base_opex * v
            elif param == "generation":
                kwargs["annual_generation_kwh"] = base_gen * v
            elif param == "discount_rate":
                kwargs["discount_rate"] = v
            results.append({
                "parameter": param,
                "multiplier_or_value": v,
                "lcoe": lcoe(**kwargs),
            })
    return pd.DataFrame(results)


def diesel_baseline_cost(
    diesel_price_per_litre: float,
    litres_per_kwh: float = 0.35,
    o_and_m_share: float = 0.15,
) -> float:
    """Simple diesel generation cost per kWh (fuel + O&M)."""
    fuel = diesel_price_per_litre * litres_per_kwh
    return fuel * (1 + o_and_m_share)
