from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import choice

def _choose_branch():
    return choice(['branch_a', 'branch_b'])

with DAG("branching_dag",
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    choose_branch = BranchPythonOperator(
        task_id="choose_branch",
        python_callable=_choose_branch
    )

    branch_a = BashOperator(
        task_id="branch_a",
        bash_command="echo 'Branch A'"
    )

    branch_b = BashOperator(
        task_id="branch_b",
        bash_command="echo 'Branch B'"
    )

    choose_branch >> [branch_a, branch_b]
