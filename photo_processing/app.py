import os
import boto3
from io import BytesIO
from multiwatermark import multiwatermark

# Initialize S3 client
s3_client = boto3.client('s3')

# Load environment variable for processed bucket
DESTINATION_BUCKET = "mjburns-processed-photos"

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Step 1: Define temporary file paths
        tmp_input_path = "/tmp/input_image.jpg"
        tmp_output_path = "/tmp/output_image.jpg"

        # Step 2: Download image from S3 to Lambda /tmp/
        s3_client.download_file(source_bucket, object_key, tmp_input_path)

        # Step 3: Process image using multiwatermark function
        text = "Matt Burns Photography"
        multiwatermark.add_watermark(tmp_input_path, text, tmp_output_path, font_size=36, opacity=128, watermark_count=5)

        # Step 5: Upload processed image back to S3
        s3_client.upload_file(tmp_output_path, DESTINATION_BUCKET, object_key)

        print(f"Processed image uploaded to {DESTINATION_BUCKET}/{object_key}")