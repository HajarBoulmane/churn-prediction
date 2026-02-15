import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Load model
model = joblib.load("models/GradientBoosting_tuned.pkl")

# Page config
st.set_page_config(
    page_title="Telco Churn AI", 
    page_icon="📉",
    layout="wide"
)

# Add Tailwind CSS + Custom Styles
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {width: 8px;}
    ::-webkit-scrollbar-track {background: #f1f5f9;}
    ::-webkit-scrollbar-thumb {background: #cbd5e1; border-radius: 4px;}
    ::-webkit-scrollbar-thumb:hover {background: #94a3b8;}
    
    /* Animations */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .fade-in {animation: fadeIn 0.5s ease-out;}
    
    @keyframes pulse {
        0%, 100% {opacity: 1;}
        50% {opacity: 0.5;}
    }
    .pulse {animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;}
    
    /* Form styling */
    .stSelectbox, .stNumberInput {
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border-radius: 0.75rem;
        width: 100%;
        transition: all 0.3s;
        font-size: 1.1rem;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 rounded-3xl shadow-2xl p-10 mb-8 fade-in">
        <div class="text-center">
            <h1 class="text-white text-5xl font-bold mb-3">📉 Telco Churn Prediction</h1>
            <p class="text-purple-100 text-xl">AI-Powered Customer Retention Intelligence</p>
            <div class="mt-4 inline-block bg-white/20 backdrop-blur-sm px-6 py-2 rounded-full">
                <span class="text-white font-semibold">Powered by Gradient Boosting ML</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Main layout
col_left, col_right = st.columns([1.2, 1])

with col_left:
    # Input Form
    st.markdown("""
        <div class="bg-white rounded-2xl shadow-xl border border-slate-200 p-6 mb-6 fade-in">
            <h2 class="text-2xl font-bold text-slate-800 mb-4 flex items-center gap-3">
                <span class="bg-gradient-to-r from-purple-600 to-indigo-600 text-white p-2 rounded-lg">👤</span>
                Customer Information
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("customer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📋 Basic Info")
            gender = st.selectbox("Gender", ["Female", "Male"])
            SeniorCitizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x else "No")
            Partner = st.selectbox("Partner", ["Yes", "No"])
            Dependents = st.selectbox("Dependents", ["Yes", "No"])
            tenure = st.number_input("Tenure (months)", 0, 100, 12)
            
            st.markdown("##### 📞 Phone Services")
            PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
            MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
        
        with col2:
            st.markdown("##### 🌐 Internet & Add-ons")
            InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
            OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
            DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
            TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
            StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
            StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        
        st.markdown("---")
        st.markdown("##### 💳 Billing Information")
        
        col3, col4 = st.columns(2)
        with col3:
            Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
        with col4:
            PaymentMethod = st.selectbox("Payment Method", [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ])
        
        col5, col6 = st.columns(2)
        with col5:
            MonthlyCharges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
        with col6:
            TotalCharges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1000.0)
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 Predict Churn Risk", use_container_width=True)

with col_right:
    # Placeholder for results
    st.markdown("""
        <div class="bg-gradient-to-br from-slate-50 to-blue-50 rounded-2xl shadow-xl border border-slate-200 p-8 text-center fade-in" style="min-height: 400px; display: flex; align-items: center; justify-content: center;">
            <div>
                <div class="text-6xl mb-4">🎯</div>
                <h3 class="text-2xl font-semibold text-slate-700 mb-2">Ready to Predict</h3>
                <p class="text-slate-500">Fill in customer details and click "Predict Churn Risk"</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---------- PREDICTION ----------
if submitted:
    with col_right:
        # Clear placeholder
        st.empty()
        
        # Create DataFrame
        customer_df = pd.DataFrame([{
            "gender": gender,
            "SeniorCitizen": SeniorCitizen,
            "Partner": Partner,
            "Dependents": Dependents,
            "tenure": tenure,
            "PhoneService": PhoneService,
            "MultipleLines": MultipleLines,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "PaymentMethod": PaymentMethod,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges
        }])
        
        # Predict
        pred_proba = model.predict_proba(customer_df)[0][1]
        pred_label = int(pred_proba > 0.5)
        
        # Risk classification
        if pred_proba < 0.3:
            risk = "LOW RISK"
            risk_color = "#10b981"
            bg_gradient = "from-emerald-50 to-teal-50"
            icon = "✅"
        elif pred_proba < 0.6:
            risk = "MEDIUM RISK"
            risk_color = "#f59e0b"
            bg_gradient = "from-amber-50 to-orange-50"
            icon = "⚠️"
        else:
            risk = "HIGH RISK"
            risk_color = "#ef4444"
            bg_gradient = "from-red-50 to-pink-50"
            icon = "🚨"
        
        # Results Container
        st.markdown(f"""
            <div class="bg-gradient-to-br {bg_gradient} rounded-2xl shadow-2xl border-2 border-{risk.split()[0].lower()}-200 p-8 fade-in">
                <div class="text-center mb-6">
                    <div class="text-7xl mb-3">{icon}</div>
                    <h2 class="text-3xl font-bold" style="color: {risk_color};">{risk}</h2>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Metrics
        st.markdown("<br>", unsafe_allow_html=True)
        metricA, metricB = st.columns(2)
        
        with metricA:
            st.markdown(f"""
                <div class="bg-white rounded-xl shadow-lg p-6 text-center border-l-4" style="border-color: {risk_color};">
                    <div class="text-sm text-slate-600 uppercase tracking-wide mb-2">Churn Probability</div>
                    <div class="text-4xl font-bold" style="color: {risk_color};">{pred_proba:.1%}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with metricB:
            st.markdown(f"""
                <div class="bg-white rounded-xl shadow-lg p-6 text-center border-l-4 border-slate-400">
                    <div class="text-sm text-slate-600 uppercase tracking-wide mb-2">Prediction</div>
                    <div class="text-4xl font-bold text-slate-800">{"CHURN" if pred_label == 1 else "STAY"}</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Gauge Chart
        st.markdown("<br>", unsafe_allow_html=True)
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pred_proba * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Churn Risk Score", 'font': {'size': 24, 'color': '#1e293b'}},
            number={'suffix': "%", 'font': {'size': 48}},
            gauge={
                'axis': {'range': [None, 100], 'tickwidth': 2, 'tickcolor': "#cbd5e1"},
                'bar': {'color': risk_color},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#e2e8f0",
                'steps': [
                    {'range': [0, 30], 'color': '#d1fae5'},
                    {'range': [30, 60], 'color': '#fed7aa'},
                    {'range': [60, 100], 'color': '#fecaca'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        ))
        
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={'color': "#1e293b", 'family': "Arial"},
            height=300,
            margin=dict(l=20, r=20, t=60, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Action Message
        if pred_label == 1:
            st.markdown("""
                <div class="bg-red-100 border-l-4 border-red-500 p-4 rounded-lg">
                    <p class="text-red-800 font-semibold">🚨 <strong>Action Required:</strong> High churn risk detected. Consider retention strategies.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="bg-emerald-100 border-l-4 border-emerald-500 p-4 rounded-lg">
                    <p class="text-emerald-800 font-semibold">✅ <strong>Good News:</strong> Customer likely to stay. Continue current engagement.</p>
                </div>
            """, unsafe_allow_html=True)

# Explainability Section
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("🧠 **How Does This Model Work?**", expanded=False):
    st.markdown("""
        <div class="bg-gradient-to-r from-purple-50 to-blue-50 p-6 rounded-xl">
            <h4 class="text-lg font-bold text-slate-800 mb-3">Model Insights</h4>
            <p class="text-slate-700 leading-relaxed mb-4">
                Our Gradient Boosting model analyzes <strong>19 customer features</strong> including demographics, 
                service usage, and billing patterns to predict churn probability.
            </p>
            <h5 class="font-semibold text-slate-800 mb-2">🔍 Key Risk Factors:</h5>
            <ul class="list-disc list-inside text-slate-700 space-y-1 ml-4">
                <li><strong>Contract Type:</strong> Month-to-month contracts show higher churn</li>
                <li><strong>Tenure:</strong> Newer customers (< 12 months) are more likely to leave</li>
                <li><strong>Internet Service:</strong> Fiber optic users have higher churn rates</li>
                <li><strong>Monthly Charges:</strong> Higher bills correlate with increased churn</li>
                <li><strong>Payment Method:</strong> Electronic check users churn more frequently</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="text-center text-slate-400 py-8 mt-12 border-t border-slate-200">
        <p>Powered by Gradient Boosting Machine Learning • Built with Streamlit & Tailwind CSS</p>
    </div>
""", unsafe_allow_html=True)