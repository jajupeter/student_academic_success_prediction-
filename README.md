# 🎓 Student Success Prediction App

> 🌟 Predict academic outcomes for STEM students using a machine learning-powered web app.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?logo=streamlit)
![Model](https://img.shields.io/badge/Model-Random%20Forest-green?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Live Demo

🔗 Load App — https://student-academic-success-prediction.streamlit.app/

---

## 📌 Project Overview

This interactive app predicts whether a student in a STEM program will be **academically successful** (above average) or **not successful** (below average), based on 15 personal, academic, and socio-economic parameters.

It’s designed to support:
- ✅ Early warning systems for educators
- ✅ Resource planning for school administrators
- ✅ Data-driven research in educational performance

---

## ❓ Problem Statement

Educational institutions often lack real-time tools to identify students at risk of underperforming. This project builds an ML-powered solution to help identify such students early using interpretable features — enabling proactive interventions.

---

## 📊 Dataset Summary

| Feature                  | Description |
|--------------------------|-------------|
| 📂 Source                | [UCI Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance) |
| 🔢 Samples               | 395 students |
| 🧮 Features Used         | 15 selected (see full list below) |
| 🎯 Target                | Binary (Successful / Not-Successful) |
| ⚠️ Limitation            | Based on Portuguese high school data — may need localization |
| 🔐 Privacy               | No PII; data is anonymized |

---

## 🧠 Methodology

### 🔍 Approach
- Supervised binary classification  
- Label: Pass/Fail based on average grade

### ⚙️ Model
- 🎯 **Random Forest Classifier**
- 🔄 Trained via cross-validation
- 🔢 Encoding via one-hot (categorical features)

### 📏 Metrics
- ✅ Accuracy
- 📉 Precision & Recall
- 📊 Confusion Matrix
- 📌 Feature Importance

---

## 📈 Model Results

| Metric         | Score    |
|----------------|----------|
| 🎯 Accuracy     | ~91.2%   |
| 🔍 Precision    | ~90.4%   |
| 🧠 Recall       | ~89.8%   |
| 🧮 F1-Score     | ~90.1%   |

### 📌 Top Predictors:
- 📚 Study Time
- 🔁 Past Failures
- 👨‍👩‍👧 Parental Education
- 🍷 Alcohol Consumption
- 🚫 School Absences

---

## 💡 App Features

🧠 **Machine Learning**: Trained on UCI data with scikit-learn  
📊 **Interactive UI**: Built with Streamlit sidebar inputs  
🔐 **Local Inference**: Runs offline, data never leaves your device  
⚡ **Fast Predictions**: <1s response time  
📈 **Prediction Probabilities**: Shows confidence levels

---

## 🏢 Business Use Cases

| Stakeholder         | Benefit |
|---------------------|---------|
| 👨‍🏫 **Educators**      | Identify at-risk students early |
| 🏫 **Administrators** | Allocate support/tutoring resources |
| 📊 **Researchers**    | Study effects of interventions |
| 🏛️ **Policy Makers**   | Design data-backed STEM education programs |

---

## 🧰 Tech Stack

| Layer       | Tools Used |
|-------------|------------|
| 📦 Language   | Python 3.10 |
| 🧠 Model      | Scikit-learn (RandomForestClassifier) |
| 🖥️ Interface  | Streamlit |
| 📁 Storage    | Pickle (.pkl) model |
| 📊 Data       | Pandas, NumPy |

---

## 💻 Run the App Locally

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/student-success-prediction.git
cd student-success-prediction
