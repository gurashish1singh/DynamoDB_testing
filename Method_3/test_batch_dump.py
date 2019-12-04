import test_create_table
import os
import json
from botocore.exceptions import ClientError
from datetime import datetime\



def batch_dump(table):
    with table.batch_writer(overwrite_by_pkeys=['name']) as batch:
        for current_path, dirnames, filename in os.walk(os.getcwd()):
            for file in filename:
                if file.endswith('.json') and not file.startswith('setting') and not file.startswith('launch'):
                    with open(os.path.join(current_path, file)) as json_file:
                        items = json.load(json_file)
                        key_name = current_path.split('\\')[-1]
                        item_name = file.split('.json')[0]

                        batch.put_item(
                            Item = {
                                'name' : key_name,
                                'item' : items
                            }
                        )

if __name__ == "__main__":

    table = test_create_table.create_table(test_create_table.table_name, test_create_table.existing_tables)    
    start_time = datetime.now()
    batch_dump(table)
    end_time = datetime.now()
    print('Time to dump items:', end_time-start_time, 'seconds')