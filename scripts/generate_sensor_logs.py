import json
from faker import Faker
import random
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

fake = Faker()

def generate_log_entry():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "aircraft_id": f"AC{random.randint(1000,9999)}",
        "altitude": random.randint(20000, 40000),
        "speed": random.randint(400, 600),
        "engine_temp": round(random.uniform(200.0, 500.0), 2),
        "location": fake.city()
    }

logs = [generate_log_entry() for _ in range(20)]

with open("data/sensor_logs.json", "w") as f:
    json.dump(logs, f, indent=4)

print("✅ Sensor log JSON created in data/sensor_logs.json")
