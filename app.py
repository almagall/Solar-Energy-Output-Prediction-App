import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Define functions
def get_day_of_year(date_value):
    # Convert the integer date to a string
    date_str = str(date_value)
    
    # Convert the string to datetime format
    date_dt = pd.to_datetime(date_str, format='%Y%m%d')
    
    # Extract day of year
    day_of_year = date_dt.dayofyear
    return day_of_year

# Define custom transformers
class DewPointFeature(BaseEstimator, TransformerMixin):
    def __init__(self, temp_index = 0, humidity_index = 1):
        self.temp_index = temp_index
        self.humidity_index = humidity_index
        
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        temp = X_copy[:, self.temp_index]
        humidity = X_copy[:, self.humidity_index]
        dew_point = temp - ((100 - humidity) / 5)
        dew_point = dew_point.reshape(-1, 1)
        return np.hstack([X_copy, dew_point])


class SolarAzimuth(BaseEstimator, TransformerMixin):
    def __init__(self, day_of_year_index = 2, hour_index = 3, latitude_index = 4):
        self.day_of_year_index = day_of_year_index
        self.hour_index = hour_index
        self.latitude_index = latitude_index
        
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        
        day_of_year = X_copy[:, self.day_of_year_index]
        hour = X_copy[:, self.hour_index]
        latitude = X_copy[:, self.latitude_index]
        
        solar_declination = 23.45 * np.sin(np.deg2rad(360 / 365 * (284 + day_of_year)))
        solar_declination = solar_declination.reshape(-1, 1)
        
        hour_angle = 15 * (hour - 12)
        hour_angle = hour_angle.reshape(-1, 1)
        
        latitude_rad = np.deg2rad(latitude)
        latitude_rad = latitude_rad.reshape(-1, 1)
        
        solar_declination_rad = np.deg2rad(solar_declination)
        solar_declination_rad = solar_declination_rad.reshape(-1, 1)
        
        hour_angle_rad = np.deg2rad(hour_angle)
        hour_angle_rad = hour_angle_rad.reshape(-1, 1)
        
        sin_latitude_sin_declination = np.sin(latitude_rad) * np.sin(solar_declination_rad)
        cos_latitude_cos_declination_cos_hour = np.cos(latitude_rad) * np.cos(solar_declination_rad) * np.cos(hour_angle_rad)
        cos_zenith = sin_latitude_sin_declination + cos_latitude_cos_declination_cos_hour
        
        cos_zenith = np.clip(cos_zenith, -1, 1)
        
        solar_zenith = np.rad2deg(np.arccos(cos_zenith))
        solar_zenith = solar_zenith.reshape(-1, 1)
        
        mask = np.ones(X_copy.shape[1], dtype=bool)
        mask[[self.day_of_year_index, self.hour_index]] = False
        X_copy = X_copy[:, mask]
        
        return np.hstack([X_copy, solar_declination, solar_zenith])

def main():
    st.sidebar.title("Alfonso's Portfolio")
    page = st.sidebar.radio('Navigate to:', ['Bio Page', 'Resume Page', 'Project Page'])

    if page == 'Bio Page':
        import bio_page as bio_page
        bio_page.show_bio_page()
    elif page == 'Resume Page':
        import resume_page as resume_page
        resume_page.show_resume_page()
    elif page == 'Project Page':
        import model_page as model_page
        model_page.show_model_page()

if __name__ == "__main__":
    main()