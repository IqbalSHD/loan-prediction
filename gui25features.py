import tkinter as tk
from tkinter import ttk
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('modelDataInbalance_25features')

# Function to make predictions
def predict():
    # Get input values
    inputs = [float(entry.get()) for entry in entries]
    inputs = np.array(inputs).reshape(1, -1)
    # Make prediction
    prediction = model.predict(inputs)
    result.set("Prediction: " + ("Repay Fail" if prediction[0] == 1 else "Repay Success"))

# Create the main window
root = tk.Tk()
root.title("Loan Repayment Prediction")

# Create a frame for the inputs
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# List of feature names
feature_names = [
    "loan_amount", "funded_amount", "funded_amount_investors", "term", "interest_rate", "installment",
    "employment_length", "home_ownership", "annual_income", "verification_status",
    "loan_status", "purpose", "debt_to_income_ratio", "no_delinquency_2yrs",
    "inquiries_last_6mths", "no_open_accounts", "public_records", "revolving_balance",
    "revolving_utillization", "no_total_account", "total_payment",
    "total_payment_investors", "total_received_principal", "total_received_interest",
    "last_payment_amnt"
]

# Create input fields
entries = []
for i, feature in enumerate(feature_names):
    ttk.Label(input_frame, text=feature).grid(row=i, column=0, sticky=tk.W)
    entry = ttk.Entry(input_frame, width=20)
    entry.grid(row=i, column=1, sticky=(tk.W, tk.E))
    entries.append(entry)

# Create a button to make predictions
predict_button = ttk.Button(input_frame, text="Predict", command=predict)
predict_button.grid(row=len(feature_names), column=0, columnspan=2)

# Create a label to display the prediction result
result = tk.StringVar()
ttk.Label(input_frame, textvariable=result, font=("Helvetica", 16)).grid(row=len(feature_names)+1, column=0, columnspan=2)

# Run the application
root.mainloop()
