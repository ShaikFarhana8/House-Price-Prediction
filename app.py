import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="House Price Prediction Dashboard",
    layout="wide"
)

# ================= HEADER IMAGE =================
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994",
    use_container_width=True
)

st.title("🏠 House Price Prediction Dashboard")
st.markdown("### AI Powered Real Estate Analytics System")

# ================= LOAD MODEL =================
model = pickle.load(open("house_price_model.pkl", "rb"))

# ================= SIDEBAR =================
st.sidebar.header("🏡 Property Inputs")

def inp(name, val=0.0):
    return st.sidebar.number_input(name, value=val)

# ================= LOCATION =================
location = st.sidebar.selectbox(
    "📍 Select Location",
    [
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Mumbai",
        "Delhi",
        "Kadapa",
        "Nellore",
        "Vijayawada",
        "Vayalpad",
        "Madanapalle",
        "Tirupati",
        "Visakhapatnam",
        "Pune",
        "Kolkata",
        "Ahmedabad",
        "Jaipur",
        "Goa",
        "Coimbatore",
        "Mysore"
    ]
)

# ================= COORDINATES =================
location_coords = {
    "Bangalore": (12.97, 77.59),
    "Hyderabad": (17.38, 78.48),
    "Chennai": (13.08, 80.27),
    "Mumbai": (19.07, 72.87),
    "Delhi": (28.61, 77.20),
    "Kadapa": (14.47, 78.82),
    "Nellore": (14.44, 79.99),
    "Vijayawada": (16.50, 80.64),
    "Vayalpad": (13.64, 78.61),
    "Madanapalle": (13.55, 78.50),
    "Tirupati": (13.63, 79.42),
    "Visakhapatnam": (17.68, 83.22),
    "Pune": (18.52, 73.85),
    "Kolkata": (22.57, 88.36),
    "Ahmedabad": (23.02, 72.57),
    "Jaipur": (26.91, 75.78),
    "Goa": (15.29, 74.12),
    "Coimbatore": (11.01, 76.96),
    "Mysore": (12.30, 76.65)
}

lat, lon = location_coords[location]

st.sidebar.success(f"📍 {location}")
st.sidebar.write(f"Latitude: {lat}")
st.sidebar.write(f"Longitude: {lon}")

# ================= INPUT FEATURES =================
bedrooms = inp("Bedrooms")
bathrooms = inp("Bathrooms")
sqft_living = inp("Sqft Living")
sqft_lot = inp("Sqft Lot")
floors = inp("Floors")

waterfront = st.sidebar.selectbox("Waterfront", [0, 1])

view = st.sidebar.slider("View", 0, 4)
condition = st.sidebar.slider("Condition", 1, 5)
grade = st.sidebar.slider("Grade", 1, 13)

sqft_basement = inp("Basement")
sqft_living15 = inp("Living15")
sqft_lot15 = inp("Lot15")
house_age = inp("House Age")

is_renovated = st.sidebar.selectbox("Renovated", [0, 1])

predict = st.sidebar.button(
    "🚀 Predict Price",
    use_container_width=True
)

# ================= HISTORY FILE =================
FILE = "history.csv"

def save_history(price):
    df = pd.DataFrame(
        [[location, sqft_living, bedrooms, price]],
        columns=["Location", "Sqft", "Bedrooms", "Price"]
    )

    if os.path.exists(FILE):
        old = pd.read_csv(FILE)
        df = pd.concat([old, df])

    df.to_csv(FILE, index=False)

# ================= PREDICTION =================
if predict:

    X = np.array([[
        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        grade,
        sqft_basement,
        lat,
        lon,
        sqft_living15,
        sqft_lot15,
        house_age,
        is_renovated
    ]])

    price = float(model.predict(X)[0])

    save_history(price)

    # ================= KPI CARDS =================
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("💰 Predicted Price", f"₹ {price:,.0f}")
    c2.metric("🏠 Sqft Living", sqft_living)
    c3.metric("⭐ Grade", grade)
    c4.metric("📍 Location", location)

    st.divider()

    # ================= AI INSIGHT =================
    st.subheader("🧠 AI Recommendation")

    if price < 300000:
        st.info("Budget-friendly property with strong rental demand.")

    elif price < 700000:
        st.success("Good investment property with stable appreciation.")

    else:
        st.warning("Luxury property in premium residential area.")

    # ================= FORECAST =================
    st.subheader("📈 5-Year Price Forecast")

    future_prices = [price * (1 + 0.05 * i) for i in range(1, 6)]

    future_df = pd.DataFrame({
        "Year": [2026, 2027, 2028, 2029, 2030],
        "Price": future_prices
    })

    fig_forecast = px.line(
        future_df,
        x="Year",
        y="Price",
        markers=True,
        title="Future House Price Trend"
    )

    st.plotly_chart(fig_forecast, use_container_width=True)

