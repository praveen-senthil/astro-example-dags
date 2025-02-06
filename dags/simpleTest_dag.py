from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def testing1():
  print("Testing1...")

def testing2():
  print("Testing2...")

default = {
      "owner" : "airflow",
      "start_date" : datetime(2025, 6, 2),
      "retries" : 1
  }

with DAG(
  dag_id = "simpleTest_dag",
  schedule_interval = '@daily',
  catchup = False
) as dag :
        test1_task = PythonOperator(
          task_id = 'test1',
          python_callable  = testing1
        )

        test2_task = PythonOperator(
          task_id = 'test2',
          python_callable = testing2
        )

        test2_task >> test1_task
