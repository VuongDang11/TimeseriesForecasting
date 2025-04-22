def fillNanTimeSeries(df,value='value',time='date'):
    ''' Function to make fill Nan values in TimeSeries by several methods
        Input: 
            data: DataFrame
            value: column name of value (default: "value")
            time:  column name of time (default: "date")
        Output:
            result: DataFrame with filled nan columns included
    '''
    df = df.copy()
    fig, axes = plt.subplots(7, 1, sharex=True, figsize=(10, 12))
    plt.rcParams.update({'xtick.bottom' : False})
    
    ## 1. Actual -------------------------------
    # df_orig.plot(title='Actual', ax=axes[0], label='Actual', color='red', style=".-")
    df.plot(title='Actual', ax=axes[0], label='Actual', color='green', style=".-")
    axes[0].legend(["Missing Data", "Available Data"])

    ## 2. Forward Fill --------------------------
    df['ffill'] = df.ffill()[value].copy()
#     error = np.round(mean_squared_error(df_orig['value'], df_ffill['value']), 2)
    df['ffill'].plot(title='Forward Fill', ax=axes[1], label='Forward Fill', style=".-")

    ## 3. Backward Fill -------------------------
    df['bfill'] = df.bfill()[value].copy()
#     error = np.round(mean_squared_error(df_orig['value'], df_bfill['value']), 2)
    df['bfill'].plot(title="Backward Fill", ax=axes[2], label='Back Fill', color='firebrick', style=".-")

    ## 4. Linear Interpolation ------------------
    from  scipy.interpolate import interp1d

    df['rownum'] = np.arange(df.shape[0])
    df_nona = df.dropna(subset = [value])
    f = interp1d(df_nona['rownum'], df_nona[value])
    df['linear_fill'] = f(df['rownum'])
#     error = np.round(mean_squared_error(df_orig[value], df['linear_fill']), 2)
    df['linear_fill'].plot(title="Linear Fill", ax=axes[3], label='Cubic Fill', color='brown', style=".-")

    ## 5. Cubic Interpolation --------------------
    f2 = interp1d(df_nona['rownum'], df_nona['value'], kind='cubic')
    df['cubic_fill'] = f2(df['rownum'])
    # error = np.round(mean_squared_error(df_orig['value'], df['cubic_fill']), 2)
    df['cubic_fill'].plot(title="Cubic Fill", ax=axes[4], label='Cubic Fill', color='red', style=".-")

    # Interpolation References:
    # https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
    # https://docs.scipy.org/doc/scipy/reference/interpolate.html

    ## 6. Mean of 'n' Nearest Past Neighbors ------
    def knn_mean(ts, n):
        out = np.copy(ts)
        for i, val in enumerate(ts):
            if np.isnan(val):
                n_by_2 = np.ceil(n/2)
                lower = np.max([0, int(i-n_by_2)])
                upper = np.min([len(ts)+1, int(i+n_by_2)])
                ts_near = np.concatenate([ts[lower:i], ts[i:upper]])
                out[i] = np.nanmean(ts_near)
        return out

    df['knn_mean'] = knn_mean(df.value.values, 8)
#     error = np.round(mean_squared_error(df_orig['value'], df['knn_mean']), 2)
    df['knn_mean'].plot(title="KNN Mean", ax=axes[5], label='KNN Mean', color='tomato', alpha=0.5, style=".-")

    ## 7. Seasonal Mean ----------------------------
    def seasonal_mean(ts, n, lr=0.7):
        """
        Compute the mean of corresponding seasonal periods
        ts: 1D array-like of the time series
        n: Seasonal window length of the time series
        """
        out = np.copy(ts)
        for i, val in enumerate(ts):
            if np.isnan(val):
                ts_seas = ts[i-1::-n]  # previous seasons only
                if np.isnan(np.nanmean(ts_seas)):
                    ts_seas = np.concatenate([ts[i-1::-n], ts[i::n]])  # previous and forward
                out[i] = np.nanmean(ts_seas) * lr
        return out

    df['seasonal_mean'] = seasonal_mean(df.value, n=12, lr=1.25)
#     error = np.round(mean_squared_error(df_orig['value'], df['seasonal_mean']), 2)
    df['seasonal_mean'].plot(title="Seasonal Mean", ax=axes[6], label='Seasonal Mean', color='blue', alpha=0.5, style=".-")
    plt.plot()
    return df
