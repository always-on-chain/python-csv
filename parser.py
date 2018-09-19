import csv

filename = 'rdu-weather-history.csv'
fields = []
rows = []

with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  fields = csvreader.next()

  for row in csvreader:
    rows.append(row)

  print('Total no. of rows: %d'%(csvreader.line_num))