import streamlit as st

from hpp import predict_rent


def main():
    st.set_page_config(page_title="House Rent Predictor", page_icon="🏠", layout="centered")

    st.markdown(
        """
        <style>
        :root {
            --bg-start: #07111f;
            --bg-end: #1d4ed8;
            --accent: #ff7a00;
            --accent-2: #ff4d6d;
            --panel: rgba(255, 255, 255, 0.12);
            --panel-strong: rgba(255, 255, 255, 0.18);
            --text: #f8fafc;
        }

        .stApp {
            background: linear-gradient(135deg, var(--bg-start), var(--bg-end));
        }

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }

        .hero-card {
            padding: 1.35rem 1.5rem;
            border-radius: 24px;
            background: linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0.08));
            border: 1px solid rgba(255,255,255,0.18);
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.18);
            margin-bottom: 1rem;
        }

        .hero-card h1 {
            color: var(--text);
            font-size: 2rem;
            margin-bottom: 0.25rem;
        }

        .hero-card p {
            color: #e2e8f0;
            font-size: 1rem;
            margin-bottom: 0;
        }

        .info-card {
            padding: 1rem 1.1rem;
            border-radius: 18px;
            background: var(--panel);
            border: 1px solid rgba(255,255,255,0.14);
            margin-top: 0.5rem;
        }

        .info-card strong {
            color: #fff;
        }

        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div {
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.95);
            color: #0f172a;
        }

        .stButton > button {
            background: linear-gradient(135deg, var(--accent), var(--accent-2));
            color: white;
            border: 0;
            border-radius: 999px;
            padding: 0.65rem 1.4rem;
            font-weight: 700;
            box-shadow: 0 8px 24px rgba(255,77,109,0.25);
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 10px 28px rgba(255,77,109,0.35);
        }

        .result-card {
            padding: 1.2rem 1.25rem;
            border-radius: 18px;
            background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
            border: 1px solid rgba(255,255,255,0.22);
            margin-top: 0.75rem;
            text-align: center;
        }

        .result-card h3 {
            color: white;
            margin-bottom: 0.3rem;
        }

        .result-card p {
            color: #fef3c7;
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-card">
            <h1>🏠 House Rent Predictor</h1>
            <p>Estimate your monthly rent in seconds with a clean, fast, and modern experience.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns([1.6, 0.9], gap="large")

    with left_col:
        with st.form("rent_form"):
            st.markdown("<div class='info-card'><strong>Enter property details</strong></div>", unsafe_allow_html=True)

            col1, col2 = st.columns(2, gap="large")
            with col1:
                bhk = st.number_input("BHK", min_value=1, max_value=6, value=2)
                size = st.number_input("Size (sq ft)", min_value=300, max_value=5000, value=1200, step=50)
                floor = st.text_input("Floor", value="1 out of 3")
                area_type = st.selectbox("Area Type", ["Super Area", "Carpet Area", "Built Area"])
                area_locality = st.text_input("Area Locality", value="Bandel")

            with col2:
                city = st.selectbox("City", ["Kolkata", "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Pune"])
                furnishing_status = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])
                tenant_preferred = st.selectbox("Tenant Preferred", ["Bachelors/Family", "Bachelors", "Family", "Any"])
                bathroom = st.number_input("Bathroom", min_value=1, max_value=4, value=2)
                point_of_contact = st.selectbox("Point of Contact", ["Contact Owner", "Contact Agent"])

            submitted = st.form_submit_button("Predict Rent")
            if submitted:
                input_data = {
                    "BHK": int(bhk),
                    "Size": int(size),
                    "Floor": floor,
                    "Area Type": area_type,
                    "Area Locality": area_locality,
                    "City": city,
                    "Furnishing Status": furnishing_status,
                    "Tenant Preferred": tenant_preferred,
                    "Bathroom": int(bathroom),
                    "Point of Contact": point_of_contact,
                }
                prediction = predict_rent(input_data)
                st.markdown(
                    f"""
                    <div class="result-card">
                        <h3>Estimated Rent</h3>
                        <p>₹{prediction:,.2f} / month</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    with right_col:
        st.markdown(
            """
            <div class="info-card">
                <strong>Why it looks great</strong><br>
                • Faster, cleaner input flow<br>
                • Modern colors and glassy cards<br>
                • More comfortable for mobile and desktop
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="info-card">
                <strong>Tip</strong><br>
                Try different cities and furnishing options to compare estimates instantly.
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()