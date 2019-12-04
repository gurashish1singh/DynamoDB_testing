import create_table
from datetime import datetime

def get_item(table,partition_key,sort_key,attr):
    request = table.get_item(
        Key = {
            'year' : partition_key,
            'title' : sort_key
        },
        ProjectionExpression = attr
    )
    return request['Item']

table = create_table.dynamodb.Table(create_table.table_name)
start_time = datetime.now()
response = get_item(table,2013,'Scary MoVie','info')
end_time = datetime.now()
print('Elapsed_time:', end_time-start_time, 'seconds')
print(response)