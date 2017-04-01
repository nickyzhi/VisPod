import csv

with open('C:/Python/Python35-32/pyCode/caseForDynamicQuery/test10-ssh_channel_read.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
	    print(', '.join(row).encode("utf-8"))
