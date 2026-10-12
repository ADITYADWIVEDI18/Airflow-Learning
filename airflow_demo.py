from datetime import datetime
from airflow.decorators import dag, task


@dag(
    dag_id="demo_life_event_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def pipeline():

    @task
    def validate():
        print("Validating data...")

    @task
    def prepare():
        print("Preparing model data...")

    @task
    def upload():
        print("Uploading data to S3...")

    @task
    def train():
        print("Training model in SageMaker...")

    @task
    def evaluate():
        print("Evaluating model...")

    @task
    def predict():
        print("Generating predictions...")

    v = validate()
    p = prepare()
    u = upload()
    t = train()
    e = evaluate()
    pred = predict()

    v >> p >> u >> t >> e >> pred


pipeline()
