# Python program to
# demonstrate merging of
# two files
import time
# Creating a list of filenames
filenames = ['Sales1.csv', 'Sales2.csv', 'Sales3.csv', 'Sales4.csv']
begin = time.time()
# Open file3 in write mode
with open('Total_Sales5.csv', 'w') as outfile:
	# Iterate through list
	for names in filenames:

		# Open each file in read mode
		with open(names) as infile:
			# read the data from file1 and
			# file2 and write it in file3
			outfile.write(infile.read())

		# Add '\n' to enter data of file2
		# from next line
		outfile.write("\n")
for i in range(10):
		end = time.time()
print(f"Total runtime of the program is {end - begin}")