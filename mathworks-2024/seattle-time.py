import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import itertools
import matplotlib.pyplot as plt
import joblib
import random
import warnings

# Convert the data to a pandas DataFrame
df = pd.read_csv("./data/seattle-time.csv")

# Set 'Time' as the index
df.set_index('Time', inplace=True)

# Suppress FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=ValueError)

# Function to add a row with NaN values for the year if it doesn't exist
def add_row_for_year(year):
    if year not in df.index:
        df.loc[year] = np.nan

# Define a function to calculate RMSE for given p, d, and q values
def evaluate_arima_model(order, data):
    model = ARIMA(data, order=order)
    results = model.fit()
    rmse = np.sqrt(mean_squared_error(data, results.fittedvalues))
    return rmse, results  # Return both RMSE and model results

def generate_ARMIA(variable: str):
    # Perform a grid search for p, d, and q values
    p_values = range(0, 3)
    d_values = range(1, 3)
    q_values = range(0, 3)

    best_rmse = float('inf')
    best_order = None
    best_model = None  # Store the best model

    for p, d, q in itertools.product(p_values, d_values, q_values):
        order = (p, d, q)
        try:
            rmse, model_results = evaluate_arima_model(order, df[variable])
            if rmse < best_rmse:
                best_rmse = rmse
                best_order = order
                best_model = model_results
        except Exception as e:
            continue

    # Save the best model using joblib
    joblib.dump(best_model, f"{variable}_arima_model.joblib")

    # Print the best order and corresponding RMSE
    print(f"Best {variable} Order: {best_order}")
    print(f"Best RMSE: {best_rmse}")

    # Plotting the fitted values with the best model
    plt.figure(figsize=(10, 6))
    plt.plot(df[variable], label='Original Data')
    plt.plot(best_model.fittedvalues, color='red', label='Fitted Values (Best Model)')
    plt.title(f'{variable} Model Fitted Values (Best Model)')
    plt.legend()
    plt.show()

# Function to load the saved model and make predictions
def predict_with_saved_model(variable: str, future_steps: int):
    model = joblib.load(f"{variable}_arima_model.joblib")
    forecast = model.get_forecast(steps=future_steps)
    return forecast.predicted_mean

# New function to predict for a specific year
def predict_for_year(variable: str, year: int):
    add_row_for_year(year)  # Add the year to the index if it doesn't exist
    # Assuming that the year is one of the observed years in the data
    observed_data = df.loc[year, variable]
    
    # Load the saved model
    model = joblib.load(f"{variable}_arima_model.joblib")
    
    # Predict for the specified year
    prediction = model.get_prediction(start=year, end=year)
    
    # Extract the predicted value
    predicted_value = prediction.predicted_mean.values[0]
    
    return observed_data, predicted_value

variables = df.columns.values.tolist()
variables.remove("Homelessness")
print(variables)
# for v in variables:
#     generate_ARMIA(v)

def get_prediction(variable: str, year: int):
    observed_value, predicted_value = predict_for_year(variable, year)
    predicted_value = float(predicted_value) + random.randint(-30, 30)
    print(year, variable, predicted_value)
    return predicted_value

# Load the trained model from the file
rf_model = joblib.load('./models/seattle-predict.joblib')


def homeless_prediction(year):
    # Define new data
    new_data = {}
    for v in variables:
        new_data[v] = [get_prediction(v, year)]
    print(new_data)

    new_df = pd.DataFrame(new_data)

    # Make predictions on new data
    new_predictions = rf_model.predict(new_df)
    # print(f"Predicted Homelessness: {new_predictions}")
    return float(new_predictions)

print(homeless_prediction(2034))
print(homeless_prediction(2054))
print(homeless_prediction(2074))
