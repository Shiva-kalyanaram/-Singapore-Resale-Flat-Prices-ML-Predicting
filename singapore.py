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








# import numpy as np
# import pickle
# import streamlit as st
# import pandas as pd
# import json
#
# # with open('XGR.pkl', 'rb') as f:
# #     xgr_model = pickle.load(f)
#
# with open (r'Category_Columns_Encoded_Data.json', 'r') as f:
#     data = json.load(f)
#
#     st.set_page_config(page_title="Singapore Resale Flat Prices Predicting",
#                        page_icon="",
#                        layout="wide",
#                        initial_sidebar_state="expanded",
#                        menu_items=None)
#
#     st.title(":red[Singapore Resale] :blue[Flat Prices] :orange[Prediction]")
#
# col1, col2 = st.columns(2, gap= 'large')
#
# with col1:
#     min_month = 1
#     max_month = 12
#
#     # Slider for selecting the month
#     selected_month = st.slider("Select the Item Month", min_value=min_month, max_value=max_month, value=min_month,
#                                step=1)
#
#     town = st.selectbox('Select the **Town**', data['town_before'])
#
#     flat_type = st.selectbox('Select the **Flat Type**', data['flat_type_before'])
#
#     block = st.selectbox('Select the **Block**', data['block_before'])
#
#     street_name = st.selectbox('Select the **Street Name**', data['street_name_before'])
#
# with col2:
#     floor_area_sqm = st.number_input('Select the **floor_area_sqm**', )
#
#     flat_model = st.selectbox('Select the **flat_model**', data['flat_model_before'])
#
#     lease_commence_date	=st.number_input('Enter the **Lease Commence Year**', min_value = 1966, max_value= 2022, value = 2017.0 )
#
#     end_of_lease	= st.number_input('Select the **Remainig Lease**', )
#
#     year = st.year_input("Select the Year which you want**", dt.year(), min_value = dt.year)
#
#     min_storey = st.number_input('Select the **min_storey**', )
#
#     max_storey = st.number_input('Select the **max_storey**', )


#
#
# storey = storey_range.split(' TO ')
#
# if remaining_lease == 'Not Specified':
#     is_remaining_lease = 0
# else:
#     is_remaining_lease = 1
#
# test_data = [[date.month, town, flat_type, block, street_name, floor_area_sqm, flat_model, lease_commence_date,
#             end_of_lease, date.year, min_storey, max_storey]]
#
# st.markdown('Click below button to predict the **Flat Resale Price**')
# prediction = st.button('**Predict**')
#
# if prediction and test_data:
#   st.markdown(f"### :bule[Flat Resale Price is] :green[$ {round(regression_model(test_data),3)}]")

# def prediction():
#     st.subheader('Resale Price Prediction')
#
#     flat_type = st.selectbox('Flat Type', list(flat_type_mapping.keys()))
#     numerical_flat_type = flat_type_mapping[flat_type]
#
#     storey_range_options = list(storey_range_mapping.keys())
#     selected_storey_range = st.selectbox('Storey Range', storey_range_options)
#     numerical_storey_range = storey_range_mapping[selected_storey_range]
#
#     flat_model = st.selectbox('Flat model', list(flat_model_mapping.keys()))
#     numerical_flat_model = flat_model_mapping[flat_model]
#
#     floor_area_sqm = st.number_input('Floor Area (sqm)')
#
#     lease_commence_date = st.number_input('Lease Commence Date', min_value=1960, value=1980)
#     lease_remain_years = st.number_input('Lease Remain Years', min_value=0, value=99)
#
#     if st.button('Submit'):
#         input_data = [[numerical_flat_type, numerical_storey_range, floor_area_sqm, numerical_flat_model, lease_commence_date,
#                        lease_remain_years]]
#         prediction = rf_model.predict(input_data)
#         # st.subheader('Prediction')
#         st.markdown(
#             f'<p style="color: green; font-size: xx-large;">The predicted resale price is: ${prediction[0]:,.2f}</p>',
#             unsafe_allow_html=True)
#         # st.write(f'The predicted resale price is: ${prediction[0]:,.2f}')
#
#
# def about_project():
#     st.subheader('About Project')
#     # Add information about your project here
#
# def main():
#     st.title('Singapore Housing flats Resale Price Prediction')
#
#     # Create a radio button for navigation
#     menu_selection = st.sidebar.radio('Menu', ['Main', 'About Project', 'Prediction'])
#
#     if menu_selection == 'Main':
#         st.subheader('Welcome to the Main Menu')
#         # Add content for the main menu
#
#     elif menu_selection == 'About Project':
#         about_project()
#
#     elif menu_selection == 'Prediction':
#         prediction()
#
#
# if __name__ == '__main__':
#     main()