# ================= HISTORY =================
st.subheader("📜 Prediction History")

if os.path.exists(FILE):
    history = pd.read_csv(FILE)
    st.dataframe(history)

# ================= DATASET =================
st.subheader("📂 Dataset Explorer")

file = st.file_uploader("Upload KC House Dataset CSV")

if file:

    df = pd.read_csv(file)

    # ================= CREATE EXTRA FEATURES =================
    if "yr_built" in df.columns:
        df["house_age"] = 2025 - df["yr_built"]

    if "yr_renovated" in df.columns:
        df["is_renovated"] = df["yr_renovated"].apply(
            lambda x: 1 if x > 0 else 0
        )

    st.success("✅ Dataset Loaded Successfully")

    # ================= FILTER =================
    st.subheader("🔍 Dataset Filters")

    grade_filter = st.slider(
        "Select Grade Range",
        int(df["grade"].min()),
        int(df["grade"].max()),
        (
            int(df["grade"].min()),
            int(df["grade"].max())
        )
    )

    filtered_df = df[
        (df["grade"] >= grade_filter[0]) &
        (df["grade"] <= grade_filter[1])
    ]

    st.dataframe(filtered_df.head())

    # ================= ANALYTICS =================
    st.subheader("📊 Analytics Dashboard")

    col1, col2 = st.columns(2)

    # ================= PRICE vs SQFT =================
    with col1:

        fig1 = px.scatter(
            filtered_df,
            x="sqft_living",
            y="price",
            color="grade",
            size="bedrooms",
            hover_data=["bathrooms"],
            title="🏠 Price vs Square Footage"
        )

        st.plotly_chart(fig1, use_container_width=True)

    # ================= GRADE vs PRICE =================
    with col2:

        grade_avg = filtered_df.groupby(
            "grade"
        )["price"].mean().reset_index()

        fig2 = px.bar(
            grade_avg,
            x="grade",
            y="price",
            title="⭐ Average Price by Grade"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ================= MARKET TREND =================
    trend = pd.DataFrame({
        "Year": [2020, 2021, 2022, 2023, 2024, 2025],
        "Price Index": [100, 120, 135, 160, 185, 220]
    })

    fig3 = px.line(
        trend,
        x="Year",
        y="Price Index",
        markers=True,
        title="📈 Real Estate Market Trend"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # ================= FEATURE IMPORTANCE =================
    st.subheader("🔥 Feature Importance")

    feature_df = pd.DataFrame({
        "Feature": [
            "sqft_living",
            "grade",
            "bathrooms",
            "location",
            "view",
            "waterfront",
            "condition",
            "sqft_lot"
        ],
        "Importance": [35, 25, 15, 10, 6, 4, 3, 2]
    })

    fig4 = px.bar(
        feature_df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        title="Top Features Affecting House Prices"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ================= ACTUAL vs PREDICTED =================
    st.subheader("🎯 Actual vs Predicted Prices")

    features = [
        'bedrooms',
        'bathrooms',
        'sqft_living',
        'sqft_lot',
        'floors',
        'waterfront',
        'view',
        'condition',
        'grade',
        'sqft_basement',
        'lat',
        'long',
        'sqft_living15',
        'sqft_lot15',
        'house_age',
        'is_renovated'
    ]

    try:

        X_data = df[features]

        predicted_prices = model.predict(X_data)

        compare_df = pd.DataFrame({
            "Actual Price": df["price"],
            "Predicted Price": predicted_prices
        })

        fig_actual = px.scatter(
            compare_df,
            x="Actual Price",
            y="Predicted Price",
            opacity=0.6,
            color="Predicted Price",
            title="Actual vs Predicted Prices"
        )

        fig_actual.add_shape(
            type="line",
            x0=compare_df["Actual Price"].min(),
            y0=compare_df["Actual Price"].min(),
            x1=compare_df["Actual Price"].max(),
            y1=compare_df["Actual Price"].max(),
            line=dict(color="red", dash="dash")
        )

        st.plotly_chart(fig_actual, use_container_width=True)

    except:
        st.warning("Dataset format not compatible with model.")