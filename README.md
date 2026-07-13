# Enterprise Asset Intelligence Platform

A live, interactive end-to-end data analytics and predictive machine learning pipeline designed to optimize industrial fleet operations, minimize unscheduled equipment downtime, and support strategic decision-making in capital-intensive corporate environments.

**[Live Web Application Link](YOUR_STREAMLIT_CLOUD_URL_HERE)** *(Replace this text with your live Streamlit URL!)*

## Executive Summary & Business Case

In asset-heavy industries, unscheduled equipment failure results in millions of dollars in lost production, inflated labor costs, and operational friction. This platform transitions organizations from high-cost **reactive maintenance** to predictive, resource-optimized **preventative scheduling**.

By leveraging predictive AI pipelines and real-time telemetry analysis, this project addresses the core corporate goals outlined in strategic consulting operations:
* **Cost Reduction:** Identifies degrading components before catastrophic failure to decrease replacement costs.
* **Operational Continuity:** Translates high-volume IoT sensor outputs into clear, functional actionable insights for floor managers.
* **To-Be Transformation:** Maps a structured data journey from unmonitored infrastructure risk to data-driven proactive asset intelligence.

## Project Architecture & Workflow

The platform follows a rigorous three-phase data lifecycle engineered entirely from scratch:

1. **Exploratory Data Analysis (EDA):** Ingests and cleans 120,000+ rows of historical multi-sensor telemetry logs. Generates statistical feature correlation matrices to establish dynamic dependencies between operating variables.
2. **Predictive Modeling (XGBoost):** Implements an advanced gradient-boosted decision tree architecture (`XGBClassifier`) to capture complex, non-linear degradation signatures and calculate the exact probability of imminent asset failure.
3. **Interactive Business Intelligence (Streamlit Cloud):** Deploys a live interactive executive dashboard, abstracting dense code into structured metric counters, failure breakdowns, and root-cause analytics.

## Strategic Insights (Key Technical Discoveries)

* **Root-Cause Isolation:** Using algorithmic feature importance extraction (`plot_importance`), the project successfully isolated **Metric 1** and **Metric 6** as the primary statistical drivers of equipment failure, accounting for over **60% of the overall model weight**.
* **Operational Strategy:** Instead of standard, low-efficiency inspections across all 9 metrics equally, corporate maintenance schedules can be optimized to focus exclusively on telemetric anomalies in Metrics 1 & 6—maximizing resource productivity.

## Tech Stack & Tooling

* **Language:** Python 3.x
* **Data Engineering & Analysis:** Pandas, NumPy
* **Data Visualization & Analytics:** Matplotlib, Seaborn
* **Machine Learning Pipeline:** Scikit-Learn, XGBoost
* **Application Framework & Deployment:** Streamlit, GitHub, Streamlit Community Cloud

## Local Installation & Setup

To run this platform locally on your machine, follow these steps using your terminal or PowerShell:

1. Clone this repository to your computer:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/Enterprise-Asset-Intelligence-Platform.git](https://github.com/YOUR_GITHUB_USERNAME/Enterprise-Asset-Intelligence-Platform.git)
   cd Enterprise-Asset-Intelligence-Platform
