import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from nltk.tokenize import sent_tokenize



def create_input(source_path):
	target_path = 'input'
	source_text_file = open(source_path, 'r').readlines()
	target_text_file = open(target_path, 'a+') 
	for line in source_text_file:
		target_text_file.write(line)

# create_input('2015_1_1')
# create_input('2015_1_2')

start_year = raw_input('Enter start year: ')
end_year = raw_input('Enter end year: ')
for i in range(int(start_year), int(end_year) + 1):
	for j in range(1, 13):
		text_files = os.listdir('Reports/Tokenized/' + str(i) + '/' + str(j))
		for text_file in text_files:
			source_path = './Reports/Tokenized/' + str(i) + '/' + str(j) + '/' + str(text_file)
			create_input(source_path)
		print('Conversion done for ' + str(j) + ' month of ' + str(i) + ' year')