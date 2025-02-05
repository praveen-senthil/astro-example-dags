from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, World!")

# Define the DAG
with DAG(
    dag_id="hello_world_dag",
    default_args={
        "owner": "airflow",
        "start_date": datetime(2024, 1, 1),
        "retries": 1,
    },
    schedule_interval="* * * *",
    catchup=False,
) as dag:
    
    task_hello = PythonOperator(
        task_id="hello",
        python_callable=print_hello,
    )

    task_hello1 = PythonOperator(
        task_id="print_hello1",
        python_callable=print_hello,
    )

    task_hello >> task_hello1
