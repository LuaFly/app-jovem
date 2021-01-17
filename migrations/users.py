from os import getenv

from google.cloud import bigquery, exceptions
from schemas.users import table_users


def create(drop_all: bool = False):
    client = bigquery.Client()
    table_id = "{}.users".format(getenv("PROJECT_ID"))
    if drop_all:
        print("Droping table {}".format(table_id))
        client.delete_table(table_id, not_found_ok=True)
    try:
        table = bigquery.Table(table_id, schema=table_users)
        table = client.create_table(table)

        print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))
    except exceptions.Conflict:
        print("Table {} already exists".format(table_id))


def insert(data: dict):
    client = bigquery.Client()
    table_id = "{}.users".format(getenv("PROJECT_ID"))
    try:
        table = bigquery.Table(table_id, schema=table_users)
        table = client.get_table(table)
        client.insert_rows_json(table, [data])
        return True
    except TypeError as e:
        print(str(e))
    return False