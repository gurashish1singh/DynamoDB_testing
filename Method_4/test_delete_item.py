import test_create_table

# Deleting an item
def delete_item(table,key_name,attr):
    request = table.delete_item(
        Key = {
            'name' : key_name
        },
    )
    return request

# Getting the respective table to work on
table = test_create_table.dynamodb.Table(test_create_table.table_name)

response = delete_item(table,'Ratesheets')
print(response)