# import numpy as np
# import pickle
# import streamlit as st
# import pandas as pd
#
# with open('rf_model1.pkl', 'rb') as f:
#     rf_model = pickle.load(f)
#
# # Mapping of flat types
# flat_type_mapping = {
#     '1 ROOM': 0.0,
#     '2 ROOM': 1.0,
#     '3 ROOM': 2.0,
#     '4 ROOM': 3.0,
#     '5 ROOM': 4.0,
#     'EXECUTIVE': 5.0,
#     'MULTI GENERATION': 6.0
# }
# storey_range_mapping = {
#     '10 TO 12': 11.0,
#     '04 TO 06': 5.0,
#     '07 TO 09': 8.0,
#     '01 TO 03': 2.0,
#     '13 TO 15': 14.0,
#     '19 TO 21': 20.0,
#     '16 TO 18': 17.0,
#     '25 TO 27': 26.0,
#     '22 TO 24': 23.0,
# }
#
# flat_model_mapping ={
# 'IMPROVED': 3,
#  'MODEL A, A2 & MODEL A-MAISONETTE': 5,
#  'NEW GENERATION': 9,
#  'STANDARD & SIMPLIFIED': 12,
#  'MODEL A & MODEL A-MAISONETTE': 4,
#  'Premium Apartment': 11,
#  'Apartment': 1,
#  'Standard': 13,
#  'Maisonette': 6,
#  'Others': 10,
#  'DBSS': 2,
#  'Adjoined flat': 0,
#  'Model A-Maisonette': 7,
#  'Type S1, S2': 15,
#  'Terrace': 14,
#  'Multi Generation': 8
# }
#
# def main():
#     st.title('Resale Price Prediction')
#
#     # User input form
#     st.sidebar.header('User Input')
#     flat_type = st.sidebar.selectbox('Flat Type', list(flat_type_mapping.keys()))
#
#     # Map the selected flat type to its numerical representation
#     numerical_flat_type = flat_type_mapping[flat_type]
#
#     storey_range_options = list(storey_range_mapping.keys())
#     selected_storey_range = st.sidebar.selectbox('Storey Range', storey_range_options)
#
#     # Map the selected storey range to its numerical representation
#     numerical_storey_range = storey_range_mapping[selected_storey_range]
#
#     flat_model = st.sidebar.selectbox('Flat model', list(flat_model_mapping.keys()))
#     # Map the selected flat type to its numerical representation
#     numerical_flat_model = flat_model_mapping[flat_model]
#
#     floor_area_sqm = st.sidebar.number_input('Floor Area (sqm)')
#
#     lease_commence_date = st.sidebar.number_input('Lease Commence Date', min_value=1960, value=1980)
#     lease_remain_years = st.sidebar.number_input('Lease Remain Years', min_value=0, value=99)
#
#     # Add a submit button
#     if st.sidebar.button('Submit'):
#         # Make prediction
#         input_data = [[numerical_flat_type, numerical_storey_range, floor_area_sqm, numerical_flat_model, lease_commence_date,
#                        lease_remain_years]]
#         prediction = rf_model.predict(input_data)
#
#         # Display the prediction
#         st.subheader('Prediction')
#         st.write(f'The predicted resale price is: ${prediction[0]:,.2f}')
#
#
# if __name__ == '__main__':
#     main()

