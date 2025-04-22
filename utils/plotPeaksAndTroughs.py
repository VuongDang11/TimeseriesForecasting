
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def plotPeaksAndTroughs(df,value='value',time='date',label="Time Series",title='Peak and Troughs of of Time Series'):  
    ''' Function to plot the Peaks and Troughs for Time Series
    input: df: dataframe of Time Series
           value: column name of value (default: "value")
           time:  column name of time (default: "date")
           label[option]: label of Time Series line
           title [option]: title of plot
    output: peak_locations: array positions of Peaks
            trough_locations: array postitions of Troughs
    '''
    # Get the Peaks and Troughs
    df = df.reset_index(drop=True)
    df[time] = pd.to_datetime(df[time])
    time = df[time].astype(str).values
    
    data = df[value].values
    doublediff = np.diff(np.sign(np.diff(data))) ##double difference
    peak_locations = np.where(doublediff == -2)[0] + 1

    doublediff2 = np.diff(np.sign(np.diff(-1*data)))
    trough_locations = np.where(doublediff2 == -2)[0] + 1

    # Draw Plot
    plt.figure(figsize=(10,8), dpi= 80)
    plt.plot(time, value, data=df, color='tab:blue', label=label)
    plt.scatter(time[peak_locations], df[value][peak_locations], marker=mpl.markers.CARETUPBASE, color='tab:green', s=100, label='Peaks')
    plt.scatter(time[trough_locations], df[value][trough_locations], marker=mpl.markers.CARETDOWNBASE, color='tab:red', s=100, label='Troughs')

    xtick_location = df.index.tolist()[::6]
    xtick_labels = df.date.tolist()[::6]
    plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=90, fontsize=12, alpha=.7)
    plt.title(title, fontsize=22)
    plt.yticks(fontsize=12, alpha=.7)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(.0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(.0)
    plt.gca().spines["left"].set_alpha(.3)

    plt.legend(loc='upper left')
    plt.grid(axis='y', alpha=.3)
    plt.show()
    return peak_locations,trough_locations

