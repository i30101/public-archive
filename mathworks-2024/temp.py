import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import itertools
import matplotlib.pyplot as plt
import joblib

# Convert the data to a pandas DataFrame
df = pd.read_csv("./data/seattle-time.csv")

# Set 'Time' as the index
df.set_index('Time', inplace=True)

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

variables = df.columns.values.tolist()
# print(variables)
# for v in variables:
#     generate_ARMIA(v)

# Example usage of prediction
future_steps = 50  # Number of steps to predict into the future
for v in variables:
    predictions = predict_with_saved_model(v, future_steps)
    print(f"{v} Predictions:")
    print(predictions)
