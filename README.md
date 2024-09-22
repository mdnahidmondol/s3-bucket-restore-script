# S3 Bucket Restore Script

This Python script removes delete markers from an Amazon S3 bucket, effectively restoring all "deleted" objects in the bucket. It's designed to work with buckets that have versioning enabled.

## Features

- Restores all deleted objects in an S3 bucket by removing delete markers
- Handles buckets with folders (prefixes)
- Processes delete markers in batches to comply with S3 API limits
- Provides progress updates and a final count of restored objects

## Prerequisites

- Python 3.6 or higher
- Boto3 library
- AWS account with appropriate S3 permissions

## Setup

1. Ensure you have Python installed on your system.
2. Install the required Boto3 library:
   ```
   pip install boto3
   ```
3. Set up your AWS credentials. You can do this by:
   - Setting environment variables
   - Using AWS CLI (`aws configure`)
   - Directly in the script (not recommended for security reasons)

## Usage

1. Open the script in a text editor.
2. Modify the following variables at the bottom of the script:
   - `bucket_name`: Your S3 bucket name
   - `aws_access_key_id`: Your AWS access key
   - `aws_secret_access_key`: Your AWS secret key
   - `region_name`: The AWS region where your bucket is located

3. Save the changes.
4. Run the script:
   ```
   python s3_bucket_restore.py
   ```

## Important Considerations

- This script will restore ALL deleted objects in the specified bucket. Make sure this is what you intend to do.
- Ensure you have the necessary permissions to list and delete object versions in the S3 bucket.
- The script processes delete markers in batches of 1000 to comply with S3 API limits.
- Depending on the size of your bucket and the number of delete markers, this script may take some time to complete.
- It's recommended to test this script on a non-production bucket first.

## Security Note

Avoid hardcoding AWS credentials directly in the script, especially if the script will be shared or stored in version control. Instead, use AWS CLI configuration or environment variables to manage credentials securely.

