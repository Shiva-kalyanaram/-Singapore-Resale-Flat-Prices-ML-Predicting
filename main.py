import numpy as np
import pickle
import streamlit as st
import pandas as pd
import json
import datetime as dt

with open('XGR.pkl', 'rb') as f:
    xgr_model = pickle.load(f)

with open(r'Category_Columns_Encoded_Data.json', 'r') as f:
    data = json.load(f)

st.set_page_config(
    page_title="Singapore Resale Flat Prices Predicting",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

st.title(":red[Singapore Resale] :blue[Flat Prices] :orange[Prediction]")

col1, col2 = st.columns(2, gap='large')

with col1:
    min_month = 1
    max_month = 12

    # Slider for selecting the month
    selected_month = st.slider("Select the Item Month", min_value=min_month, max_value=max_month, value=min_month,
                               step=1)

    town = st.selectbox('Select the **Town**', data['town_before'])

    flat_type = st.selectbox('Select the **Flat Type**', data['flat_type_before'])

    block = st.selectbox('Select the **Block**', data['block_before'])

    street_name = st.selectbox('Select the **Street Name**', data['street_name_before'])

with col2:
    floor_area_sqm = st.number_input('Select the **floor_area_sqm**', value=60.0, min_value=28.0, max_value=173.0,
                                     step=1.0)

    flat_model = st.selectbox('Select the **flat_model**', data['flat_model_before'])

    lease_commence_date = st.number_input('Enter the **Lease Commence Year**', min_value=1966, max_value=2022,
                                          value=2017)

    end_of_lease = st.number_input('Select the **end_of_lease**', value=0, min_value=0, max_value=3000)

    year = st.number_input("Select the transaction Year which you want**", min_value=1990, max_value=2023, value=dt.datetime.now().year)

    min_storey = st.number_input('Select the **min_storey**', value=0, min_value=0, max_value=100)

    max_storey = st.number_input('Select the **max_storey**', value=10, min_value=0, max_value=100)

st.markdown('Click below button to predict the **Flat Resale Price**')
prediction = st.button('**Predict**')

# Convert categorical values to corresponding encoded values
town_encoded = data['town_before'].index(town)
flat_type_encoded = data['flat_type_before'].index(flat_type)
block_encoded = data['block_before'].index(block)
street_name_encoded = data['street_name_before'].index(street_name)
flat_model_encoded = data['flat_model_before'].index(flat_model)

# Prediction logic
test_data = [
    selected_month,
    town_encoded,  # Use encoded value
    flat_type_encoded,  # Use encoded value
    block_encoded,  # Use encoded value
    street_name_encoded,  # Use encoded value
    floor_area_sqm,
    flat_model_encoded,  # Use encoded value
    lease_commence_date,
    end_of_lease,  # Assuming you have 'remaining_lease_before' in your data
    year,
    min_storey,
    max_storey,
]

if prediction:
    # Perform prediction
    test_data_array = np.array([test_data], dtype=np.float32)  # Convert to 2D array with float data type

    predicted_price = xgr_model.predict(test_data_array)  # Assuming your model's predict method takes a 2D array

    # Display predicted price
    st.markdown(f"### :blue[Flat Resale Price is] :green[$ {round(predicted_price[0], 3)}]")
