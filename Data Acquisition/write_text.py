file = open('sample_write.txt', 'w')
file.write('This is line one \n')

data = [1, 2, 3, 4, 5]

for d in data:
	file.write(str(d) + "\n")

file.close()