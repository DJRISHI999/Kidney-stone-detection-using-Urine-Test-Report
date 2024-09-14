import streamlit as st
from models import extract_text_from_pdf, extract_relevant_info, predict_kidney_stones

# Title
st.title("Urine Report Analysis for Kidney Stone Prediction")

# Option to choose input method
input_method = st.radio("Choose input method:", ("Upload PDF", "Manual Input"))

# Manual input for urination pain
urination_painful = st.checkbox("Is urination painful?")

if input_method == "Upload PDF":
    # Upload PDF
    uploaded_file = st.file_uploader("Choose a urine report PDF...", type=["pdf"])

    if uploaded_file is not None:
        st.write("Extracting information from the report...")
        
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)
        
        if text:
            # Extract relevant information
            data = extract_relevant_info(text)
            
            if data:
                # Add manual input to the data
                data['urination_painful'] = urination_painful
                
                # Predict kidney stones
                prediction = predict_kidney_stones(data)
                st.write("Prediction:", prediction)
                st.write("Extracted Data:", data)
            else:
                st.error("Failed to extract relevant information from the report.")
        else:
            st.error("Failed to extract text from the PDF.")
    else:
        st.write("Please upload a urine report PDF.")
else:
    # Manual input form
    st.write("Enter the values for the following indices:")
    color = st.selectbox("Color", ["Pink", "Brown", "Red", "Other"])
    appearance = st.selectbox("Appearance", ["Cloudy", "Clear"])
    rbc_in_urine = st.checkbox("RBC in urine")
    calcium_oxalate_crystal = st.checkbox("Calcium oxalate crystal")
    uric_acid_salt_crystal = st.checkbox("Uric acid salt crystal")
    usg = st.number_input("USG (Urine Specific Gravity)", min_value=0.0, max_value=5.0, step=0.001)

    # Collect data
    data = {
        'color': color,
        'appearance': appearance,
        'rbc_in_urine': rbc_in_urine,
        'calcium_oxalate_crystal': calcium_oxalate_crystal,
        'uric_acid_salt_crystal': uric_acid_salt_crystal,
        'urination_painful': urination_painful,
        'usg': usg
    }

    # Predict kidney stones
    if st.button("Predict"):
        prediction = predict_kidney_stones(data)
        st.write("Prediction:", prediction)
        st.write("Input Data:", data)