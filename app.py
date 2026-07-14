import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Predictive Maintenance Dashboard", layout="wide")
st.title("🛠️ Enterprise Predictive Maintenance Dashboard")
st.write("A Strategy & Consulting analytics pipeline optimizing fleet operations using XGBoost.")

# 2. LOAD DATA
@st.cache_data # Cleans up performance so the app loads fast
def load_data():
    df = pd.read_csv("predictive_maintenance_dataset.csv")
    numeric_df = df.select_dtypes(include=[np.number])
    return df, numeric_df

df, numeric_df = load_data()

# 3. SIDEBAR NAVIGATION
st.sidebar.markdown(
    "[🐙 View Source Code on GitHub](https://github.com/kratimandovra/Enterprise-Asset-Intelligence-Platform)"
)

page = st.sidebar.selectbox(
    "Navigate Project",
    ["Executive Summary & EDA", "AI Model & Strategic Insights"]
)


if page == "Executive Summary & EDA":
    st.subheader("📊 Operational Fleet Overview (Current State)")
    
    # Simple Metrics Cards
    col1, col2 = st.columns(2)
    col1.metric("Total Devices Monitored", len(df))
    col2.metric("Total Observed Failures", int(df['failure'].sum()))
    
    # Correlation Matrix Plot
    st.write("### Sensor Correlation Analysis")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

elif page == "AI Model & Strategic Insights":
    st.subheader("🤖 XGBoost Failure Prediction & To-Be Strategy")
    
    # Train Model
    X = numeric_df.drop(columns=['failure']) 
    y = numeric_df['failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    
    # Plot Feature Importance
    st.write("### Root-Cause Factor Identification")
    fig, ax = plt.subplots(figsize=(8, 4))
    xgb.plot_importance(model, ax=ax)
    st.pyplot(fig)
    
    st.success("💡 **Consulting Takeaway:** Focus preventive maintenance schedules tightly around Metric 1 and Metric 6 to minimize operational costs.")
