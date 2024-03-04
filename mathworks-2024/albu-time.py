import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import pickle
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load CSV file
file_path = './data/albu-time.csv'
df = pd.read_csv(file_path)

# Assuming 'Time' is the index column
df['Time'] = pd.to_datetime(df['Time'])
df.set_index('Time', inplace=True)

# Function to create ARIMA model and return it
def build_arima_model(column_name):
    # Split data into training and testing sets
    train_size = int(len(df[column_name]) * 0.8)
    train, test = df[column_name][:train_size], df[column_name][train_size:]

    # Build ARIMA model
    model = ARIMA(train, order=(5, 1, 0))  # You can adjust the order based on your data
    fitted_model = model.fit()

    # Save the model using pickle
    model_filename = f'{column_name}_arima_model.pkl'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(fitted_model, model_file)

    return fitted_model, test

# Apply the function for each column (excluding 'Homelessness')
columns_to_predict = ['ATHPI', 'Basic Utilities Bill', 'Rent Per Month', 'Unemployment', 'Healthcare cost', 'Total crime']

# Dictionary to store ARIMA models and corresponding test sets
arima_models = {}

for column in tqdm(columns_to_predict, desc="Building ARIMA Models"):
    model, test_data = build_arima_model(column)
    arima_models[column] = {'model': model, 'test_data': test_data}

# Function to predict for a specific year and calculate accuracy
def predict_and_evaluate_for_month(model, year, month):
    start_time = pd.Timestamp(f'{year}-{month:02d}-01')
    end_time = pd.Timestamp(f'{year}-{month:02d}-{pd.Timestamp(year, month + 1, 1) - pd.Timedelta(days=1):%d}')

    predictions = model.predict(start=start_time, end=end_time, typ='levels')
    
    return predictions

# Evaluate and output accuracy for each predictor for each month
for column, model_info in tqdm(arima_models.items(), desc="Predicting and Evaluating"):
    model = model_info['model']
    test_data = model_info['test_data']
    
    year_to_predict = 2022  # Change this to the desired year
    
    all_predictions = pd.Series()

    for month_to_predict in range(1, 13):
        predictions = predict_and_evaluate_for_month(model, year_to_predict, month_to_predict)
        test_data_month = test_data[test_data.index.month == month_to_predict]
        
        # Concatenate predictions
        all_predictions = pd.concat([all_predictions, predictions])

        # Evaluate accuracy
        mae = mean_absolute_error(test_data_month, predictions)
        mse = mean_squared_error(test_data_month, predictions)
        rmse = np.sqrt(mse)

        print(f'\nAccuracy for {column} in {year_to_predict}-{month_to_predict:02d}:')
        print(f'Mean Absolute Error (MAE): {mae}')
        print(f'Mean Squared Error (MSE): {mse}')
        print(f'Root Mean Squared Error (RMSE): {rmse}')

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.plot(test_data_month.index, test_data_month, label='Actual Data')
        plt.plot(predictions.index, predictions, label='Predictions')
        plt.title(f'ARIMA Model for {column} in {year_to_predict}-{month_to_predict:02d}')
        plt.xlabel('Time')
        plt.ylabel(column)
        plt.legend()
        plt.show()

    # Plot overall results
    plt.figure(figsize=(10, 6))
    plt.plot(test_data.index, test_data, label='Actual Data')
    plt.plot(all_predictions.index, all_predictions, label='Predictions')
    plt.title(f'ARIMA Model for {column} in {year_to_predict}')
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.legend()
    plt.show()
