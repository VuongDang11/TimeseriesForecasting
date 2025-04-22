def ForecastARIMA(train,test, p,d,q,s):
    from statsmodels.tsa.arima.model import ARIMA

    history = [x for x in train]
    predictions = list()
    # walk-forward validation

    for t in range(len(test)):
        model = ARIMA(history, seasonal_order = (p,d,q,s))#order=(5,1,0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    # evaluate forecasts

    from sklearn.metrics import mean_squared_error,mean_absolute_error
    print("Test MAPE: %.3f" % mean_absolute_percentage_error(test, predictions))
    print("Test MAE: %.3f" % mean_absolute_error(test, predictions))
    print("Test MSE: %.3f" % (mean_squared_error(test, predictions)))
    print("Test RMSE: %.3f" % np.sqrt(mean_squared_error(test, predictions)))

    # plot forecasts against actual outcomes
    plt.plot(test)
    plt.plot(predictions, color='red')
    plt.show()