from test_create import *
from collections import OrderedDict

def func(table,name,attr, data):
    request = table.get_item(
        Key={
            'name' : name
        },
        ProjectionExpression=attr
    )['Item']['info']
    #dict_ = OrderedDict()
    request_keys = {k:i for i,k in enumerate(list(map(lambda x: list(x.keys())[0] ,request)))}
    print(request_keys)
    
    #for x,y in enumerate(request_keys): 
    #    dict_[y] = x

    return request[request_keys[data]]
print(func(table,'Input_Json','info', "firstName"))