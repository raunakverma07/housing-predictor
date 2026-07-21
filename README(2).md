<div align="center">

# 🏠 Housing Price Predictor

### AI-powered house price estimation, built with Streamlit & Scikit-learn

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**[🚀 Live Demo](https://housing-app-g2v4.onrender.com/)** &nbsp;·&nbsp; **[📂 Repository](https://github.com/raunakverma07/housing-predictor)**

</div>

---

## 📌 Overview

**Housing Price Predictor** is a machine learning web application that estimates house prices based on key property features — area, bedrooms, bathrooms, stories, parking, and more. It uses a **regression model** trained on housing data and is deployed with an interactive, premium-styled **Streamlit** interface.

> Enter your property details, hit predict, and get an instant price estimate — no coding required.

🔗 **Try it live:** [housing-app-g2v4.onrender.com](https://housing-app-g2v4.onrender.com/)

---

## ✨ Features

- 🎯 **Instant Predictions** — Real-time house price estimation from a trained ML model
- 🖥️ **Modern, Premium UI** — Custom-styled Streamlit interface with gradient accents
- 🧠 **Regression Model** — Trained using Scikit-learn on structured housing data
- 🧩 **Simple Input System** — Clean dropdowns and number fields instead of raw binary encoding
- ⚡ **Cached Model Loading** — Faster performance using Streamlit's resource caching
- 📱 **Responsive Layout** — Works well on desktop and mobile browsers

---

## 🛠️ Tech Stack

| Category | Tool / Library |
|---|---|
| Language | Python 3.9+ |
| Web Framework | [Streamlit](https://streamlit.io/) |
| ML Library | [Scikit-learn](https://scikit-learn.org/) |
| Model Serialization | [Joblib](https://joblib.readthedocs.io/) |
| Data Handling | Pandas |
| Deployment | Render |

---

## 📂 Project Structure

```
housing-predictor/
│
├── app.py                   # Streamlit web application
├── my_housing_model.pkl     # Pre-trained regression model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Model Inputs

The model uses the following 11 features to predict house price:

| Feature | Description |
|---|---|
| `area` | Total area of the property (sq. ft) |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `stories` | Number of floors/stories |
| `mainroad` | Main road access (Yes/No) |
| `guestroom` | Guest room availability (Yes/No) |
| `basement` | Basement availability (Yes/No) |
| `airconditioning` | Air conditioning present (Yes/No) |
| `parking` | Number of parking spaces |
| `prefarea` | Located in a preferred area (Yes/No) |
| `furnishingstatus` | Furnished / Semi-Furnished / Unfurnished |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/raunakverma07/housing-predictor.git
cd housing-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 📦 requirements.txt

```
streamlit
scikit-learn
pandas
joblib
```

---

## 🔮 Future Improvements

- [ ] Add data visualization for price trends
- [ ] Support CSV bulk predictions
- [ ] Add model explainability (SHAP values)
- [ ] Add price range confidence interval

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---

<div align="center">

⭐ If you found this project useful, consider giving it a star on GitHub!

### Made by Raunak Verma

[![About Me](https://img.shields.io/badge/🔗_Know_More_About_Me-raunakverma.vercel.app-6366f1?style=for-the-badge)](https://raunakverma.vercel.app)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raunakverma07)

</div>
