import boto3

def restore_bucket(bucket_name, aws_access_key_id, aws_secret_access_key, region_name):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    s3 = session.client('s3')
    
    paginator = s3.get_paginator('list_object_versions')
    
    all_delete_markers = []
    
    # Paginate through all objects in the bucket, including those in "folders"
    for page in paginator.paginate(Bucket=bucket_name):
        if 'DeleteMarkers' in page:
            for delete_marker in page['DeleteMarkers']:
                if delete_marker['IsLatest']:
                    all_delete_markers.append({
                        'Key': delete_marker['Key'],
                        'VersionId': delete_marker['VersionId']
                    })
    

    batch_size = 1000
    for i in range(0, len(all_delete_markers), batch_size):
        batch = all_delete_markers[i:i + batch_size]
        if batch:
            s3.delete_objects(
                Bucket=bucket_name,
                Delete={'Objects': batch}
            )
            print(f"Removed {len(batch)} delete markers")
    
    print(f"Total delete markers removed: {len(all_delete_markers)}")


bucket_name = 'xxxx'
aws_access_key_id = 'xxx'
aws_secret_access_key = 'xxx'
region_name = 'xxxx'  

restore_bucket(bucket_name, aws_access_key_id, aws_secret_access_key, region_name)