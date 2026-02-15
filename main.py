# main.py
from src.preprocess import load_data, clean_data, split_data, build_preprocessor
from src.train import train_model, save_model
from src.evaluate import evaluate_model
from src.models import get_models_and_params
from sklearn.model_selection import GridSearchCV
import os

def main():
    # Load + clean
    df = load_data("data/telco_churn.csv")
    df = clean_data(df)
    
    # Split
    X_train, X_test, y_train, y_test = split_data(df)
    
    # Build pipeline preprocessor
    preprocessor = build_preprocessor(X_train)

    # Get models + hyperparameters
    models = get_models_and_params()

    os.makedirs("models", exist_ok=True)

    for name, obj in models.items():
        print(f"\n🔍 Tuning {name} ...")

        # Train pipeline with base model
        pipeline = train_model(preprocessor, obj["model"], X_train, y_train)

        # GridSearchCV for hyperparameter tuning
        grid = GridSearchCV(
            pipeline,
            obj["params"],
            cv=5,
            scoring="roc_auc",
            n_jobs=-1
        )

        grid.fit(X_train, y_train)

        best_model = grid.best_estimator_

        print(f"✅ Best params for {name}: {grid.best_params_}")

        # Evaluate
        evaluate_model(name, best_model, X_test, y_test)

        # Save tuned model
        save_model(best_model, f"models/{name}_tuned.pkl")

if __name__ == "__main__":
    main()
