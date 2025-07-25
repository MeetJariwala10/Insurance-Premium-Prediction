import streamlit as st
import requests
from PIL import Image
import base64

st.markdown("# 🛡️ Insurance Premium Prediction")

# --- Sidebar ---
st.sidebar.title("About")
st.sidebar.info(
    """
    This app predicts your insurance premium based on your details.\n
    **Instructions:**\n
    1. Fill in your information.\n    2. Click **Predict**.\n    3. See your estimated premium instantly!\n
    _Built with Streamlit_
    """
)

# --- Main Form Layout ---
st.markdown("---")
st.markdown("### Enter your details:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 Age", min_value=0, max_value=120, value=30)
    height = st.number_input("📏 Height (meters)", min_value=0.0, max_value=2.5, value=1.5)
    city = st.text_input("🏙️ City", value="surat")
with col2:
    weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, max_value=200.0, value=65.0)
    income_lpa = st.number_input("💰 Income (LPA)", min_value=0.0, value=150000.0)
    occupation = st.text_input("💼 Occupation", value="retired")

smoker = st.checkbox("🚬 Smoker", value=False)

st.markdown("---")

if st.button("🔮 Predict My Premium"):
    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        if response.status_code == 200:
            result = response.json()
            # Extract values
            res = result.get('response', result)
            category = res.get('predicted_category', 'N/A')
            confidence = res.get('confidence', 0)
            class_probs = res.get('class_probabilities', {})
            # Display nicely
            st.markdown(f"## 🎉 **Predicted Category:** <span style='color:green;font-size:32px;'>{category}</span>", unsafe_allow_html=True)
            st.markdown(f"**Confidence:** {confidence*100:.1f}%")
            if class_probs:
                st.markdown("**Class Probabilities:**")
                st.table({k: [f"{v*100:.1f}%"] for k, v in class_probs.items()})
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to API: {e}")      