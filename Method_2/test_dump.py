import test_create
import os
import json
from botocore.exceptions import ClientError
import datetime

def dump_items(table):
    for current_path, dirnames, filename in os.walk(os.getcwd()):
        for file in filename:
            if file.endswith('.json') and not file.startswith('setting') and not file.startswith('launch'):
                with open(os.path.join(current_path,file)) as json_file:
                    items = json.load(json_file)
                    name = current_path.split('\\')[-1]
                    # # dict[(current_path.split('\\')[-1])] = items
                    # print(current_path.split('\\')[-1])
                    # print(items)

                    # Inserting items in the table
                    # if name in table.key_schema['AttributeName']:
                    #     print('Exists')
                    # else:
                    try:
                        start_time = datetime.datetime.now()
                        table.update_item(
                            Key={
                                'name': name,
                            },
                            # AttributeUpdates={
                            #     'info': {
                            #         'Value': items,
                            #         'Action': 'ADD'
                            #     }
                            # },
                            UpdateExpression="SET info = list_append(info, :i)",
                            ExpressionAttributeValues={
                                ':i': [items],
                            },
                            # ReturnValues="UPDATED_NEW"
                        )
                        print('Uploading:', name,items)
                        end_time = datetime.datetime.now()
                    except ClientError as e:
                        if e.response['Error']['Code'] == 'ValidationException':
                            start_time_e = datetime.datetime.now()
                            table.update_item(
                            Key={
                                'name': name,
                            },
                            UpdateExpression="SET info = :i",
                            ExpressionAttributeValues={
                                ':i': [items],
                            },
                            # ReturnValues="UPDATED_NEW"
                        )
                        print('Creating:', name,items)
                        end_time_e = datetime.datetime.now()

    print('ElapsedTimeIfItemExists: ', end_time-start_time)
    print('ElapsedTimeIfItemDoesNotExists: ', end_time_e-start_time_e)

if __name__ == "__main__":

    table = test_create.create_table(test_create.table_name, test_create.existing_tables)    
    # start_time = datetime.now()
    dump_items(table)
    # end_time = datetime.now()
    # print('Elapsed_time:', end_time-start_time, 'seconds')











# import glob
# import os
# import json

# dict = {}
# result = []

# for current_path, dirnames, filename in os.walk(os.getcwd()):
#     for file in filename:
#         if file.endswith('.json') and not file.endswith('_merged.json') and not file.startswith('setting') and not file.startswith('launch'):
#             name = os.path.join(current_path.split('\\')[-1] + "_merged.json")
#             with open(name,'a') as out:
#                 # out.write(f"[{','.join(open(os.path.join(current_path,file),'''rt'''))}]")
#                 out.write(f'''{','.join(open(os.path.join(current_path,file),"r"))}''')

# read_files = glob.glob('**/*.json')
# for file in read_files:
#     name = file.split('\\')[0]+"_merged.json"
#     with open(name, "a") as outfile:
#         outfile.write(json.load())

# for json_file in glob.glob('**/*.json',recursive=True):
#     print(json_file)

# read_files = glob.glob('**/*.json')

# with open('merged.json', "a") as outfile:
#     outfile.write('[{}]'.format(
#         ',\n'.join([open(f, "r").read() for f in read_files])))

# for current_path, dirnames, filename in os.walk(os.getcwd()):
#     for file in filename:
#         if file.endswith('.json') and not file.startswith('setting') and not file.startswith('launch'):
#             with open(os.path.join(current_path,file)) as json_file:
#                 items = json.load(json_file)
#                 name = current_path.split('\\')[-1]
#                 # # dict[(current_path.split('\\')[-1])] = items
#                 # print(current_path.split('\\')[-1])
#                 # print(items)

#                 # Inserting items in the table
#                 # if name in table.key_schema['AttributeName']:
#                 #     print('Exists')
#                 # else:
#                 table.put_item(
#                     Item={
#                         'name':current_path.split('\\')[-1],
#                         'data':items
#                     }
#                 )
    # json_files = [file for file in os.listdir() if file.endswith('.json')]
# print('names:',names,'\n','files:', json_files)

# # Parsing json file for requried data
# for file in json_files:
#     with open(file) as json_file:
#         items = json.load(json_file)
#         # print(names)
#         # print(len(items))
#         # print(items)
#         for item in items:
#             name = file.split('.json')[0]
#             print(name)
#             data = items

#             print('Adding item: ', name, data)

#         Inserting items in the table
#         table.put_item(
#             Item={
#                 'name':file.split('.json')[0],
#                 'data':items
#             }
#         )




