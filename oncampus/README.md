# On-Campus Food Recommendation Model - YumRadar (On Campus)

This repository contains the on-campus module of the YumRadar food recommendation system designed to suggest the best eating outlets within the DTU campus based on user preferences. It leverages machine learning to predict suitable food spots like Raj Soin, Hims, Raydee, Dosa Plaza, Nescafe, and more.

## Description

- Model Used: Random Forest Classifier (Best accuracy: 82%)
- Other Models Tried: Logistic Regression, XGBoost
- Techniques Applied:
  - One-Hot Encoding for categorical variables
  - SMOTE for handling class imbalance
  - Train-Test Split and performance evaluation using classification_report
  - Encoded using ColumnTransformer
- Deployment Ready: Integrated with a Streamlit frontend for real-time prediction with mapped inputs

## On-Campus Outlets Covered

- Raj Soin  
- Hims  
- Raydee  
- Dosa Plaza  
- Nescafe  
- Mess  
- Deltech  
- Udupi  
- Bistro  
- Dazzledine  

## How It Works

Users provide their preferences like:
- Hunger level
- Meal type
- Budget
- Food preference (Veg/Non-Veg)
- Willingness for drinks

The model processes this input, encodes it, and predicts the most relevant food outlet on campus.

---

> 🔧 Built with Python, Scikit-learn, Pandas, Imbalanced-learn, Streamlit, and Joblib.

