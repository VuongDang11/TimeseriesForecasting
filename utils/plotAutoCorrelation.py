
def plotAutoCorrelation(df,value='value',time='date', lags = 50):
    ''' Function to plot AutoCorrelation and Partial AutoCorrelation
        Input: 
            df: DataFrame of Time Series
            value: column name of value (default: "value")
            time:  column name of time (default: "date")
            lags: lag of Time Series for checking (default = 50)
    '''
    # import
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

    # Draw Plot
    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,6), dpi= 80)
    plot_acf(df[value].tolist(), ax=ax1, lags=50)
    plot_pacf(df[value].tolist(), ax=ax2, lags=50)

    # Decorate
    # lighten the borders
    ax1.spines["top"].set_alpha(.3); ax2.spines["top"].set_alpha(.3)
    ax1.spines["bottom"].set_alpha(.3); ax2.spines["bottom"].set_alpha(.3)
    ax1.spines["right"].set_alpha(.3); ax2.spines["right"].set_alpha(.3)
    ax1.spines["left"].set_alpha(.3); ax2.spines["left"].set_alpha(.3)

    # font size of tick labels
    ax1.tick_params(axis='both', labelsize=12)
    ax2.tick_params(axis='both', labelsize=12)
    ax1.grid()
    ax2.grid()
    plt.show()
    