from custom_imports import (
    os,
    json,
    dynamodb,
    dynamodb_client
)

table_name = os.getcwd().split('\\')[-1]
existing_tables = dynamodb_client.list_tables()['TableNames']

# Create the DynamoDB table.
def create_table(table_name, existing_tables):
    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'   # PK
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':5,
                'WriteCapacityUnits':5
            }
        )

        # Wait until the table exists.
        dynamodb_client.get_waiter('table_exists').wait(TableName=table_name)

        if table.table_status=='CREATING':
            print("Table status:", table.table_status)

    else:
        print('Table exists')
        table = dynamodb.Table(table_name)
    
    return table

if __name__ == "__main__":

    print('create_table')
    create_table(table_name, existing_tables)