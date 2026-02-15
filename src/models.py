# src/models.py
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def get_models_and_params():
    models = {
        "LogisticRegression": {
            "model": LogisticRegression(max_iter=5000, solver='saga'),
            "params": {
                "classifier__C": [0.1, 1, 10]
            }
        },
        "RandomForest": {
            "model": RandomForestClassifier(random_state=42),
            "params": {
                "classifier__n_estimators": [100, 200],
                "classifier__max_depth": [None, 10, 20]
            }
        },
        "GradientBoosting": {
            "model": GradientBoostingClassifier(random_state=42),
            "params": {
                "classifier__n_estimators": [100, 200],
                "classifier__learning_rate": [0.05, 0.1]
            }
        }
    }
    return models
