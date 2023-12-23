# -Singapore-Resale-Flat-Prices-ML-Predicting

# Singapore Resale Flat Price Prediction

## Introduction
This project aims to construct a machine learning model and implement it as a user-friendly online application to provide accurate predictions about the resale values of apartments in Singapore. The prediction model is based on past transactions involving resale flats, aiming to assist both future buyers and sellers in evaluating the worth of a flat after it has been previously resold. Resale prices are influenced by various criteria, including location, type of apartment, square footage, and lease length. The predictive model helps customers by providing an expected resale price based on these criteria.

## Domain
Real Estate

## Prerequisites
- Python -- Programming Language
- pandas -- Python Library for Data Visualization
- numpy -- Fundamental Python package for scientific computing
- streamlit -- Python framework to build and share machine learning and data science web apps
- scikit-learn -- Machine Learning library for Python

## Data Source
- [Singapore Resale Flat Prices Dataset](https://beta.data.gov.sg/collections/189/view)

## Project Workflow
1. Merge the five distinct CSV files representing specific time periods into a unified dataset.
2. Convert the data into a format appropriate for analysis, perform cleaning, and pre-process the data.
3. Extract relevant features, including town, flat type, storey range, floor area, flat model, and lease commence date.
4. Create additional features that may enhance prediction accuracy.
5. Construct a machine learning regression model using the decision tree regressor to forecast the continuous variable 'resale_price'.
6. Develop a Streamlit webpage allowing users to input values for each column and obtain the expected resale_price value for flats in Singapore.

## Using the App
### Resale Price Prediction
1. Select the "Predictions" option menu.
2. Fill in the required information like which are available on streamlit:
   - Street Name
   - Block Number
   - Floor Area (Per Square Meter)
   - Lease Commence Date
   - Storey Range
3. Click the "PREDICT RESALE PRICE" button.
4. The app will display the predicted resale price based on the provided information.


