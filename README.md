# SkyStream 🚀 – Airline Data Engineering Project

An industrial-style AWS Data Engineering project simulating airline operations & customer intelligence.

## Features
- PostgreSQL database for flight operations
- JSON aircraft sensor logs
- Streamlit-based feedback API (upcoming)
- ETL pipeline to AWS S3 using Boto3
- Query with Athena, model with SageMaker, deploy with Jenkins (later phases)

## Setup

```bash
python -m venv sky_stream
./sky_stream/bin/activate
pip install -r requirements.txt
docker-compose up -d
python scripts/init_postgres.py

# SKY_STREAM: End-to-End Data Engineering Pipeline in AWS

## 🧠 Project Overview
This is an industrial-style AWS Data Engineering project that simulates a real-world scenario for an airline company. The project demonstrates data ingestion, data lake architecture, serverless querying, and ML readiness using AWS services.

## 🛠 Tech Stack
- Python (virtualenv)
- Docker + PostgreSQL (mock database)
- AWS S3, Glue, Athena
- Pandas, Faker
- boto3
- Streamlit (UI planned)
- AWS SageMaker (ML planned)

## 🧱 Architecture

1. **PostgreSQL (Docker)** → Mock Passenger Data (using Faker)
2. **Python Script** → Ingest to S3 (Raw Zone)
3. **Glue Crawler** → Register data in Glue Catalog
4. **Athena** → Query raw CSV via SQL
5. **Python Cleaning** → Upload to Curated S3 Zone
6. **Glue + Athena** → Query curated data
7. **Coming Soon** → ML Model with SageMaker + Streamlit Analytics

## 📁 Folder Structure

SKY_STREAM/ 
├── .env 
├── docker/ 
│ └── docker-compose.yml 

├── scripts/ 
│ ├── init_postgres.py │ 
├── generate_sensor_logs.py │ 
├── postgres_to_s3.py │ 
├── curate_passenger_data.py 

├── data/ 
├── tmp/ 
├── README.md 
└── requirements.txt
