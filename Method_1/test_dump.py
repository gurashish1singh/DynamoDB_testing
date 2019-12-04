import test_create
import os
import json
from datetime import datetime

def dump_items(table):
    json_files = [file for file in os.listdir() if file.endswith('.json')]
    # print(json_files)

    # Parsing json file for requried data
    for file in json_files:
        with open(file) as json_file:
            items = json.load(json_file)
            # print(len(items))
            # print(items)
            # for item in items:
            #     name = file.split('.json')[0]
            #     print(name)
            #     data = items

            #     print('Adding item: ', name, data)

            # Inserting items in the table
            table.put_item(
                Item={
                    'name':file.split('.json')[0],
                    'data':items
                }
            )


if __name__ == "__main__":

    table = test_create.create_table(test_create.table_name, test_create.existing_tables)    
    start_time = datetime.now()
    dump_items(table)
    end_time = datetime.now()
    print('Elapsed_time:', end_time-start_time, 'seconds')