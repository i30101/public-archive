# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import numpy as np



# Create a DataFrame
df = pd.read_csv("./data/albu-homeless-prediction.csv")

# Split the data into features (X) and target variable (y)
X = df.drop('Homelessness', axis=1)
y = df['Homelessness']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model to the training data
rf_model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(rf_model, './models/seattle-predict.joblib')

# Make predictions on the test set
predictions = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Now you can use the model to make predictions on new data
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
