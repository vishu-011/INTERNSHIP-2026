import streamlit as st

from wine_quality import classify_wine_quality, predict_wine_quality


def main():
    st.set_page_config(page_title="Wine Quality Checker", page_icon="🍷", layout="centered")

    st.markdown(
        """
        <style>
        .stApp { background: linear-gradient(135deg, #2b0a3d, #5b2a86); }
        .block-container { padding-top: 1rem; padding-bottom: 2rem; }
        .hero-card { padding: 1.2rem 1.3rem; border-radius: 20px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2); margin-bottom: 1rem; }
        .hero-card h1 { color: white; font-size: 2rem; margin-bottom: 0.25rem; }
        .hero-card p { color: #f5e8ff; margin-bottom: 0; }
        .info-card { padding: 0.9rem 1rem; border-radius: 16px; background: rgba(255,255,255,0.1); margin-top: 0.5rem; color: white; }
        .stButton > button { border-radius: 999px; background: linear-gradient(135deg, #ff7a59, #ff4d6d); color: white; border: 0; }
        .result-card { padding: 1rem 1.1rem; border-radius: 16px; background: rgba(255,255,255,0.16); margin-top: 0.75rem; text-align: center; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-card">
            <h1>🍷 Wine Quality Checker</h1>
            <p>Estimate wine quality from its chemical properties.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("wine_form"):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            fixed_acidity = st.number_input("Fixed Acidity", value=7.4, format="%.2f")
            volatile_acidity = st.number_input("Volatile Acidity", value=0.70, format="%.2f")
            citric_acid = st.number_input("Citric Acid", value=0.00, format="%.2f")
            residual_sugar = st.number_input("Residual Sugar", value=1.90, format="%.2f")
            chlorides = st.number_input("Chlorides", value=0.076, format="%.3f")
            free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0, format="%.2f")
        with col2:
            total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0, format="%.2f")
            density = st.number_input("Density", value=0.9978, format="%.4f")
            ph = st.number_input("pH", value=3.51, format="%.2f")
            sulphates = st.number_input("Sulphates", value=0.56, format="%.2f")
            alcohol = st.number_input("Alcohol", value=9.4, format="%.2f")

        submitted = st.form_submit_button("Check Wine Quality")
        if submitted:
            wine_input = {
                "fixed acidity": float(fixed_acidity),
                "volatile acidity": float(volatile_acidity),
                "citric acid": float(citric_acid),
                "residual sugar": float(residual_sugar),
                "chlorides": float(chlorides),
                "free sulfur dioxide": float(free_sulfur_dioxide),
                "total sulfur dioxide": float(total_sulfur_dioxide),
                "density": float(density),
                "pH": float(ph),
                "sulphates": float(sulphates),
                "alcohol": float(alcohol),
            }
            score = predict_wine_quality(wine_input)
            label = classify_wine_quality(score)
            st.markdown(
                f"""
                <div class="result-card">
                    <h3>Predicted Quality</h3>
                    <p>{score:.2f} ({label})</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()
