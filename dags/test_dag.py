from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def testing1():
  print("Testing1...")

def testing2():
  print("Testing2...")

with DAG(
  dag_id = "simpleTest_dag",
  default = {
      "owner" : "airflow",
      "start_date" : datetime(2025, 02, 06),
      "retries" : 1
  },
  schedule_interval = '*/1 * * * *',
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
