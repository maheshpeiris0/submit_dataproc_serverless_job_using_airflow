# submit_dataproc_serverless_job_using_airflow
<br>

classairflow.providers.google.cloud.operators.dataproc.DataprocCreateBatchOperator(*, region=None, project_id=PROVIDE_PROJECT_ID, batch, batch_id, request_id=None, retry=DEFAULT, timeout=None, metadata=(), gcp_conn_id='google_cloud_default', impersonation_chain=None, result_retry=DEFAULT, asynchronous=False, deferrable=conf.getboolean('operators', 'default_deferrable', fallback=False), polling_interval_seconds=5, **kwargs)[source]
Bases: airflow.providers.google.cloud.operators.cloud_base.GoogleCloudBaseOperator

Create a batch workload.

Parameters
project_id (str) – Optional. The ID of the Google Cloud project that the cluster belongs to. (templated)

region (str | None) – Required. The Cloud Dataproc region in which to handle the request. (templated)

batch (dict | google.cloud.dataproc_v1.Batch) – Required. The batch to create. (templated)

batch_id (str) – Required. The ID to use for the batch, which will become the final component of the batch’s resource name. This value must be 4-63 characters. Valid characters are /[a-z][0-9]-/. (templated)

request_id (str | None) – Optional. A unique id used to identify the request. If the server receives two CreateBatchRequest requests with the same id, then the second request will be ignored and the first google.longrunning.Operation created and stored in the backend is returned.

retry (google.api_core.retry.Retry | google.api_core.gapic_v1.method._MethodDefault) – A retry object used to retry requests. If None is specified, requests will not be retried.

result_retry (google.api_core.retry_async.AsyncRetry | google.api_core.gapic_v1.method._MethodDefault) – Result retry object used to retry requests. Is used to decrease delay between executing chained tasks in a DAG by specifying exact amount of seconds for executing.

timeout (float | None) – The amount of time, in seconds, to wait for the request to complete. Note that if retry is specified, the timeout applies to each individual attempt.

metadata (Sequence[tuple[str, str]]) – Additional metadata that is provided to the method.

gcp_conn_id (str) – The connection ID to use connecting to Google Cloud.

impersonation_chain (str | Sequence[str] | None) – Optional service account to impersonate using short-term credentials, or chained list of accounts required to get the access_token of the last account in the list, which will be impersonated in the request. If set as a string, the account must grant the originating account the Service Account Token Creator IAM role. If set as a sequence, the identities from the list must grant Service Account Token Creator IAM role to the directly preceding identity, with first account from the list granting this role to the originating account (templated).

asynchronous (bool) – Flag to return after creating batch to the Dataproc API. This is useful for creating long-running batch and waiting on them asynchronously using the DataprocBatchSensor

deferrable (bool) – Run operator in the deferrable mode.

polling_interval_seconds (int) – Time (seconds) to wait between calls to check the run status.
