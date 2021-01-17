from google.cloud import bigquery

table_users = [
    bigquery.SchemaField("ID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("NAME", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("EMAIL", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("PASSWORD", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("ZIP_CODE", "STRING", mode="REQUIRED")
]