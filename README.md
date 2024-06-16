# submit_dataproc_serverless_job_using_airflow
<br>



```markdown
# DataprocCreateBatchOperator

The `DataprocCreateBatchOperator` is an Apache Airflow operator designed to streamline the creation of batch workloads within Google Cloud Dataproc.

## Class Definition

```python
class airflow.providers.google.cloud.operators.dataproc.DataprocCreateBatchOperator(
    *,
    region=None,
    project_id=PROVIDE_PROJECT_ID,
    batch,
    batch_id,
    request_id=None,
    retry=DEFAULT,
    timeout=None,
    metadata=(),
    gcp_conn_id='google_cloud_default',
    impersonation_chain=None,
    result_retry=DEFAULT,
    asynchronous=False,
    deferrable=conf.getboolean('operators', 'default_deferrable', fallback=False),
    polling_interval_seconds=5,
    **kwargs
)
```

## Base Class

`airflow.providers.google.cloud.operators.cloud_base.GoogleCloudBaseOperator`

## Key Parameters

| Parameter               | Description                                                                                             | Required |
|-------------------------|---------------------------------------------------------------------------------------------------------|----------|
| `project_id` (str)      | The Google Cloud project ID associated with the cluster. (templated)                                    | Optional |
| `region` (str)          | The Cloud Dataproc region to handle the request. (templated)                                            | Yes      |
| `batch` (dict/object)   | The batch configuration (either a dictionary or a `google.cloud.dataproc_v1.Batch` object). (templated) | Yes      |
| `batch_id` (str)        | A unique ID for the batch (4-63 characters, lowercase, numbers, hyphens). (templated)                    | Yes      |
| `request_id` (str)      | A unique ID for the request (optional).                                                                 | No       |
| `asynchronous` (bool)   | If True, returns immediately after submitting the batch creation request, enabling asynchronous monitoring. | No       |

## Additional Parameters

Refer to the official documentation for details on parameters like `retry`, `timeout`, `metadata`, `gcp_conn_id`, `impersonation_chain`, `result_retry`, `deferrable`, and `polling_interval_seconds`.

## Example Usage

```python
from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateBatchOperator

with DAG(...) as dag:
    create_batch = DataprocCreateBatchOperator(
        task_id='create_batch',
        # ... (other parameters)
    )
```

## Notes

- The operator leverages the Google Cloud Python client library. Make sure you have the necessary dependencies installed.
- For in-depth usage and customization options, consult the [Apache Airflow documentation](https://airflow.apache.org/).
```

airflow dependency 
pip install apache-airflow-providers-google

Google cloud Bigquery connector
https://cloud.google.com/dataproc-serverless/docs/guides/bigquery-connector-spark-example
https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases
