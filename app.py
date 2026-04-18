import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

st.title("📦 Retail Sales & Inventory Optimizer")

# Generate Synthetic Data on the fly if CSV missing
date_rng = pd.date_range(start='2024-01-01', end='2025-12-31', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['qty_sold'] = 20 + (df['date'].dt.dayofweek * 5) + np.random.randint(-5, 5, size=len(df))
df['lag_1'] = df['qty_sold'].shift(1)
df = df.dropna()

# Model
X = df[['lag_1']]
y = df['qty_sold']
model = RandomForestRegressor().fit(X, y)

# Sidebar
lt = st.sidebar.slider("Lead Time (Days)", 1, 14, 7)
prediction = model.predict(X.tail(1))[0]

# Inventory Logic
rop = (prediction * lt) + (1.64 * 5 * np.sqrt(lt)) # Simple ROP formula

st.metric("Predicted Sales", f"{int(prediction)} units")
st.metric("Reorder Point", f"{int(rop)} units")
st.line_chart(df.tail(30).set_index('date')['qty_sold'])