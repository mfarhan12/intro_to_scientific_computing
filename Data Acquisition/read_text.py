# Read all the text data into memory
file = open('sample_text.txt', 'r')
file_data = file.read()
print file_data

# Reset file line
file.seek(0)
for data in file:
	print data.rstrip("\n")