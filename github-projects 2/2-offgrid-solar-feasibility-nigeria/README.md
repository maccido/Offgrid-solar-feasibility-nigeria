# Off-Grid Solar Feasibility Assessment – Northern Nigeria

**Author:** Mohammed Tukur Saidu, PhD  
**ORCID:** [0000-0003-0250-1311](https://orcid.org/0000-0003-0250-1311)  
**Contact:** maccido@gmail.com | [LinkedIn](https://www.linkedin.com/in/mohammed-tukur-saidu-7458a858)

---

## Overview

This repository documents the quantitative feasibility framework I developed while serving as Energy and Community Development Consultant for the League of Association, Kwarbai (2015–Present). It operationalises:

- Field-data collection protocols for energy-adoption barriers  
- World Bank Environmental & Social (E&S) and gender-lens frameworks (SDG 5 & SDG 7)  
- Techno-economic modelling of off-grid solar mini-grids and solar-home-systems  
- Bilingual (Hausa/English) stakeholder reporting templates  

The four pilot projects covered communities in Kaduna and neighbouring Northern Nigerian states.

## Research / Policy Questions

1. What are the primary demand-side and supply-side barriers to off-grid solar adoption in rural Northern Nigeria?  
2. How do gender dynamics affect household energy choices and willingness-to-pay?  
3. Under what cost, tariff and financing assumptions do the projects achieve positive NPV and acceptable LCOE?

## Key Deliverables in this Repo

| Component | Description |
|-----------|-------------|
| Survey instrument | Structured questionnaire (energy use, expenditure, gender roles, willingness-to-pay) |
| Data pipeline | Cleaning, indicator construction, World Bank E&S scoring |
| Techno-economic model | Simple LCOE / NPV calculator with sensitivity tables |
| Dashboard | Power BI–ready data model + Python visualisation layer |
| Stakeholder brief | Template for bilingual community feedback reports |

## Repository Structure

```
2-offgrid-solar-feasibility-nigeria/
├── data/
│   ├── raw_survey_sample.csv
│   └── processed_indicators.csv
├── notebooks/
│   └── 01_feasibility_analysis.ipynb
├── src/
│   ├── survey_prep.py
│   ├── techno_economic.py
│   └── esg_scoring.py
├── templates/
│   └── stakeholder_brief_template.md
├── results/
│   ├── tables/
│   └── figures/
├── requirements.txt
└── README.md
```

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/offgrid-solar-feasibility-nigeria.git
cd offgrid-solar-feasibility-nigeria

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

jupyter notebook notebooks/01_feasibility_analysis.ipynb
```

## Methodology Highlights

- **Demand assessment** – Household energy diaries, stated-preference WTP, gender-disaggregated analysis.  
- **Supply & cost modelling** – Component costing (panels, batteries, inverters), O&M, diesel baseline comparison.  
- **Risk & safeguards** – World Bank E&S screening checklist + gender action indicators.  
- **Financial metrics** – Levelised Cost of Electricity (LCOE), Net Present Value, payback period under alternative tariff regimes.  
- **Sensitivity** – One-way and multi-way sensitivity on CAPEX, diesel price, discount rate, and collection rates.

## Citation & Attribution

This work builds on field research conducted under the League of Association, Kwarbai consultancy. Academic citation of the modelling approach should reference:

> Saidu, M. T. – Energy and Community Development Consultant reports (2015–Present) and related peer-reviewed energy-economics publications (see Google Scholar / ORCID).

## License

MIT License for academic and non-commercial use. Field instruments and community data remain subject to the original ethical clearance and data-sharing agreements.

## Contact

Open to collaboration on renewable-energy feasibility, gender-and-energy research, and applied policy work in Sub-Saharan Africa.  
maccido@gmail.com | maccido@fuez.edu.ng
