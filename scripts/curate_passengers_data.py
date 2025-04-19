import os
import pandas as pd

# Load raw data
raw_path = "tmp/passenger_data.csv"
df = pd.read_csv(raw_path)

# Basic cleaning: Remove nulls, uppercase names, drop duplicates
df = df.dropna()
df["name"] = df["name"].str.upper()
df = df.drop_duplicates(subset=["email"])

# Save locally
os.makedirs("tmp", exist_ok=True)
clean_path = "tmp/curated_passenger_data.csv"
df.to_csv(clean_path, index=False)

# Upload to curated S3 bucket
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

s3.upload_file(
    clean_path,
    os.getenv("CURATED_BUCKET_NAME"),  # We’ll add this in .env
    "passengers/curated_passenger_data.csv"
)

print("✅ Cleaned data uploaded to curated S3 zone")
