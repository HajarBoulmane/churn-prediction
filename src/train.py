# src/train.py
import joblib
from sklearn.pipeline import Pipeline

def train_model(preprocessor, model, X_train, y_train):
    pipeline = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("classifier", model)
    ])
    pipeline.fit(X_train, y_train)
    return pipeline

def save_model(model, path):
    joblib.dump(model, path)
