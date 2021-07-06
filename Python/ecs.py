import boto3

client = boto3.client('ecs')

# response = client.describe_task_definition(
#     taskDefinition='graphql-global-live:7'
# )

response = client.list_task_definitions(
    familyPrefix='graphql',
    status='ACTIVE',
    # nextToken='string',
    maxResults=100
)

print(response)