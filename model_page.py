import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

def show_model_page():
    def get_day_of_year(date_value):
        # Convert the integer date to a string
        date_str = str(date_value)
    
        # Convert the string to datetime format
        date_dt = pd.to_datetime(date_str, format='%Y%m%d')
    
        # Extract day of year
        day_of_year = date_dt.dayofyear
        return day_of_year
    

    st.title('Solar Energy Output Prediction')
    st.header('Overview:')
    st.write("""
    Data was collected over 14 months across 12 photo-voltaic (PV) solar panel sites. This tool leverages machine learning (XG Boost) to estimate the power output of horizontal solar panels based on weather, geographical, and time data.

    By analyzing data from 12 different locations, the model aims to predic solar power output (Poly Power in Watts) without needing direct irradiation measurements. This tool is designed to help optimize solar energy utilization and improve forecasting for solar energy projects.
    """)
    performance_data = {
        'Model': ['Random Forest', 'XGBoost', 'MLP (Neural Network)'],
        'MAE': [3.12, 3.10, 3.46],
        'RMSE': [4.38, 4.37, 4.63],
        'R²': [0.62, 0.62, 0.58]
    }
    
    performance_df = pd.DataFrame(performance_data)
    st.write("### Model Performance")
    st.table(performance_df)
    st.write('XGBoost was ultimately chosen as the final model due to it having the highest R² and lowest RMSE and MAE.')
    st.write('')
    
    st.header('Input:')

    # Select Boxes
    latitude_options = [20.89, 26.98, 33.9, 38.16, 38.82, 38.95, 40.67, 41.13, 41.15, 44.89, 47.11, 47.52]
    season_options = ['Spring', 'Summer', 'Fall', 'Winter']

    # Input fields
    date = st.number_input('Date (YYYYMMDD):', min_value=20170101, max_value=20241231, step=1)
    hour = st.slider('Hour:', min_value=10, max_value=15, value=12, step=1)
    latitude = st.selectbox('Latitude:', latitude_options)
    humidity = st.number_input('Humidity Level:', min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    ambient_temp = st.number_input('Ambient Temperature:', min_value=-20.0, max_value=80.0, value=30.0)
    visibility = st.slider('Visibility:', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    cloud_ceiling = st.number_input('Cloud Ceiling:', min_value=0, max_value=730, value=80, step=1)
    season = st.selectbox('Season:', season_options)

    # Transformation
    day_of_year = get_day_of_year(date)

    # Input Data
    input_data = pd.DataFrame({
        'AmbientTemp': [ambient_temp],
        'Humidity': [humidity],
        'DayOfYear': [day_of_year],
        'Hour': [hour],
        'Latitude': [latitude],
        'Visibility': [visibility],
        'Cloud.Ceiling': [cloud_ceiling],
        'Season': [season]
    })

    # Load Model
    pipeline = joblib.load('xgb_pipeline.pkl')

    # Prediction
    prediction = pipeline.predict(input_data)

    # Display Prediction
    st.write('')
    st.markdown(
        f"""
        <div style='background-color: #d4edda; padding: 10px; border-radius: 5px; border: 1px solid #c3e6cb;'>
            <h3 style='color: #155724;'>Predicted Value:</h3>
            <h3 style='color: #155724;'>{prediction[0]:.2f} Watts</h3>
        </div>
        """,
        unsafe_allow_html=True
    )