import test_create_table
import os
import json
from botocore.exceptions import ClientError
from datetime import datetime

def dump_items(table):
    for current_path, dirnames, filename in os.walk(os.getcwd()):
        for file in filename:
            if file.endswith('.json') and not file.startswith('setting') and not file.startswith('launch'):
                with open(os.path.join(current_path,file)) as json_file:
                    items = json.load(json_file)
                    key_name = current_path.split('\\')[-1]
                    item_name = file.split('.json')[0]

                    try:
                        # start_time = datetime.datetime.now()
                        table.update_item(
                            Key={
                                'name': key_name,
                            },
                            # AttributeUpdates={
                            #     'info': {
                            #         'Value': items,
                            #         'Action': 'ADD'
                            #     }
                            # },
                            # UpdateExpression="SET #item_name = list_append(#item_name, :i)",
                            UpdateExpression="SET #item_name = :i",
                            ExpressionAttributeNames  = {
                                "#item_name" : item_name
                            },
                            ExpressionAttributeValues={
                                ':i': items,
                            },
                            # ReturnValues="UPDATED_NEW"
                        )
                        # print('Uploading:', name,items)
                        # end_time = datetime.datetime.now()
                    except ClientError as e:
                        print(e)
                        print(Exception)
                        if e.response['Error']['Code'] == 'ValidationException':
                            # start_time_e = datetime.datetime.now()
                            table.update_item(
                            Key={
                                'name': key_name,
                            },
                            UpdateExpression="SET #item_name = :i",
                            ExpressionAttributeNames  = {
                                "#item_name" : item_name
                            },
                            ExpressionAttributeValues={
                                ':i': items,
                            },
                            # ReturnValues="UPDATED_NEW"
                        )
                        # print('Creating:', name,items)
                        # end_time_e = datetime.datetime.now()

    # print('ElapsedTimeIfItemExists: ', end_time-start_time)
    # print('ElapsedTimeIfItemDoesNotExists: ', end_time_e-start_time_e)

if __name__ == "__main__":

    table = test_create_table.create_table(test_create_table.table_name, test_create_table.existing_tables)    
    start_time = datetime.now()
    dump_items(table)
    end_time = datetime.now()
    print('Elapsed_time:', end_time-start_time, 'seconds')

