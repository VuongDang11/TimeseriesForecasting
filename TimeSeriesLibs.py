from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sys
import subprocess
import pkg_resources
import warnings
warnings.filterwarnings('ignore')

# def plotPeaksAndTroughs(df,value='value',time='date',label="Time Series",title='Peak and Troughs of of Time Series'):  
#     ''' Function to plot the Peaks and Troughs for Time Series
#     input: df: dataframe of Time Series
#            value: column name of value (default: "value")
#            time:  column name of time (default: "date")
#            label[option]: label of Time Series line
#            title [option]: title of plot
#     output: peak_locations: array positions of Peaks
#             trough_locations: array postitions of Troughs
#     '''
#     # Get the Peaks and Troughs
#     df = df.reset_index(drop=True)
#     df[time] = pd.to_datetime(df[time])
#     time = df[time].astype(str).values
    
#     data = df[value].values
#     doublediff = np.diff(np.sign(np.diff(data))) ##double difference
#     peak_locations = np.where(doublediff == -2)[0] + 1

#     doublediff2 = np.diff(np.sign(np.diff(-1*data)))
#     trough_locations = np.where(doublediff2 == -2)[0] + 1

#     # Draw Plot
#     plt.figure(figsize=(10,8), dpi= 80)
#     plt.plot(time, value, data=df, color='tab:blue', label=label)
#     plt.scatter(time[peak_locations], df[value][peak_locations], marker=mpl.markers.CARETUPBASE, color='tab:green', s=100, label='Peaks')
#     plt.scatter(time[trough_locations], df[value][trough_locations], marker=mpl.markers.CARETDOWNBASE, color='tab:red', s=100, label='Troughs')

#     xtick_location = df.index.tolist()[::6]
#     xtick_labels = df.date.tolist()[::6]
#     plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=90, fontsize=12, alpha=.7)
#     plt.title(title, fontsize=22)
#     plt.yticks(fontsize=12, alpha=.7)

#     # Lighten borders
#     plt.gca().spines["top"].set_alpha(.0)
#     plt.gca().spines["bottom"].set_alpha(.3)
#     plt.gca().spines["right"].set_alpha(.0)
#     plt.gca().spines["left"].set_alpha(.3)

#     plt.legend(loc='upper left')
#     plt.grid(axis='y', alpha=.3)
#     plt.show()
#     return peak_locations,trough_locations

# def plotAutoCorrelation(df,value='value',time='date', lags = 50):
#     ''' Function to plot AutoCorrelation and Partial AutoCorrelation
#         Input: 
#             df: DataFrame of Time Series
#             value: column name of value (default: "value")
#             time:  column name of time (default: "date")
#             lags: lag of Time Series for checking (default = 50)
#     '''
#     # import
#     from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#     # Draw Plot
#     fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,6), dpi= 80)
#     plot_acf(df[value].tolist(), ax=ax1, lags=50)
#     plot_pacf(df[value].tolist(), ax=ax2, lags=50)

#     # Decorate
#     # lighten the borders
#     ax1.spines["top"].set_alpha(.3); ax2.spines["top"].set_alpha(.3)
#     ax1.spines["bottom"].set_alpha(.3); ax2.spines["bottom"].set_alpha(.3)
#     ax1.spines["right"].set_alpha(.3); ax2.spines["right"].set_alpha(.3)
#     ax1.spines["left"].set_alpha(.3); ax2.spines["left"].set_alpha(.3)

#     # font size of tick labels
#     ax1.tick_params(axis='both', labelsize=12)
#     ax2.tick_params(axis='both', labelsize=12)
#     ax1.grid()
#     ax2.grid()
#     plt.show()
    
# def plotCrossCorrelation(df,firstFeature, secondFeature,title):
    
#     import statsmodels.tsa.stattools as stattools

#     # Import Data
#     x = df[firstFeature]
#     y = df[secondFeature]

#     # Compute Cross Correlations
#     ccs = stattools.ccf(x, y)[:100]
#     nlags = len(ccs)

#     # Compute the Significance level
#     # ref: https://stats.stackexchange.com/questions/3115/cross-correlation-significance-in-r/3128#3128
#     conf_level = 2 / np.sqrt(nlags)

#     # Draw Plot
#     plt.figure(figsize=(12,7), dpi= 80)

#     plt.hlines(0, xmin=0, xmax=100, color='gray')  # 0 axis
#     plt.hlines(conf_level, xmin=0, xmax=100, color='gray')
#     plt.hlines(-conf_level, xmin=0, xmax=100, color='gray')

#     plt.bar(x=np.arange(len(ccs)), height=ccs, width=.3)

