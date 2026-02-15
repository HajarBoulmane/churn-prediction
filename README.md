

# 📊 TelcoChurn: Enterprise Retention Analytics
**Predicting customer attrition with high-precision Gradient Boosted Trees.**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Model: Gradient Boosting](https://img.shields.io/badge/Model-Gradient%20Boosting-green.svg)](https://scikit-learn.org/)

---

## 🎯 Business Value
Customer churn is a multi-billion dollar challenge. This project provides an end-to-end ML pipeline to:
* **Quantify Risk:** Assign churn probability scores to every customer.
* **Identify Drivers:** Understand why customers leave (Contract type, Monthly charges, etc.).
* **Enable Action:** A Streamlit-based interface for non-technical teams to run real-time predictions.

---

## 🏗️ Project Architecture
The repository follows a modular "Production-Lite" structure to separate data logic from the user interface.

### **The ML Pipeline**
1. **Preprocessing:** Feature scaling and categorical encoding (Label/One-Hot).
2. **Modeling:** Comparative analysis of Logistic Regression, Random Forest, and **Gradient Boosting**.
3. **Optimization:** Hyperparameter tuning via `GridSearchCV` for maximized ROC-AUC.
4. **Deployment:** Model serialization via `joblib` and interactive serving via **Streamlit**.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Libraries** | Scikit-Learn, Pandas, NumPy, Plotly |
| **Persistence** | Joblib |
| **Frontend** | Streamlit |

---

## 🗂 Project Structure
```bash
churn-prediction/
├── data/               # Raw and processed datasets
├── models/             # Serialized .pkl artifacts
├── src/                # Core ML logic
│   ├── preprocess.py   # Cleaning & Transformation
│   ├── train.py        # Model training scripts
│   └── evaluate.py     # Metrics & Visualizations
├── app/
│   └── app.py          # Streamlit UI Dashboard
└── requirements.txt    # Dependency manifest
```
🚀 Getting Started
1. Environment Setup

# Clone the repository
git clone [https://github.com/HajarBoulmane/churn-prediction.git](https://github.com/HajarBoulmane/churn-prediction.git)
cd churn-prediction

# Initialize virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate

# Install dependencies
1. pip install -r requirements.txt
2. Launch the Application
 ```Bash
streamlit run app/app.py
```
Note: The app will be available at http://localhost:8501
