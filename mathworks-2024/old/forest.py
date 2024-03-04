import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Assuming your data is stored in a DataFrame called 'df'
# Replace 'your_factors' with the actual column names representing the factors influencing homelessness

# Load your data
df = pd.read_csv('alls.csv')
df.fillna(0, inplace=True)

# Extract features (factors) and target variable (homelessness)
X = df.drop('Homelessness', axis=1)  # Drop the target variable to get all factors
y = df['Homelessness']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model to the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Get feature importances
feature_importances = rf_model.feature_importances_
print(feature_importances)
feature_names = X.columns
print(feature_names)

# Visualize feature importances
plt.barh(feature_names, feature_importances)
plt.xlabel('Feature Importance')
plt.ylabel('Features')
plt.title('Random Forest Regression - Feature Importances')
plt.show()
