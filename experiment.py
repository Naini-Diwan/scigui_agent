import mlflow
import dvc.api

def track_experiment(params, metrics, artifacts):
    with mlflow.start_run():
        for key, value in params.items():
            mlflow.log_param(key, value)
        for key, value in metrics.items():
            mlflow.log_metric(key, value)
        for artifact in artifacts:
            mlflow.log_artifact(artifact)
