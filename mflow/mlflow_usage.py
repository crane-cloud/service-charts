import mlflow
!pip install mlflow

mlflow.set_tracking_uri("https://mlflow.renu-01.cranecloud.io/")

# Set experiment name or create a new one if it doesn't exist
mlflow.set_experiment( < name_of_experiment > )

# Start an MLflow run
# Log parameters, metrics, and artifacts
mlflow.log_param("param_name", param_value)
mlflow.log_metric("metric_name", metric_value)
mlflow.log_artifact("path_to_artifact")
