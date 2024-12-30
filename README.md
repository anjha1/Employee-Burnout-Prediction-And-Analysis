# Employee Burnout Prediction and Analysis

This project predicts the **Employee Burnout Rate** based on input features such as `Designation`, `Resource Allocation`, and `Mental Fatigue Score`. The web application allows users to input these details and get a predicted burn rate using a machine learning model.

## Live Demo

You can view and interact with the live project [here](https://employee-burnout-prediction-and-analysis.onrender.com/).

---

## Project Overview

### Problem Statement
Employee burnout is a critical issue in workplaces, leading to decreased productivity and increased employee turnover. Predicting the burnout rate can help organizations take proactive measures to mitigate its impact. This project aims to develop a system to analyze and predict the burnout rate of employees using machine learning models.

---

### System Approach

#### System Requirements:
- Python 3.x
- Flask (for web application)
- Scikit-learn (for building the ML model)
- NumPy and Pandas (for data preprocessing)
- HTML/CSS (for the front-end)

#### Libraries Required:
- `flask`
- `numpy`
- `pandas`
- `scikit-learn`
- `pickle`

---

### Algorithm & Deployment

1. **Data Preparation**:
   - The dataset was sourced from Kaggle and preprocessed for training.
   - Features used: `Designation`, `Resource Allocation`, and `Mental Fatigue Score`.
   - Target variable: `Burn Rate`.

2. **Model Training**:
   - The dataset was split into training and testing datasets.
   - Machine Learning algorithms were applied, and the best-performing model was selected.

3. **Model Deployment**:
   - The trained model was serialized using `pickle`.
   - A Flask web application was created for user interaction.

4. **User Interface**:
   - A simple and intuitive form allows users to input data for predictions.
   - The prediction is displayed directly on the web page.

5. **Hosting**:
   - The application is hosted on [Render](https://render.com/) for live demonstration.

---

### Results
- The model provides accurate predictions of employee burnout rates based on the input features.
- The web application enables easy interaction for real-world use.

---

### Future Scope
- Incorporate additional features to improve model accuracy.
- Add data visualization to highlight trends and insights about employee burnout.
- Expand the model to predict other HR metrics, such as employee turnover.

---

### How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/anjha1/Employee-Burnout-Prediction-And-Analysis.git
