import test_create
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
                    name = current_path.split('\\')[-1]
                    item_name = file.split('.json')[0]

                    table.put_item(
                        Item={
                            'name' : name,
                            item_name : {
                                item_name : items
                            }
                        }
                        #  ExpressionAttributeNames  = {
                        #     "item_name" : item_name
                        # },
                        # ExpressionAttributeValues={
                        #     ':i': items,
                        # },
                    )

if __name__ == "__main__":

    table = test_create.create_table(test_create.table_name, test_create.existing_tables)    
    start_time = datetime.now()
    dump_items(table)
    end_time = datetime.now()
    print('Elapsed_time:', end_time-start_time, 'seconds')

