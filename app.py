import streamlit as st
import joblib
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Housing Price Predictor",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Custom CSS Styling
# ----------------------------
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .title-text {
            font-size: 42px;
            font-weight: 800;
            text-align: center;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0px;
        }
        .subtitle-text {
            text-align: center;
            color: #9ca3af;
            font-size: 16px;
            margin-bottom: 30px;
        }
        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #38bdf8, #6366f1);
            color: white;
            font-weight: 700;
            font-size: 18px;
            padding: 12px 0px;
            border-radius: 10px;
            border: none;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.6);
        }
        .result-box {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            border: 1px solid #334155;
            margin-top: 20px;
        }
        .price-text {
            font-size: 36px;
            font-weight: 800;
            color: #4ade80;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown('<p class="title-text">🏠 Housing Price Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">AI-powered house price estimation using Machine Learning</p>', unsafe_allow_html=True)
st.divider()

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load("my_housing_model.pkl")
    except FileNotFoundError:
        st.error("⚠️ Model file 'my_housing_model.pkl' not found. Please place it in the app directory.")
        st.stop()

model = load_model()

# ----------------------------
# Sidebar Info
# ----------------------------
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        "This app predicts house prices based on key property features "
        "using a trained regression model (Scikit-learn)."
    )
    st.markdown("---")
    st.subheader("📊 Features Used")
    st.write("""
    - Area (sq. ft)
    - Bedrooms & Bathrooms
    - Stories
    - Parking Spaces
    - Main Road Access
    - Guest Room / Basement
    - Air Conditioning
    - Preferred Area
    - Furnishing Status
    """)
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit & Scikit-learn")

# ----------------------------
# Input Section
# ----------------------------
st.subheader("📋 Enter Property Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq. ft)", min_value=0, value=5000, step=50)
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=3, step=1)
    bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, value=2, step=1)
    stories = st.number_input("Stories", min_value=0, max_value=10, value=2, step=1)
    parking = st.number_input("Parking Spaces", min_value=0, max_value=10, value=1, step=1)

with col2:
    mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
    guestroom = st.selectbox("Guest Room", ["Yes", "No"])
    basement = st.selectbox("Basement", ["Yes", "No"])
    airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
    prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

# ----------------------------
# Encoding helper
# ----------------------------
def yes_no(val):
    return 1 if val == "Yes" else 0

furnishing_map = {"Furnished": 0, "Semi-Furnished": 1, "Unfurnished": 2}

st.divider()

# ----------------------------
# Prediction
# ----------------------------
if st.button("🔍 Predict Price"):
    features = [[
        area, bedrooms, bathrooms, stories,
        yes_no(mainroad), yes_no(guestroom), yes_no(basement),
        yes_no(airconditioning), parking, yes_no(prefarea),
        furnishing_map[furnishingstatus]
    ]]

    with st.spinner("Calculating best estimate..."):
        result = model.predict(features)

    predicted_price = result[0]

    st.markdown(f"""
        <div class="result-box">
            <p style="color:#94a3b8; font-size:16px;">Estimated Property Value</p>
            <p class="price-text">₹ {predicted_price:,.0f}</p>
        </div>
    """, unsafe_allow_html=True)

    st.balloons()

# ----------------------------
# About Developer — Premium Card
# ----------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <style>
        .dev-card {
            position: relative;
            background: linear-gradient(135deg, #1e1b4b, #0f172a 60%, #1e1b4b);
            border-radius: 20px;
            padding: 2px;
            margin-top: 10px;
        }
        .dev-card-inner {
            background: radial-gradient(circle at top left, #1e293b, #0b1120 70%);
            border-radius: 18px;
            padding: 28px 25px;
            text-align: center;
        }
        .dev-avatar {
            width: 64px;
            height: 64px;
            margin: 0 auto 14px auto;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 22px;
            color: white;
            background: linear-gradient(135deg, #38bdf8, #a855f7);
            box-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
        }
        .dev-name {
            font-size: 20px;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 2px;
        }
        .dev-role {
            font-size: 13px;
            color: #94a3b8;
            margin-bottom: 18px;
            letter-spacing: 0.5px;
        }
        .dev-links {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }
        .dev-btn {
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            padding: 9px 18px;
            border-radius: 30px;
            transition: 0.25s;
            display: inline-block;
        }
        .dev-btn-portfolio {
            background: linear-gradient(90deg, #38bdf8, #6366f1);
            color: white;
        }
        .dev-btn-portfolio:hover {
            box-shadow: 0 0 14px rgba(99, 102, 241, 0.7);
            transform: translateY(-2px);
        }
        .dev-btn-linkedin {
            background: rgba(10, 102, 194, 0.15);
            color: #38bdf8;
            border: 1px solid #0a66c2;
        }
        .dev-btn-linkedin:hover {
            background: #0a66c2;
            color: white;
            transform: translateY(-2px);
        }
        .dev-btn-github {
            background: rgba(148, 163, 184, 0.1);
            color: #e2e8f0;
            border: 1px solid #475569;
        }
        .dev-btn-github:hover {
            background: #334155;
            transform: translateY(-2px);
        }
    </style>

    <div class="dev-card">
        <div class="dev-card-inner">
            <div class="dev-avatar">RV</div>
            <div class="dev-name">Raunak Verma</div>
            <div class="dev-role">AI ENTHUSIAST | ASPIRING DATA SCIENTIST</div>
            <div class="dev-links">
                <a class="dev-btn dev-btn-portfolio" href="https://raunakverma.vercel.app" target="_blank">🔗 Know More About Me</a>
                <a class="dev-btn dev-btn-linkedin" href="https://www.linkedin.com/in/raunakverma07" target="_blank">💼 LinkedIn</a>
                <a class="dev-btn dev-btn-github" href="https://github.com/raunakverma07/housing-predictor" target="_blank">💻 GitHub</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("⚠️ Predictions are model-based estimates and may not reflect actual market prices.")
