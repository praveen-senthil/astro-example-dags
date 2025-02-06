from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def my_python_function():
    print("Hello from Python!")

with DAG("simple_dag",
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    python_task = PythonOperator(
        task_id="python_task",
        python_callable=my_python_function
    )

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo 'Hello from Bash!'"
    )

    python_task >> bash_task
