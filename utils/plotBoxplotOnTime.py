def plotBoxplotOnTime(df,value='value',time='date', formatdate='%Y-%m-%d'):
    ''' Function to plot the Boxplot of Time Series
        Input: 
            df: DataFrame of Time Series
            value: column name of value (default: "value")
            time:  column name of time (default: "date")
            formatdate: format of datetime (default: '%Y-%m-%d')
            
        Output:
            result_: matplotlib of boxplots
    '''

    # Prepare data
    df = df.reset_index(drop=True)
    df[time] = pd.to_datetime(df[time])

    df['year'] = [d.year for d in df[time]]
    df['month'] = [d.strftime('%b') for d in df[time]]
    df['day'] = [d.strftime('%d') for d in df[time]]
    df['dow'] = [d.strftime("%A") for d in df[time]]

    years = df['year'].unique()

    # Draw Plot
    fig, axes = plt.subplots(2, 2, figsize=(20,7), dpi= 80,constrained_layout=True)
#     fig.tight_layout()
    sns.boxplot(x='year', y=value, data=df, ax=axes[0][0])
    sns.boxplot(x='month', y='value', data=df,ax=axes[0][1])
    sns.boxplot(x='day', y='value', data=df,ax=axes[1][0])
    sns.boxplot(x="dow", y='value', data=df,ax=axes[1][1])

    # Set Title
    axes[0][0].set_title('\n Year-wise Box Plot', fontsize=18); 
    axes[0][1].set_title('\n Month-wise Box Plot', fontsize=18)
    axes[1][0].set_title('\n Day-wise Box Plot', fontsize=18)
    axes[1][1].set_title('\n DoW-wise Box Plot', fontsize=18)
    plt.show()