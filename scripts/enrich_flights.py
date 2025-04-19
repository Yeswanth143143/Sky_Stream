import psycopg2
import random
from datetime import timedelta

# Connect to Postgres
conn = psycopg2.connect(
    dbname="airlinedb",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Add new columns
cur.execute("""
    ALTER TABLE flights
    ADD COLUMN IF NOT EXISTS weather_condition VARCHAR(20),
    ADD COLUMN IF NOT EXISTS actual_arrival_time TIMESTAMP,
    ADD COLUMN IF NOT EXISTS is_delayed INT;
""")
conn.commit()

# 2. Simulate actual arrival time and weather
weather_options = ['Clear', 'Rain', 'Fog', 'Snow', 'Storm']

cur.execute("SELECT flight_id, arrival_time FROM flights;")
flights = cur.fetchall()

for flight_id, est_arrival in flights:
    # Simulate actual arrival time: within +/- 2 hours of estimated
    delta_minutes = random.randint(-20, 120)  # -20 early to +120 mins late
    actual_arrival = est_arrival + timedelta(minutes=delta_minutes)
    weather = random.choice(weather_options)

    cur.execute("""
        UPDATE flights
        SET actual_arrival_time = %s,
            weather_condition = %s
        WHERE flight_id = %s;
    """, (actual_arrival, weather, flight_id))

conn.commit()

# 3. Update is_delayed flag
cur.execute("""
    UPDATE flights
    SET is_delayed = CASE 
        WHEN actual_arrival_time > arrival_time THEN 1
        ELSE 0
    END;
""")
conn.commit()

cur.close()
conn.close()
print("✅ flights table enriched with weather_condition and is_delayed")
