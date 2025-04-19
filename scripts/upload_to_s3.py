import os
import boto3
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load AWS credentials
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("CURATED_BUCKET_NAME")

# Upload to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

s3.upload_file("data/curated_flight_data.csv", S3_BUCKET, "passenger_flight_data.csv")
print("✅ Data uploaded to S3 bucket")