#     # Decoration
#     plt.title(title, fontsize=22)
#     plt.xlim(0,len(ccs))
#     plt.show()
    
# def plotDecomposeTimeSeries(df,value='value',time='date', formatdate='%Y-%m-%d', model = 'multiplicative'):
#     ''' Function to plot the Decompose Time Series
#         Input: 
#             df: DataFrame of Time Series
#             value: column name of value (default: "value")
#             time:  column name of time (default: "date")
#             formatdate: format of datetime (default: '%Y-%m-%d')
#             model: model of decompose method (default: 'multiplicative')
#                     model should be in ['multiplicative', 'additive']
#         Output:
#             result_: statsmodel for decompose Time Series
#     '''
#     if model not in ['multiplicative', 'additive']:
#         model = 'multiplicative'
#     else:
    
#         from statsmodels.tsa.seasonal import seasonal_decompose
#         from dateutil.parser import parse

#         # Import Data
#         dates = pd.DatetimeIndex([parse(d).strftime(formatdate) for d in df[time]])
#         df = df.set_index(dates).copy()

#         result_ = seasonal_decompose(df[value], model=model, extrapolate_trend='freq')

#         # Plot
#         plt.rcParams.update({'figure.figsize': (5,5)})
#         result_.plot().suptitle(f'{str.capitalize(model)} Decompose', fontsize=10, y=1)
        
#         plt.show()
#         return result_
    
# def plotBoxplotOnTime(df,value='value',time='date', formatdate='%Y-%m-%d'):
#     ''' Function to plot the Boxplot of Time Series
#         Input: 
#             df: DataFrame of Time Series
#             value: column name of value (default: "value")
#             time:  column name of time (default: "date")
#             formatdate: format of datetime (default: '%Y-%m-%d')
            
#         Output:
#             result_: matplotlib of boxplots
#     '''

#     # Prepare data
#     df = df.reset_index(drop=True)
#     df[time] = pd.to_datetime(df[time])

#     df['year'] = [d.year for d in df[time]]
#     df['month'] = [d.strftime('%b') for d in df[time]]
#     df['day'] = [d.strftime('%d') for d in df[time]]
#     df['dow'] = [d.strftime("%A") for d in df[time]]

#     years = df['year'].unique()

#     # Draw Plot
#     fig, axes = plt.subplots(2, 2, figsize=(20,7), dpi= 80,constrained_layout=True)
# #     fig.tight_layout()
#     sns.boxplot(x='year', y=value, data=df, ax=axes[0][0])
#     sns.boxplot(x='month', y='value', data=df,ax=axes[0][1])
#     sns.boxplot(x='day', y='value', data=df,ax=axes[1][0])
#     sns.boxplot(x="dow", y='value', data=df,ax=axes[1][1])

#     # Set Title
#     axes[0][0].set_title('\n Year-wise Box Plot', fontsize=18); 
#     axes[0][1].set_title('\n Month-wise Box Plot', fontsize=18)
#     axes[1][0].set_title('\n Day-wise Box Plot', fontsize=18)
#     axes[1][1].set_title('\n DoW-wise Box Plot', fontsize=18)
#     plt.show()

# def make_stationary(data: pd.Series, alpha: float = 0.05, max_diff_order: int = 10) -> dict:
#     ''' Function to make Series to Stationary
#         Input: 
#             data: Series of Time Series
#             alpha: Alpha of confident level (default = 0.05)
#             max_diff_order:  maximun difference of order of lags (defaul=10)
#         Output:
#             result: dictionary {'differencing_order','time_series'}
            
#     '''
#     from statsmodels.tsa.stattools import adfuller
#     # Test to see if the time series is already stationary
#     if adfuller(data)[1] < alpha:
#         return {
#             'differencing_order': 0,
#             'time_series': np.array(data)
#         }
    
#     # A list to store P-Values
#     p_values = []
    
#     # Test for differencing orders from 1 to max_diff_order (included)
#     for i in range(1, max_diff_order + 1):
#         # Perform ADF test
#         result = adfuller(data.diff(i).dropna())
#         # Append P-value
#         p_values.append((i, result[1]))
        
#     # Keep only those where P-value is lower than significance level
#     significant = [p for p in p_values if p[1] < alpha]
#     # Sort by the differencing order
#     significant = sorted(significant, key=lambda x: x[0])
    
#     # Get the differencing order
#     diff_order = significant[0][0]
    
#     # Make the time series stationary
#     stationary_series = data.diff(diff_order).dropna()
    
