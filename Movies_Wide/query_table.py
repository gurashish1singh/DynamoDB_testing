import create_table
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr

def query_table(table,partition_key,sort_key,attr_partition_key,condition):

    request = table.query(
        KeyConditionExpression=Key(partition_key).eq(attr_partition_key) & Key(sort_key).begins_with(condition)
    )
    return request['Items']


table = create_table.dynamodb.Table(create_table.table_name)
start_time = datetime.now()
response = query_table(table,'year','title',1985,'B')
end_time = datetime.now()
print('Elapsed_time:', end_time-start_time, 'seconds')

for item in response:
    print(item['title'])
    print(item['info']['actors'])
