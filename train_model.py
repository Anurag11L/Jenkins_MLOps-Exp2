import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('data/housing.csv')

# Prepare data
X = data[['square_feet']]
y = data['price']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model training completed.")
