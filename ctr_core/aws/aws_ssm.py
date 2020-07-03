import boto3


def fetch_ssm_config(name):
    ssm = boto3.client('ssm')
    data = ssm.get_parameter(Name=name)
    value = data['Parameter']['Value']
    return value
