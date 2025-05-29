import pandas as pd 
import joblib 
import streamlit as st

print(st.__version__)

# Load model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

# Define options
hunger_options = ['Somewhat Hungry', 'Very Hungry']
meal_options = ['Breakfast', 'Lunch', 'Evening Refreshments', 'Dinner']
budget_options = ['<50', '5-100', '100-150', '150-200', '200-500', '500-1000', '1000+']
drink_options = ['Yes', 'No']
food_options = ['Veg', 'Non-Veg']
travel_options = ['<5 min', '5-10', '10-15', '15-20', '20-25', '25-30', '30+']

# 🔁 Add label-to-name mapping (replace with your actual data)
place_label_map = {
    6: 'hungry yak/dtu cafe',
    8: 'yellow bowl',
    4: 'baozi',
    3: 'Rohini Market cafes',
    9: 'zomato/swiggy/online mode',
    1: 'Mcd, KFC other fast food outlets',
    10: 'Bunker house/Yogit Mess/Apsara',
    7: 'street food from front of the campus',
    5: 'crazy crisp',
    2: 'Dillicious/Madras Cafe'
    # Add more if needed
}

st.title("Restaurant Place Recommender 🍽️")

# Input form
with st.form("user_input_form"):
    hunger_level = st.selectbox("1. Hunger Level", hunger_options)
    meal_type = st.selectbox("2. Meal Type", meal_options)
    budget = st.selectbox("3. Budget Range (₹)", budget_options)
    drinks = st.selectbox("4. Prefer Drinks?", drink_options)
    food_type = st.selectbox("5. Food Preference", food_options)
    travel_time = st.selectbox("6. Travel Time", travel_options)

    submit = st.form_submit_button("Predict Place")

# Handle prediction
if submit:
    # Map options to integers (must match training data)
    hunger_map = {'Somewhat Hungry': 0, 'Very Hungry': 1}
    meal_map = {'Breakfast': 0, 'Lunch': 1, 'Evening Refreshments': 2, 'Dinner': 3}
    drink_map = {'No': 0, 'Yes': 1}
    food_map = {'Veg': 0, 'Non-Veg': 1}

    # Replace user input with numerical values
    input_df = pd.DataFrame([{
        'hunger_level_': hunger_map[hunger_level],
        'frequent_meal_type_': meal_map[meal_type],
        'budget_range': budget,
        'prefer_dinks_': drink_map[drinks],
        'prefer_food_type_': food_map[food_type],
        'travel_time_range': travel_time
    }])

    # Transform and predict
    input_encoded = encoder.transform(input_df)
    prediction = model.predict(input_encoded)

    # 🧠 Map predicted label to place name
    predicted_label = prediction[0]
    place_name = place_label_map.get(predicted_label, "Unknown Place")

    st.success(f"📍 Recommended Place: **{place_name}**")






