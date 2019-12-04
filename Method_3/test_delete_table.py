import test_create_table

def delete_table(table_name):
    test_create.dynamodb_client.delete_table(TableName=table_name)
    test_create.dynamodb_client.get_waiter('table_not_exists').wait(TableName=table_name)
    print(table_name, 'deleted successfully!')

if __name__ == "__main__":
    print('Deleting table')
    table = test_create.dynamodb.Table(test_create.table_name) 
    delete_table(table.table_name)