#     ap_stationary = {
#         'differencing_order': diff_order,
#         'time_series': np.array(stationary_series)
#     }

#     plt.title(f"Stationary Time Series Dataset - Order = {ap_stationary['differencing_order']}", size=20)
#     plt.plot(ap_stationary['time_series']);
#     return ap_stationary

# def testStationarity(series, method='ADF'):
#     ''' Function to test the Stationary of Series
#         Input: 
#             series: Series input
#             method: "ADF" or "KPSS"
#     '''
#     if method=='ADF':
#         from statsmodels.tsa.stattools import adfuller
#         print("="*20)
#         # ADF Test
#         result = adfuller(series, autolag='AIC')
#         print(f'Augmented Dickey-Fuller Statistic: {result[0]}')
#         print(f'p-value: {result[1]}')
#         for key, value in result[4].items():
#             print('Critial Values:')
#             print(f'   {key}, {value}')
#         print(f'Result(ADF): The series is {"not " if result[1] > 0.05 else ""}stationary')
        
#     if method=='KPSS':
#         print("="*20)
#         from statsmodels.tsa.stattools import kpss
#         statistic, p_value, n_lags, critical_values = kpss(series)
#         # Format Output
#         print(f'Kwiatkowski-Phillips-Schmidt-Shin Statistic: {statistic}')
#         print(f'p-value: {p_value}')
#         print(f'num lags: {n_lags}')
#         print('Critial Values:')
#         for key, value in critical_values.items():
#             print(f'   {key} : {value}')
#         print(f'Result(KPSS): The series is {"not " if p_value < 0.05 else ""}stationary')
#     print("="*20)

# def fillNanTimeSeries(df,value='value',time='date'):
#     ''' Function to make fill Nan values in TimeSeries by several methods
#         Input: 
#             data: DataFrame
#             value: column name of value (default: "value")
#             time:  column name of time (default: "date")
#         Output:
#             result: DataFrame with filled nan columns included
#     '''
#     df = df.copy()
#     fig, axes = plt.subplots(7, 1, sharex=True, figsize=(10, 12))
#     plt.rcParams.update({'xtick.bottom' : False})
    
#     ## 1. Actual -------------------------------
#     # df_orig.plot(title='Actual', ax=axes[0], label='Actual', color='red', style=".-")
#     df.plot(title='Actual', ax=axes[0], label='Actual', color='green', style=".-")
#     axes[0].legend(["Missing Data", "Available Data"])

#     ## 2. Forward Fill --------------------------
#     df['ffill'] = df.ffill()[value].copy()
# #     error = np.round(mean_squared_error(df_orig['value'], df_ffill['value']), 2)
#     df['ffill'].plot(title='Forward Fill', ax=axes[1], label='Forward Fill', style=".-")

#     ## 3. Backward Fill -------------------------
#     df['bfill'] = df.bfill()[value].copy()
# #     error = np.round(mean_squared_error(df_orig['value'], df_bfill['value']), 2)
#     df['bfill'].plot(title="Backward Fill", ax=axes[2], label='Back Fill', color='firebrick', style=".-")

#     ## 4. Linear Interpolation ------------------
#     from  scipy.interpolate import interp1d

#     df['rownum'] = np.arange(df.shape[0])
#     df_nona = df.dropna(subset = [value])
#     f = interp1d(df_nona['rownum'], df_nona[value])
#     df['linear_fill'] = f(df['rownum'])
# #     error = np.round(mean_squared_error(df_orig[value], df['linear_fill']), 2)
#     df['linear_fill'].plot(title="Linear Fill", ax=axes[3], label='Cubic Fill', color='brown', style=".-")

#     ## 5. Cubic Interpolation --------------------
#     f2 = interp1d(df_nona['rownum'], df_nona['value'], kind='cubic')
#     df['cubic_fill'] = f2(df['rownum'])
#     # error = np.round(mean_squared_error(df_orig['value'], df['cubic_fill']), 2)
#     df['cubic_fill'].plot(title="Cubic Fill", ax=axes[4], label='Cubic Fill', color='red', style=".-")

#     # Interpolation References:
#     # https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
#     # https://docs.scipy.org/doc/scipy/reference/interpolate.html

#     ## 6. Mean of 'n' Nearest Past Neighbors ------
#     def knn_mean(ts, n):
#         out = np.copy(ts)
#         for i, val in enumerate(ts):
#             if np.isnan(val):
#                 n_by_2 = np.ceil(n/2)
#                 lower = np.max([0, int(i-n_by_2)])
#                 upper = np.min([len(ts)+1, int(i+n_by_2)])
#                 ts_near = np.concatenate([ts[lower:i], ts[i:upper]])
#                 out[i] = np.nanmean(ts_near)
#         return out

