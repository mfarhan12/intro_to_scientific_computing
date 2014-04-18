data = {}

file = open('sample_csv.csv', 'r')

file_header = file.readline().split(',')

for header_item in file_header:
	data[header_item] = []

for raw_data in file:
	print raw_data
