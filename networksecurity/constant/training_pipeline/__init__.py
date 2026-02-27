# ===============================
# Pipeline Basic Config
# ===============================

PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"

# ===============================
# Data Ingestion Config
# ===============================

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

# 🔥 VERY IMPORTANT (MATCH YOUR ATLAS)
DATA_INGESTION_DATABASE_NAME: str = "ABHAYAI"
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"


# ===============================
# Data Validation
# ===============================

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


# ===============================
# Data Transformation
# ===============================

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessor.pkl"


# ===============================
# Model Trainer
# ===============================

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_FILE_NAME: str = "model.pkl"

MODEL_TRAINER_EXPECTED_SCORE: float = 0.7
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05