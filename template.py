import os
from pathlib import Path

project_name = "src"

list_of_files = [

    # Main initialization
    f"{project_name}/__init__.py",

    # Data components
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",         # Reddit + Stock price fetching
    f"{project_name}/components/sentiment_analysis.py",     # FinBERT/VADER
    f"{project_name}/components/feature_engineering.py",    # Merging sentiment with stock data
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluator.py",
    f"{project_name}/components/model_deployer.py",

    # Configuration modules
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    # Cloud & local storage
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_utils.py",

    # MongoDB/Reddit/Yahoo data access
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/reddit_data.py",
    f"{project_name}/data_access/yahoo_data.py",

    # Constants for configuration
    f"{project_name}/constants/__init__.py",

    # Entity classes (data containers)
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/sentiment_entity.py",

    # Logging and Exception handling
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",

    # Pipelines
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # Utility functions
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # Main entry point & supporting files
    "app.py",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "requirements.txt",
    "dockerfile",
    ".dockerignore",

    # Config files
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    path = Path(filepath)
    filedir, filename = os.path.split(path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, "w") as f:
            pass
    else:
        print(f"File already exists at: {path}")
