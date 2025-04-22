def testStationarity(series, method='ADF'):
    ''' Function to test the Stationary of Series
        Input: 
            series: Series input
            method: "ADF" or "KPSS"
    '''
    if method=='ADF':
        from statsmodels.tsa.stattools import adfuller
        print("="*20)
        # ADF Test
        result = adfuller(series, autolag='AIC')
        print(f'Augmented Dickey-Fuller Statistic: {result[0]}')
        print(f'p-value: {result[1]}')
        for key, value in result[4].items():
            print('Critial Values:')
            print(f'   {key}, {value}')
        print(f'Result(ADF): The series is {"not " if result[1] > 0.05 else ""}stationary')
        
    if method=='KPSS':
        print("="*20)
        from statsmodels.tsa.stattools import kpss
        statistic, p_value, n_lags, critical_values = kpss(series)
        # Format Output
        print(f'Kwiatkowski-Phillips-Schmidt-Shin Statistic: {statistic}')
        print(f'p-value: {p_value}')
        print(f'num lags: {n_lags}')
        print('Critial Values:')
        for key, value in critical_values.items():
            print(f'   {key} : {value}')
        print(f'Result(KPSS): The series is {"not " if p_value < 0.05 else ""}stationary')
    print("="*20)