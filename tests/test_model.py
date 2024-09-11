import pickle
import pandas as pd

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def test_prediction():
    # Create a DataFrame with the same column name as in training
    test_input = pd.DataFrame({'square_feet': [1500]})
    
    # Make prediction
    prediction = model.predict(test_input)
    
    # Assert the prediction
    assert prediction > 0, "The prediction should be a positive value."
    
    # Print the prediction result
    print(f"Predicted house price for 1500 square feet: ${prediction[0]:.2f}")

test_prediction()
print("Test passed.")
