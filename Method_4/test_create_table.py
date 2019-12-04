from custom_imports import (
    os,
    json,
    dynamodb,
    dynamodb_client
)

# Taking the table name as the version name
table_name = os.getcwd().split('\\')[-1]
# Getting all the existing tables
existing_tables = dynamodb_client.list_tables()['TableNames']

# Create the DynamoDB table.
def create_table(table_name, existing_tables):
    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'Sheet',
                    'KeyType': 'HASH'   # Partition Key
                },
                {
                    'AttributeName': 'Outer Key',
                    'KeyType': 'RANGE'   # Sort Key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Sheet',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'Outer Key',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':5,
                'WriteCapacityUnits':5
            }
        )

        # Wait until the table exists.
        print('Waiting for table to be created')
        dynamodb_client.get_waiter('table_exists').wait(TableName=table_name)

        if table.table_status=='CREATING':
            print("Table status:", table.table_status)
            print('New Table is being created')
            
    # If table exists, assign the resource services to that table
    else:
        table = dynamodb.Table(table_name)
        print(table, 'Table Exists!')\

    return table
    
if __name__ == "__main__":

    print('create_table')
    create_table(table_name, existing_tables)