import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def plot_series(timeseries : pd.Series, forecast_index, median, low, high):
    "Plot the time series with Forecasting"
    fig, ax = plt.subplots()
    ax.plot(timeseries, color="royalblue", label="historical data")
    ax.plot(forecast_index, median, color="tomato", label="median forecast")
    ax.fill_between(forecast_index, low, high, color="tomato", alpha=0.3, label="90% prediction interval")
    ax.legend()
    ax.grid()
    return fig, ax


def map_feature(df: pd.DataFrame, time_feature: str, series_feature: str):
    df = df.rename(columns={time_feature:'ds', series_feature:'y'}).copy()
    return df