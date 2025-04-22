def make_stationary(data: pd.Series, alpha: float = 0.05, max_diff_order: int = 10) -> dict:
    ''' Function to make Series to Stationary
        Input: 
            data: Series of Time Series
            alpha: Alpha of confident level (default = 0.05)
            max_diff_order:  maximun difference of order of lags (defaul=10)
        Output:
            result: dictionary {'differencing_order','time_series'}
            
    '''
    from statsmodels.tsa.stattools import adfuller
    # Test to see if the time series is already stationary
    if adfuller(data)[1] < alpha:
        return {
            'differencing_order': 0,
            'time_series': np.array(data)
        }
    
    # A list to store P-Values
    p_values = []
    
    # Test for differencing orders from 1 to max_diff_order (included)
    for i in range(1, max_diff_order + 1):
        # Perform ADF test
        result = adfuller(data.diff(i).dropna())
        # Append P-value
        p_values.append((i, result[1]))
        
    # Keep only those where P-value is lower than significance level
    significant = [p for p in p_values if p[1] < alpha]
    # Sort by the differencing order
    significant = sorted(significant, key=lambda x: x[0])
    
    # Get the differencing order
    diff_order = significant[0][0]
    
    # Make the time series stationary
    stationary_series = data.diff(diff_order).dropna()
    
    ap_stationary = {
        'differencing_order': diff_order,
        'time_series': np.array(stationary_series)
    }

    plt.title(f"Stationary Time Series Dataset - Order = {ap_stationary['differencing_order']}", size=20)
    plt.plot(ap_stationary['time_series']);
    return ap_stationary
