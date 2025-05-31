# Twinner Production Scenario Calculator

This Python script simulates different production scenarios for a cable manufacturing line involving an **extruder** and a **twinner**. Given a total production order (in meters), the script calculates:

- Twinner idle time based on spool color combinations (white/black)
- Estimated PVC waste percentage due to color change
- Working time for the twinner

The output is saved as an Excel file (`production_scenarios.xlsx`) for further analysis.

---

## 📦 Requirements

Make sure you have the following installed:

- Python 3.7+
- `pandas` library
- Excel-compatible software to view the output (e.g., Microsoft Excel, LibreOffice)

You can install the required Python package via pip:

```bash
pip install pandas
