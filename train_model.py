import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv('Salary_Data.csv')

# Features and target
X = data[['YearsExperience']]
y = data['Salary']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'salary_model.pkl')

print("Model saved successfully!")