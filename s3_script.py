import boto3
import json
access_key= 'billing_user'
secret_key= '9zRZbj3}'
s3_client = boto3.client('s3', aws_access_key_id=billing_user, aws_secret_access_key=9zRZbj3})
ce_client = boto3.client('ce', aws_access_key_id=billing_user, aws_secret_access_key=9zRZbj3})
def get_billing_details():
    response = ce_client.get_cost_and_usage(
        TimePeriod={'Start': '2023-07-26', 'End': '2023-08-26'},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
    )
    return response

