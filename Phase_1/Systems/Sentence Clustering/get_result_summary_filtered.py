import csv
import os

all_files = os.listdir('Try2_output')
summary_file = open('Try2_summary_filtered', 'w+')
count = 0
small_cluster_count = 0
for file in all_files:
	if(file.startswith('cluster_')):
		csv_reader = csv.reader(open('Try2_output/'+str(file)))
		csv_reader_copy = csv.reader(open('Try2_output/'+str(file)))
		total_rows = len(list(csv_reader_copy))
		# print(total_rows)
		# if(total_rows>1000):
		# 	count += 1
		# 	# print(total_rows)
		# 	# summary_file.write('\n' + str(file) + '\n')
		# 	# for row in csv_reader:
		# 	# 	summary_file.write(row[0] + '\n')
		# 	print(file)
		if(total_rows<=1000 and total_rows>100):
			small_cluster_count += 1
			print(file)
	# break
	# print(str(file))
print(count)
print(small_cluster_count)