import streamlit as st
from io import BytesIO
import pandas as pd

from src.ts_forecast_chronos import ChronosForecast
from src.ts_forecast_prophet import ProphetForecast
from src.utils import plot_series, map_feature

uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    list_columns = df.columns.to_list()



    solution = st.sidebar.radio(
        "Select the solution want to try 👉",
        key="Prophet",
        options=["Prophet", "Chronos"],
    )

    
    prediction_length = st.slider("Select a range of prediction_length", 1, 200, 1)

    
    if solution == 'Chronos':
      selected_feature = st.sidebar.selectbox(
          "Select feature name?",
          list_columns,
          index=None,
      )
      if selected_feature is not None:
        chronos = ChronosForecast(df=df, feature_name=selected_feature)
        chronos.chronos_predict(prediction_length=prediction_length)
        fig, ax = plot_series(chronos.timeseries, chronos.forecast_index, chronos.median, chronos.low, chronos.high)
        st.pyplot(fig)
    else:
      series_feature_name = None
      time_feature_name = None
      freq = st.radio("Select the Frequency Time Range?", key='M', options = ["M", "D", 'Y'], horizontal=True)
      time_feature_name = st.sidebar.selectbox(
          "Select feature which is time?",
          list_columns,
          index=None,
      )
      if time_feature_name is not None:
        list_columns.remove(time_feature_name)
        series_feature_name = st.sidebar.selectbox(
            "Select feature which is value?",
            list_columns,
            index=None,
        )

      if (time_feature_name is not None)&(series_feature_name is not None):
        df = map_feature(df=df, time_feature=time_feature_name, series_feature=series_feature_name)
        prophet = ProphetForecast(timeseries=df)
        prophet.prophet_fit()
        prophet.set_future(period=prediction_length, freq=freq)
        prophet.prophet_predict()
        fig = prophet.prophet_plot_pyplot()
        st.pyplot(fig)

