from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateBatchOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import string
import random

# Generate a random batch_id
def generate_batch_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits + '-', k=10))


default_args = {
    'owner': 'Name',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 18),  
    'retries': 0
}

dag = DAG(
    'gcs_to_gbq',
    default_args=default_args,
    schedule_interval=None,
)



create_batch = DataprocCreateBatchOperator(
    task_id='hello_dataproc_batch',
    region='us-central1',  # e.g., 'us-central1'
    batch={
        'runtime_config': {
            'version': '2.2'  # specify the runtime version
        },
        
        'pyspark_batch': {
            'main_python_file_uri': 'gs://bucket_name/dataproc_gcs_to_gbq.py',  # GCS bucket path to the file
        },
    },
    batch_id=generate_batch_id(), # change it in every run or auto-generated. This value must be 4-63 characters. Valid characters are /[a-z][0-9]-/.
    dag=dag
)
