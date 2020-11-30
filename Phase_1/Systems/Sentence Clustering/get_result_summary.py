import csv
import os

all_files = os.listdir('Try2_output')
summary_file = open('Try2_summary', 'w+')
for file in all_files:
	csv_reader = csv.reader(open('Try2_output/'+str(file)))
	summary_file.write('\n' + str(file) + '\n')
	for row in csv_reader:
		summary_file.write(row[0] + '\n')
	# break
	# print(str(file))