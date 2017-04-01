import csv
import numpy as np

dataArray = []

with open('C:/Miniconda3/pyCode/test10-ssh_channel_read.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        dataArray.append(row)

    for i in range(len(dataArray)):
        if dataArray[i] == 'Value':
            print(' ')
