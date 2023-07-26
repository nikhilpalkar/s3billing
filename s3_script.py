import boto3
import json
access_key= '******'
secret_key= '#####'
s3_client = boto3.client('s3', aws_access_key_id=*****, aws_secret_access_key=#####)
ce_client = boto3.client('ce', aws_access_key_id=*****, aws_secret_access_key=#####)
def get_billing_details():
    response = ce_client.get_cost_and_usage(
        TimePeriod={'Start': '2023-07-26', 'End': '2023-08-26'},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
    )
    return response

