def smoothingTimeSeries(df,verbose=True):
    ''' Function to smooth the Time Series
        Input: df: DataFrame of Time Series
        Output:
            df_ma:      Moving Average(3) smoothing
            df_loess_5: Loess Smoothing (5%)
            df_loess_15: Loess Smoothing (15%)
    '''
    from statsmodels.nonparametric.smoothers_lowess import lowess
    plt.rcParams.update({'xtick.bottom' : False, 'axes.titlepad':5})

    # Import
    df_orig = df.copy()
    # 1. Moving Average
    df_ma = df_orig.value.rolling(3, center=True, closed='both').mean()

    # 2. Loess Smoothing (5% and 15%)
    df_loess_5 = pd.DataFrame(lowess(df_orig.value, np.arange(len(df_orig.value)), frac=0.05)[:, 1], index=df_orig.index, columns=['value'])
    df_loess_15 = pd.DataFrame(lowess(df_orig.value, np.arange(len(df_orig.value)), frac=0.15)[:, 1], index=df_orig.index, columns=['value'])

    # Plot
    if verbose:
        fig, axes = plt.subplots(4,1, figsize=(7, 7), sharex=True, dpi=120)
        df_orig['value'].plot(ax=axes[0], color='k', title='Original Series')
        df_loess_5['value'].plot(ax=axes[1], title='Loess Smoothed 5%')
        df_loess_15['value'].plot(ax=axes[2], title='Loess Smoothed 15%')
        df_ma.plot(ax=axes[3], title='Moving Average (3)')
        fig.suptitle('Smoothen a Time Series', y=0.95, fontsize=14)
        plt.show()
    
    return df_ma,df_loess_5,df_loess_15
