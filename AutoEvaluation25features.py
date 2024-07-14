#auto evaluation -- use excel Book25features.csv
import pandas as pd
import joblib
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, accuracy_score

# Load the trained model
model = joblib.load('modelDataInbalance_25features')

# Load the new data
new_data_path = 'Book25features.csv'  # Update with your file path
new_data = pd.read_csv(new_data_path)

# Preprocess the data
new_data = new_data.drop(columns=['id'])


# Split the data into features and target
X_new = new_data.drop('repay_fail', axis=1)
y_new = new_data['repay_fail']

# Make predictions
y_pred_new = model.predict(X_new)

# Evaluate the model
accuracy_new = accuracy_score(y_new, y_pred_new)
classification_report_new = classification_report(y_new, y_pred_new)

print(f"Accuracy on new data: {accuracy_new}")
print(f"Classification Report on new data:\n{classification_report_new}")
