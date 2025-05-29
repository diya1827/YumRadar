On-Campus Food Recommendation Model - YumRadar (On Campus)

This repository contains the on-campus module of the YumRadar food recommendation system. It is designed to suggest the best eating outlets within the DTU campus based on user preferences. The system uses machine learning to predict suitable food spots such as Raj Soin, Hims, Raydee, Dosa Plaza, Nescafe, and others.

Model Used: Random Forest Classifier (Best accuracy: 82%)
Other Models Tried: Logistic Regression, XGBoost
Techniques Applied:
One-Hot Encoding for categorical variables
SMOTE for handling class imbalance
Train-Test Split and performance evaluation using classification report
Encoded using ColumnTransformer
Deployment Ready: Integrated with a Streamlit frontend for real-time predictions with properly mapped inputs

On-Campus Outlets Covered-
Raj Soin
Hims
Raydee
Dosa Plaza
Nescafe
Mess
Deltech
Udupi
Bistro
Dazzledine

How It Works-
Users provide their preferences such as:
Hunger level
Meal type
Budget
Food preference (Veg/Non-Veg)
Preference for drinks

The model processes this input, encodes the data, and predicts the most relevant food outlet within the campus.

Technologies used include Python, scikit-learn, pandas, imbalanced-learn, Streamlit, and joblib.
