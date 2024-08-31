import boto3

client = boto3.client('ecr', region_name='us-east-1')

response = client.create_repository(repositoryName='resource_monitoring_app_cloud_native')

repository_uri = response['repository']['repositoryUri']
print(repository_uri)


