import joblib

# Load the model
def load_model(file_path):
    return joblib.load(file_path)

# Predict function
# Predict function
def predict_kidney_stones(data):
    # Criteria for high risk of kidney stones
    high_risk_criteria = [
        data['rbc_in_urine'],
        data['calcium_oxalate_crystal'],
        data['uric_acid_salt_crystal'],
        data['color'] in ["Pink", "Brown", "Red"],
        data['appearance'] == "Cloudy",
        data['urination_painful'],
        data['usg'] > 1.020  # High risk if USG is greater than 1.020
    ]
    
    # Count the number of criteria met
    high_risk_count = sum(high_risk_criteria)
    
    # Determine risk based on the number of criteria met
    if high_risk_count >= 4:
        return "High risk of kidney stones"
    else:
        return "Low risk of kidney stones"