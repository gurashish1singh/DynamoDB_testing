import test_create_table
from datetime import datetime

def get_item(table,key_name,attr):
    request = table.get_item(
        Key = {
            'name' : key_name
        },
        #ProjectionExpression = attr
    )
    return request['Item'][attr]

table = test_create_table.dynamodb.Table(test_create_table.table_name)
start_time = datetime.now()
response = get_item(table,'Ratesheets','sample-json-file - Copy (2)')['Pets']
end_time = datetime.now()
print('Elapsed_time:', end_time-start_time, 'seconds')
print(response)
# print(func(table, 'Ratesheets'))
# print(func(table, 'Input_Json')['example_2 - Copy (2)']['quiz']['maths'])
# print(func(table, 'Ratesheets')['sample-json-file - Copy']['Boolean'])



# def func(table,name,attr, data):
#     request = table.get_item(
#         Key={
#             'name' : name
#         },
#         ProjectionExpression=attr
#     )['Item']['info']
#     #dict_ = OrderedDict()
#     request_keys = {k:i for i,k in enumerate(list(map(lambda x: list(x.keys())[0] ,request)))}
#     print(request_keys)
    
#     #for x,y in enumerate(request_keys): 
#     #    dict_[y] = x

#     return request[request_keys[data]]

# print(func(table,'Input_Json','info', "firstName"))