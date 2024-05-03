S3 to RDS (or Glue Database) Data Pipeline

Overview:

This repository contains code for creating a data pipeline that reads data from an S3 bucket and pushes it to an RDS instance. If RDS is not available, the data is pushed to a Glue Database. The pipeline is deployed using AWS services and managed through Terraform. Jenkins CI/CD pipeline is utilized for code deployment and resource creation.

Prerequisites:

Before getting started, ensure you have the following:

AWS account with appropriate permissions
Terraform installed locally
Docker installed locally
Jenkins server for CI/CD pipeline setup
Repository Structure

dockerfile: Contains the Dockerfile for building the Docker image.
python.py: Python script that reads data from S3 and pushes it to RDS or Glue Database.
terraform: Directory containing Terraform code for creating AWS resources.
jenkinsfile: Jenkinsfile defining the CI/CD pipeline stages.
Getting Started

Clone this repository:
bash
Copy code
git clone https://github.com/IshaGhule/Docker.git

Set up AWS credentials:
Copy code
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key

Build the Docker image:
docker build -t demo_image .

Push the Docker image to AWS ECR:
1. aws ecr get-login-password --region your_region | docker login --username AWS --password-stdin your_account_id.dkr.ecr.your_region.amazonaws.com

2. docker tag s3-to-rds:latest your_account_id.dkr.ecr.us-east-2.amazonaws.com/s3-to-rds:latest
docker push your_account_id.dkr.ecr.us-east-2.amazonaws.com/s3-to-rds:latest

Deploy AWS resources using Terraform:
terraform init
terraform plan
terraform apply

Set up Jenkins CI/CD pipeline:
Configure Jenkins to connect to your GitHub repository.
Create a new pipeline job and point it to the Jenkinsfile in this repository.
Usage

Once the pipeline is set up and running:

Upload data files to the configured S3 bucket.
Jenkins pipeline will trigger automatically upon changes to the repository.
Data will be processed and pushed to RDS (or Glue Database) based on availability.

Testing:

Test the Lambda function by invoking it manually from the AWS Lambda console.
Ensure data is correctly processed and stored in the target database.
