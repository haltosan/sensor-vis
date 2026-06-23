import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import matplot2tikz
import sys
from datetime import datetime

start_time = None
end_time = None
summary = ''

def user_input():
    global summary
    summary += 'Date: ' + str(datetime.now()).split('.')[0] + '\\newline\n'
    summary += 'Addr: ' + input('Address: ') + '\\newline\n'
    summary += 'Insepctor: ' + input('Name of inspector: ') + '\\newline\n'
    summary += 'Room: ' + input('Location of sensor: ') + '\\newline\n'
    summary += input('Is this [initial/follow up]: ') + ' test\\newline\n'

def show_column(column, data_file, title, ylabel, tex):
    global start_time, end_time, summary
    itr = pd.read_csv(data_file, sep=';', iterator=True, chunksize=1000)
    data = pd.concat([chunk[chunk[column] >= 0] for chunk in itr])

    x = [datetime.strptime(i,'%Y-%m-%dT%H:%M:%S') for i in data['recorded']]
    y = data[column]
    summary += title + '\\newline\n'
    summary += 'Min: ' + str(np.min(y)) + '\\newline\n'
    summary += 'Max: ' + str(np.max(y)) + '\\newline\n'
    summary += 'Avg:' + str(np.average(y)) + '\\newline\n'
    if start_time is None or x[0] < start_time:
        start_time = x[0]
    if end_time is None or x[-1] > end_time:
        end_time = x[-1]
    plt.plot(x,y)
    plt.gcf().autofmt_xdate()

    plt.title(title)
    plt.xlabel('MM-DD HH')
    plt.ylabel(ylabel)
    #plt.show()
    matplot2tikz.save(tex+'.tex')
    plt.close()


def show_columns(fname):
    reports = [
            ['RADON_SHORT_TERM_AVG pCi/L', 'Radon detection over time', 'Radon pCi/L', 'radon'],
            ['TEMP °F', 'Temperature over time', 'Degrees F', 'temp'],
            ['HUMIDITY %', 'Humidity over time', 'Humidity %', 'humid']
    ]
    for report in reports:
        show_column(report[0], fname, report[1], report[2], report[3])

fname = sys.argv[1]

user_input()
show_columns(fname)
summary += '\\newline\n'
summary += 'Start time: ' + str(start_time) + '\\newline\n'
summary += 'End time: ' + str(end_time) + '\\newline\n'
summary += 'Test length: ' + str(end_time - start_time) + '\\newline\n'

with open('format.tex', 'r') as x:
    raw = x.read()

out = raw.replace('REP-SUMMARY', summary)
with open('out.tex', 'w') as x:
    x.write(out)
