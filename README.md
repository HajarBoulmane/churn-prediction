📊 TelcoChurn: Enterprise-Grade Retention AnalyticsTelcoChurn is a predictive analytics solution designed to mitigate customer attrition. By leveraging Gradient Boosted Trees and a streamlined inference pipeline, this project transforms raw customer telemetry into actionable retention strategies.🎯 Business Value PropositionIn the telecommunications industry, acquiring a new customer is 5-25x more expensive than retaining an existing one. This tool enables retention teams to:Proactively identify high-risk accounts before they churn.Quantify risk via calibrated probability scores.Analyze drivers of churn to tailor personalized win-back offers.🏗️ System ArchitectureThe project implements a decoupled architecture, separating training logic from inference to ensure scalability and maintainability.The ML PipelineIngestion & Cleaning: Handling missing values and class imbalance.Feature Engineering: Automated encoding for categorical variables and scaling.Optimization: Hyperparameter tuning via GridSearchCV with 5-fold cross-validation.Persistence: Model versioning using serialized joblib artifacts.Inference: A stateless Streamlit interface serving real-time predictions.🛠️ Tech StackLayerTechnologyLanguagePython 3.9+Data SciencePandas, NumPy, Scikit-LearnModelGradient Boosting Classifier (GBM)UI / UXStreamlit, Plotly (Interactive Visuals)🚀 Quick StartBash# Clone & Environment Setup
git clone https://github.com/your-username/churn-prediction.git
cd churn-prediction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch the Analytics Dashboard
streamlit run app/app.py
📊 Model PerformanceModelAccuracyF1-ScoreROC-AUCLogistic Regression0.780.740.82Random Forest0.790.760.84Gradient Boosting0.810.790.87
