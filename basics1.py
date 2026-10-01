from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello Airflow")

with DAG(
    dag_id="dag_1_hello_world",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="hello_task",
        python_callable=hello
    )

# DAG
# Task
# PythonOperator
# Task Execution
# Logs
