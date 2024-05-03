FROM python:3.8

# Install necessary dependencies
RUN pip install boto3 pymysql

# Copy Python script to the container
COPY python.py /

# Command to run the Python script
CMD ["python", "/python.py"]
