def plotCrossCorrelation(df,firstFeature, secondFeature,title):
    
    import statsmodels.tsa.stattools as stattools

    # Import Data
    x = df[firstFeature]
    y = df[secondFeature]

    # Compute Cross Correlations
    ccs = stattools.ccf(x, y)[:100]
    nlags = len(ccs)

    # Compute the Significance level
    # ref: https://stats.stackexchange.com/questions/3115/cross-correlation-significance-in-r/3128#3128
    conf_level = 2 / np.sqrt(nlags)

    # Draw Plot
    plt.figure(figsize=(12,7), dpi= 80)

    plt.hlines(0, xmin=0, xmax=100, color='gray')  # 0 axis
    plt.hlines(conf_level, xmin=0, xmax=100, color='gray')
    plt.hlines(-conf_level, xmin=0, xmax=100, color='gray')

    plt.bar(x=np.arange(len(ccs)), height=ccs, width=.3)

    # Decoration
    plt.title(title, fontsize=22)
    plt.xlim(0,len(ccs))
    plt.show()