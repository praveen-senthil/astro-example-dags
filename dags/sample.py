def test1():
    print("Hello, World!")

# Define the DAG
with DAG(
    dag_id="hello_world_dag",
    default_args={
        "owner": "airflow",
        "start_date": datetime(2024, 1, 1),
        "retries": 1,
    },
    schedule_interval="* * * * *",  # Runs every 1 minute
    catchup=False,
) as dag:
    
    task_hello = PythonOperator(
        task_id="print_hello",
        python_callable=test1,
    )

    task_hello1 = PythonOperator(
        task_id="print_hello1",
        python_callable=test1,
    )

    task_hello >> task_hello1
