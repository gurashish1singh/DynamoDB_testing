import create_table
import os
import json
import decimal
# from botocore.exceptions import ClientError
from datetime import datetime

def dump_items(table):
    with open('moviedata.json') as json_file:
        movies = json.load(json_file, parse_float=decimal.Decimal)
        for movie in movies:
            year = int(movie['year'])
            title = movie['title']
            info = movie['info']

            # Inserting items in the table
            try:
                table.update_item(
                    Key={
                        'year' : year,
                    },
                    UpdateExpression="SET #info = :i",
                    ExpressionAttributeNames  = {
                        "#info" : title
                    },
                    ExpressionAttributeValues={
                        ':i': info,
                    }
                )
            except ClientError as e:
                print(e)
                print(Exception)


if __name__ == "__main__":

    table = create_table.create_table(create_table.table_name, create_table.existing_tables)    
    start_time = datetime.now()
    dump_items(table)
    end_time = datetime.now()
    print('Elapsed_time:', end_time-start_time, 'seconds')