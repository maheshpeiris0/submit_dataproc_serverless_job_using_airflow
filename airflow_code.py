from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateBatchOperator
from airflow.utils.dates import days_ago
from datetime import datetime

default_args = {
    'owner': 'Name',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 18),  
    'retries': 1
}

dag = DAG(
    'hello_example',
    default_args=default_args,
    schedule_interval=None,
)



create_batch = DataprocCreateBatchOperator(
    task_id='hello_dataproc_batch',
    region='us-central1',  # e.g., 'us-central1'
    batch={
        'pyspark_batch': {
            'main_python_file_uri': 'gs://bucket/hello_pyspark.py',  # GCS bucket
        },
    },
    batch_id='tey47rvb', # change it in every run or auto-generated. This value must be 4-63 characters. Valid characters are /[a-z][0-9]-/.
    dag=dag
)
