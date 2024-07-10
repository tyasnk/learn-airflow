from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.utils.dates import days_ago

default_args = {"owner": "airflow"}

with DAG(
    "medallion_sales_dag",
    start_date=days_ago(2),
    schedule_interval=None,
    default_args=default_args,
) as dag:

    mount = DatabricksRunNowOperator(
        task_id="mount", databricks_conn_id="databricks_default", job_id=461897774379636
    )

    data_structure_creation = DatabricksRunNowOperator(
        task_id="data_structure_creation", databricks_conn_id="databricks_default", job_id=179527302079419
    )

    mount >> data_structure_creation
