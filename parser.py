import csv

file = 'rdu-weather-history.csv'
header = []
parsed_header = []
rows = []
parsed_header_rows = {}

with open(file, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  header = csvreader.next()
  parsed_header = header[0].split(';')

  for row in csvreader:
    rows.append(row[0].split(';'))

parsed_header_rows['header'] = parsed_header
parsed_header_rows['rows'] = rows