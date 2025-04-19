import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

conn = psycopg2.connect(
    dbname="airlinedb",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Drop if exists
cur.execute("DROP TABLE IF EXISTS flights, passengers, crew;")

# Create tables
cur.execute("""
CREATE TABLE flights (
    flight_id SERIAL PRIMARY KEY,
    flight_number VARCHAR(10),
    origin VARCHAR(50),
    destination VARCHAR(50),
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP
);
""")

cur.execute("""
CREATE TABLE passengers (
    passenger_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    flight_id INTEGER REFERENCES flights(flight_id)
);
""")

cur.execute("""
CREATE TABLE crew (
    crew_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50),
    assigned_flight INTEGER REFERENCES flights(flight_id)
);
""")

# Insert flights
flights = []
for _ in range(10):
    dep_time = fake.date_time_this_year()
    arr_time = dep_time + timedelta(hours=random.randint(1, 5))
    cur.execute("""
        INSERT INTO flights (flight_number, origin, destination, departure_time, arrival_time)
        VALUES (%s, %s, %s, %s, %s) RETURNING flight_id;
    """, (
        f"UA{random.randint(100,999)}",
        fake.city(),
        fake.city(),
        dep_time,
        arr_time
    ))
    flights.append(cur.fetchone()[0])

# Insert passengers and crew
for _ in range(50):
    cur.execute("""
        INSERT INTO passengers (name, email, flight_id)
        VALUES (%s, %s, %s);
    """, (fake.name(), fake.email(), random.choice(flights)))

roles = ['Pilot', 'Co-Pilot', 'Cabin Crew']
for _ in range(15):
    cur.execute("""
        INSERT INTO crew (name, role, assigned_flight)
        VALUES (%s, %s, %s);
    """, (fake.name(), random.choice(roles), random.choice(flights)))

conn.commit()
cur.close()
conn.close()
print("✅ Database seeded with mock data.")