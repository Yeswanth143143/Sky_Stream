import pandas as pd
import numpy as np
import os
from faker import Faker
import random

fake = Faker()
random.seed(42)

# Generate fake data
n = 500
data = {
    "flight_id": [f"UA{random.randint(100,999)}" for _ in range(n)],
    "departure_hour": [random.randint(0, 23) for _ in range(n)],
    "weather_condition": [random.choice(["clear", "rain", "storm", "fog", "snow"]) for _ in range(n)],
    "route_distance_km": [random.randint(300, 2500) for _ in range(n)],
    "day_of_week": [random.randint(0, 6) for _ in range(n)],
    "is_delayed": []
}

# Generate target with some rule-based logic
for i in range(n):
    score = 0
    if data["weather_condition"][i] in ["storm", "fog", "snow"]:
        score += 1
    if data["departure_hour"][i] in [20, 21, 22, 23, 0, 1, 2]:
        score += 1
    if data["route_distance_km"][i] > 1800:
        score += 1
    data["is_delayed"].append(1 if score >= 2 else 0)

df = pd.DataFrame(data)

# Save locally
os.makedirs("tmp", exist_ok=True)
df.to_csv("tmp/flight_delays.csv", index=False)
print("✅ flight_delays.csv created")
