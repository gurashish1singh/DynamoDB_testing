import boto3
import json
import os

os.environ['AWS_PROFILE'] = "dynamodb"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

# Instantiating the service
# def instantiate_dynamodb():
dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')


# if __name__ == "__main__":
#     print('Run from custom')
#     instantiate_dynamodb()