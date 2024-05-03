import boto3

def read_from_s3():
    # Initialize Boto3 S3 client
    s3 = boto3.client('s3')
    
    # Example: Read data from S3 bucket
    response = s3.get_object(Bucket='keka-bucket', Key='sales_data_sample.csv')
    data = response['Body'].read()

    # Try decoding using different encodings
    encodings = ['utf-8', 'iso-8859-1']  # Add more encodings if needed
    for encoding in encodings:
        try:
            decoded_data = data.decode(encoding)
            return decoded_data
        except UnicodeDecodeError:
            continue

    # If none of the encodings work, raise an error
    raise UnicodeDecodeError("Failed to decode data using any of the specified encodings")

    return data

# Rest of the code remains the same
