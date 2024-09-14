from models import load_model, predict_kidney_stones

# Load the trained model
model = load_model('models/kidney_stone_model.pkl')

# Prepare sample input data
# Example input: [gravity, ph, osmo, cond, urea, calc]
sample_input = [1.021, 4.91, 725, 14.0, 443, 2.45]

# Make a prediction
prediction = predict_kidney_stones(model, sample_input)
print("Prediction:", prediction)