#     df['knn_mean'] = knn_mean(df.value.values, 8)
# #     error = np.round(mean_squared_error(df_orig['value'], df['knn_mean']), 2)
#     df['knn_mean'].plot(title="KNN Mean", ax=axes[5], label='KNN Mean', color='tomato', alpha=0.5, style=".-")

#     ## 7. Seasonal Mean ----------------------------
#     def seasonal_mean(ts, n, lr=0.7):
#         """
#         Compute the mean of corresponding seasonal periods
#         ts: 1D array-like of the time series
#         n: Seasonal window length of the time series
#         """
#         out = np.copy(ts)
#         for i, val in enumerate(ts):
#             if np.isnan(val):
#                 ts_seas = ts[i-1::-n]  # previous seasons only
#                 if np.isnan(np.nanmean(ts_seas)):
#                     ts_seas = np.concatenate([ts[i-1::-n], ts[i::n]])  # previous and forward
#                 out[i] = np.nanmean(ts_seas) * lr
#         return out

#     df['seasonal_mean'] = seasonal_mean(df.value, n=12, lr=1.25)
# #     error = np.round(mean_squared_error(df_orig['value'], df['seasonal_mean']), 2)
#     df['seasonal_mean'].plot(title="Seasonal Mean", ax=axes[6], label='Seasonal Mean', color='blue', alpha=0.5, style=".-")
#     plt.plot()
#     return df


# def smoothingTimeSeries(df,verbose=True):
#     ''' Function to smooth the Time Series
#         Input: df: DataFrame of Time Series
#         Output:
#             df_ma:      Moving Average(3) smoothing
#             df_loess_5: Loess Smoothing (5%)
#             df_loess_15: Loess Smoothing (15%)
#     '''
#     from statsmodels.nonparametric.smoothers_lowess import lowess
#     plt.rcParams.update({'xtick.bottom' : False, 'axes.titlepad':5})

#     # Import
#     df_orig = df.copy()
#     # 1. Moving Average
#     df_ma = df_orig.value.rolling(3, center=True, closed='both').mean()

#     # 2. Loess Smoothing (5% and 15%)
#     df_loess_5 = pd.DataFrame(lowess(df_orig.value, np.arange(len(df_orig.value)), frac=0.05)[:, 1], index=df_orig.index, columns=['value'])
#     df_loess_15 = pd.DataFrame(lowess(df_orig.value, np.arange(len(df_orig.value)), frac=0.15)[:, 1], index=df_orig.index, columns=['value'])

#     # Plot
#     if verbose:
#         fig, axes = plt.subplots(4,1, figsize=(7, 7), sharex=True, dpi=120)
#         df_orig['value'].plot(ax=axes[0], color='k', title='Original Series')
#         df_loess_5['value'].plot(ax=axes[1], title='Loess Smoothed 5%')
#         df_loess_15['value'].plot(ax=axes[2], title='Loess Smoothed 15%')
#         df_ma.plot(ax=axes[3], title='Moving Average (3)')
#         fig.suptitle('Smoothen a Time Series', y=0.95, fontsize=14)
#         plt.show()
    
#     return df_ma,df_loess_5,df_loess_15


# def mean_absolute_percentage_error(y_true, y_pred): 
#     y_true, y_pred = np.array(y_true), np.array(y_pred)
#     return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# def ForecastARIMA(train,test, p,d,q,s):
#     from statsmodels.tsa.arima.model import ARIMA

#     history = [x for x in train]
#     predictions = list()
#     # walk-forward validation

#     for t in range(len(test)):
#         model = ARIMA(history, seasonal_order = (p,d,q,s))#order=(5,1,0))
#         model_fit = model.fit()
#         output = model_fit.forecast()
#         yhat = output[0]
#         predictions.append(yhat)
#         obs = test[t]
#         history.append(obs)
#         print('predicted=%f, expected=%f' % (yhat, obs))
#     # evaluate forecasts

#     from sklearn.metrics import mean_squared_error,mean_absolute_error
#     print("Test MAPE: %.3f" % mean_absolute_percentage_error(test, predictions))
#     print("Test MAE: %.3f" % mean_absolute_error(test, predictions))
#     print("Test MSE: %.3f" % (mean_squared_error(test, predictions)))
#     print("Test RMSE: %.3f" % np.sqrt(mean_squared_error(test, predictions)))

#     # plot forecasts against actual outcomes
#     plt.plot(test)
#     plt.plot(predictions, color='red')
#     plt.show()