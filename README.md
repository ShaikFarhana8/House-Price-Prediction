# 🏠 House Price Prediction Dashboard

An AI-powered real estate analytics dashboard developed using Machine Learning, XGBoost, Streamlit, and Plotly.  
This project predicts house prices based on property features and provides interactive visual analytics for real estate insights.

---

# 📌 Project Overview

The main goal of this project is to predict house prices using the KC House Price dataset and visualize important market trends through an interactive dashboard.

The application allows users to:
- Predict house prices instantly
- Analyze property trends
- Compare actual vs predicted prices
- Explore dataset analytics
- Understand important pricing features
- View future market growth trends

---

# 🚀 Features

## ✅ House Price Prediction
Predicts house prices using:
- Bedrooms
- Bathrooms
- Sqft Living
- Sqft Lot
- Floors
- Waterfront
- View
- Condition
- Grade
- Basement Area
- Latitude & Longitude
- Living15 & Lot15
- House Age
- Renovation Status

---

## 📊 Interactive Dashboard
Professional dashboard with:
- KPI Cards
- Price Forecast Graphs
- Analytics Charts
- Real Estate Trends
- Feature Importance Visualizations

---

## 📈 Actual vs Predicted Graph
Compares:
- Actual house prices
- Model predicted prices

Helps evaluate model performance visually.

---

## 🔥 Feature Importance Analysis
Shows which features impact house prices the most:
- Square Footage
- Grade
- Bathrooms
- Location
- View
- Waterfront

---

## 📂 Dataset Explorer
Upload and analyze KC House dataset directly inside the dashboard.

Includes:
- Filters
- Scatter plots
- Bar charts
- Trend analysis

---

## 📜 Prediction History
Stores prediction history automatically for future analysis.

---

# 🧠 Machine Learning Models Used

The following regression models were implemented and evaluated:

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

XGBoost was selected as the final deployed model because it provided the best accuracy and performance.

---

# 📉 Overfitting Analysis

Training score and testing score were compared to check overfitting.

Evaluation metrics used:
- R² Score
- MAE
- RMSE

The final model achieved strong generalization performance with minimal overfitting.

---

# 🛠 Technologies Used

## Programming Language
- Python

## Libraries
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- XGBoost

---

# 📦 Dataset

Dataset Used:
- KC House Price Dataset

Contains:
- Property details
- Location information
- House features
- Historical sale prices

---

# ▶️ Run the Project

## Install Dependencies

```bash
pip install -r requirements.txt
