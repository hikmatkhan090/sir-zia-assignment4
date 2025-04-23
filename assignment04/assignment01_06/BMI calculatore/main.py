import streamlit as st

# Configure page
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        color: #2e8b57;
    }
    .result-box {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 20px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.title("🚀 Smart BMI Calculator by Hikmat khan")
st.markdown("---")

# Weight units selection
unit = st.radio("Select Measurement System:", 
               ["Metric (kg & meters)", "Imperial (lbs & inches)"],
               horizontal=True)

# Input fields
with st.form("bmi_form"):
    if "Metric" in unit:
        weight = st.number_input("Enter Weight (kg)", min_value=1.0, max_value=300.0)
        height = st.number_input("Enter Height (meters)", min_value=0.5, max_value=3.0)
    else:
        weight = st.number_input("Enter Weight (lbs)", min_value=1.0, max_value=660.0)
        col1, col2 = st.columns(2)
        with col1:
            feet = st.number_input("Feet", min_value=1, max_value=8)
        with col2:
            inches = st.number_input("Inches", min_value=0, max_value=11)
        height = feet * 12 + inches  # Convert to total inches

    submitted = st.form_submit_button("Calculate BMI")

# BMI Calculation
if submitted:
    try:
        if "Metric" in unit:
            bmi = weight / (height ** 2)
        else:
            bmi = (weight * 703) / (height ** 2)
        
        bmi_category = ""
        color = ""
        if bmi < 18.5:
            bmi_category = "Underweight 🏋️"
            color = "#3498db"
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal Weight ✅"
            color = "#2ecc71"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight ⚠️"
            color = "#f1c40f"
        else:
            bmi_category = "Obese ❌"
            color = "#e74c3c"

        # Display results
        st.markdown("---")
        st.markdown(f"<div class='result-box' style='border-color: {color};'>"
                    f"<h3 style='color: {color};'>Your BMI: {bmi:.1f}</h3>"
                    f"<p class='big-font'>{bmi_category}</p></div>", 
                    unsafe_allow_html=True)
        
    except ZeroDivisionError:
        st.error("Please enter valid height greater than zero")

# BMI Classification Chart
with st.expander("📊 BMI Classification Chart"):
    st.markdown("""
    | BMI Range       | Category        |
    |----------------|-----------------|
    | Below 18.5      | Underweight     |
    | 18.5 - 24.9     | Normal Weight   |
    | 25.0 - 29.9     | Overweight      |
    | 30.0 and above  | Obese           |
    """)

# Health Tips
st.markdown("---")
st.subheader("💡 Health Tips")
st.write("""
- Maintain balanced diet
- Exercise regularly (150 mins/week)
- Get enough sleep (7-9 hours)
- Stay hydrated (2-3 liters/day)
- Monitor your weight regularly
""")

# Disclaimer
st.markdown("---")
st.caption("ℹ️ Note: BMI is a simple screening tool and does not account for muscle mass or body composition.")

