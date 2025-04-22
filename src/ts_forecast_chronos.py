from chronos import ChronosPipeline
import pandas as pd
import numpy as np
import torch


class ChronosForecast:
    " Time-Series Forecasting with Chronos"
    def __init__(self, df: pd.DataFrame, feature_name : str):
        self.df = df
        self.timeseries = df[feature_name]

        self.pipeline = ChronosPipeline.from_pretrained(
                "amazon/chronos-t5-small",
                device_map="cpu",
                torch_dtype=torch.bfloat16,
                )
        self.context = None
        self.forecast = None
        self.prediction_length = 0

    def get_context(self):
        "Get context from tensor timeseries"
        self.context = torch.tensor(self.timeseries, dtype=torch.int64)
    
    def get_confident_interval(self):
        "Get the CI with 90% interval"
        n = len(self.timeseries)
        self.forecast_index = range(n, n + self.prediction_length)
        self.low, self.median, self.high = np.quantile(self.forecast[0].numpy(), [0.1, 0.5, 0.9], axis=0)

    def chronos_predict(self, prediction_length: int = 64):
        "Predict by prediction length"
        self.get_context()
        self.prediction_length = prediction_length
        self.forecast = self.pipeline.predict(self.context, 
                                              self.prediction_length, 
                                              limit_prediction_length=False)
        
        self.get_confident_interval()
        
