import pandas as pd
from sklearn.model_selection import train_test_split
import os

df = pd.read_csv("data/curated_flight_data.csv")

# Drop identifiers & passenger fields
df = df.drop(columns=["flight_id", "flight_number", "passenger_id", "passenger_name", "email"])

# Encode categorical features
df = pd.get_dummies(df, columns=["origin", "destination", "weather_condition"], drop_first=True)

# Target column: is_delayed
y = df["is_delayed"]
X = df.drop(columns=["is_delayed"])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Combine features + target
train_df = pd.concat([y_train, X_train], axis=1)
test_df = pd.concat([y_test, X_test], axis=1)

# Save as CSV (no header for XGBoost)
os.makedirs("data/ml", exist_ok=True)
train_df.to_csv("data/train.csv", index=False, header=False)
test_df.to_csv("data/test.csv", index=False, header=False)

print("✅ Train/test CSVs saved in data/")