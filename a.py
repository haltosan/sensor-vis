import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np

from datetime import datetime

def show_radon():
    radon_col = 'RADON_SHORT_TERM_AVG pCi/L'
    itr = pd.read_csv('data/ex.csv', sep=';', iterator=True, chunksize=1000)
    data_radon = pd.concat([chunk[chunk[radon_col] >= 0] for chunk in itr])

    x = [datetime.strptime(i,'%Y-%m-%dT%H:%M:%S') for i in data_radon['recorded']]
    y = data_radon[radon_col]
    plt.plot(x,y)
    plt.gcf().autofmt_xdate()

    plt.title('Radon detection over time')
    plt.xlabel('MM-DD HH')
    plt.ylabel('Radon pCi/L')
    plt.show()

show_radon()
