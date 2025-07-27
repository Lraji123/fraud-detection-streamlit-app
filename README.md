# 🛡️ Fraud Detection Web App

An interactive web application built with Streamlit to detect fraudulent transactions using machine learning.

## 🚀 Features
- Upload transaction data or enter manually
- Predicts whether a transaction is fraudulent or not
- Visualizations for model insights and data distribution
- Built with Logistic Regression (customizable with other models)

## 📊 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, Scikit-learn
- **ML Model:** Logistic Regression
- **Visualization:** Matplotlib, Seaborn

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fraud-detection-streamlit-app.git
cd fraud-detection-streamlit-app
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
🌐 Live Demo
Click here to open the app

🧠 Model Info
The app uses a simple Logistic Regression model trained on a public credit card fraud dataset with a 94% accuracy. You can swap it with other classifiers like Random Forest or XGBoost.

📁 File Structure
pgsql
Copy
Edit
fraud-detection-streamlit-app/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── utils.py  (if any helper functions)
📄 License
This project is open source and free to use under the MIT License.

