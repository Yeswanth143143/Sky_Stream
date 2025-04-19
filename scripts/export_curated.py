import psycopg2
import pandas as pd

# Connect to Postgres
conn = psycopg2.connect(
    dbname="airlinedb",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)
query = """
SELECT
    f.flight_id,
    f.flight_number,
    f.origin,
    f.destination,
    f.departure_time,
    f.arrival_time,
    f.actual_arrival_time,
    f.weather_condition,
    f.is_delayed,
    p.passenger_id,
    p.name AS passenger_name,
    p.email
FROM
    flights f
JOIN
    passengers p ON f.flight_id = p.flight_id;
"""

# Load into DataFrame
df = pd.read_sql_query(query, conn)

# Export to CSV
output_path = "data/curated_flight_data.csv"
df.to_csv(output_path, index=False)

conn.close()
print(f"✅ Curated dataset exported to {output_path}")
