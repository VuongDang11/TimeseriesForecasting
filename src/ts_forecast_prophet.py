from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import pandas as pd
import streamlit as st

class ProphetForecast:
    def __init__(self, timeseries: pd.DataFrame):
        if timeseries is not None:
            self.timeseries = timeseries
        self.model = Prophet()
        self.future = None
        self.forecast = None
        
    def set_future(self, period:int = 365, freq: str = 'M'):
        self.future = self.model.make_future_dataframe(periods=period,  freq=freq)

    def prophet_fit(self, timeseries:pd.DataFrame = None):
        "Fit the Prophet model"
        if timeseries is not None:
            self.model.fit(timeseries)
        else:
            self.model.fit(self.timeseries)

    def prophet_predict(self):
        "Predict future time scale"
        self.forecast = self.model.predict(self.future)

    def prophet_plot_pyplot(self):
        "Plot the prediction based on prophet"
        fig = self.model.plot(self.forecast)
        return fig
    
    def prophet_plot_plotly(self):
        fig = plot_plotly(self.model, self.forecast)
        return fig

