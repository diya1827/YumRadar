# Off-Campus Food Recommendation Model - YumRadar (Off Campus)

This repository contains the off-campus module of the YumRadar food recommendation system. It recommends the best eating places around the DTU campus based on user preferences. The system predicts suitable food outlets such as Hungry Yak/DTU Cafe, Yellow Bowl, Baozi, Rohini Market Cafes, and others.

## Overview

- Model Used: Random Forest Classifier (Best accuracy: 82%)
- Other Models Tried: Logistic Regression, XGBoost
- Techniques Applied:
  - One-Hot Encoding for categorical variables
  - SMOTE for handling class imbalance
  - Train-Test Split and performance evaluation using classification report
  - Encoded using ColumnTransformer
- Deployment Ready: Integrated with a Streamlit frontend for real-time predictions with properly mapped inputs

## Off-Campus Outlets Covered

- Hungry Yak / DTU Cafe  
- Yellow Bowl  
- Baozi  
- Rohini Market Cafes  
- Zomato / Swiggy / Online Mode  
- Street Food from Front of the Campus  
- Crazy Crisp  
- McDonald’s, KFC, and Other Fast Food Outlets  
- Dillicious / Madras Cafe  
- Bunker House / Yogit Mess / Apsara  

## How It Works

Users provide their preferences such as:

- Hunger level  
- Meal type  
- Budget  
- Food preference (Veg/Non-Veg)  
- Preference for drinks  
- Travel time range  

The model processes this input, encodes the data, and predicts the most relevant off-campus food outlet nearby.

Technologies used include Python, scikit-learn, pandas, imbalanced-learn, Streamlit, and joblib.

