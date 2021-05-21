import csv

with open('datapoints.txt', mode='r') as infile:
    reader = csv.reader(infile)
    with open('datapoints_new.txt', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}