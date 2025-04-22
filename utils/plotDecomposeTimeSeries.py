def plotDecomposeTimeSeries(df,value='value',time='date', formatdate='%Y-%m-%d', model = 'multiplicative'):
    ''' Function to plot the Decompose Time Series
        Input: 
            df: DataFrame of Time Series
            value: column name of value (default: "value")
            time:  column name of time (default: "date")
            formatdate: format of datetime (default: '%Y-%m-%d')
            model: model of decompose method (default: 'multiplicative')
                    model should be in ['multiplicative', 'additive']
        Output:
            result_: statsmodel for decompose Time Series
    '''
    if model not in ['multiplicative', 'additive']:
        model = 'multiplicative'
    else:
    
        from statsmodels.tsa.seasonal import seasonal_decompose
        from dateutil.parser import parse

        # Import Data
        dates = pd.DatetimeIndex([parse(d).strftime(formatdate) for d in df[time]])
        df = df.set_index(dates).copy()

        result_ = seasonal_decompose(df[value], model=model, extrapolate_trend='freq')

        # Plot
        plt.rcParams.update({'figure.figsize': (5,5)})
        result_.plot().suptitle(f'{str.capitalize(model)} Decompose', fontsize=10, y=1)
        
        plt.show()
        return result_