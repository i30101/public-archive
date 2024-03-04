import pandas as pd
import joblib

# Load the trained model from the file
rf_model = joblib.load('./models/seattle-predict.joblib')

# Define new data
new_data = {
    'ATHPI': [205.5],
    'Basic Utilities Bill': [180],
    'Rent Per Month': [1200],
    'Unemployment': [8.5],
    'Healthcare cost': [365],
    'Total crime': [36000]
}

new_df = pd.DataFrame(new_data)

# Make predictions on new data
new_predictions = rf_model.predict(new_df)
print(f"Predicted Homelessness: {new_predictions}")
