# 📦 Retail Sales Forecasting & Inventory Optimization System

## 🚀 Project Overview
This project is an end-to-end data science solution designed to solve the "Stockout vs. Overstock" dilemma in retail. Using **Random Forest Regression** for demand forecasting and **Statistical Operations Research** for inventory replenishment, the system provides real-time reorder recommendations.
Instead of looking at simple averages, the system uses a Random Forest Regressor. This machine learning model analyzes historical "Lags" (what happened yesterday and last week) to understand the underlying patterns of customer behavior.
(e.g., Saturday sales being 3x higher than Tuesday).
Predictions alone aren't enough—we must account for uncertainty. The system uses the Normal Distribution to calculate a statistical "Safety Stock" buffer.
The Reorder Point (ROP): The system calculates the exact moment a purchase order should be triggered to ensure that new stock arrives just before the current stock hits zero.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Forecasting:** Scikit-Learn (Random Forest)
- **Inventory Logic:** Scipy (Normal Distribution for Safety Stock)
- **Dashboard:** Streamlit
- **Data Handling:** Pandas, NumPy

## 🧠 Business Logic & Formulae
The system calculates the **Reorder Point (ROP)** using the formula:
$$ROP = (d \times L) + SS$$
Where:
- $d$: Predicted Daily Demand
- $L$: Lead Time (Days)
- $SS$: Safety Stock ($Z \times \sigma \times \sqrt{L}$)

## 📂 Folder Structure
```text
Retail-Inventory-Optimizer/
├── data/               # Synthetic Retail Datasets
├── src/                # Core Logic (Inventory/Forecast)
├── app.py              # Streamlit Interactive Dashboard
├── requirements.txt    # Project Dependencies
└── README.md           # Documentation
