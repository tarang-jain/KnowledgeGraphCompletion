import os
import re
#from importlib import reload
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from nltk.tokenize import sent_tokenize


# Tokenizes the report text corpus into the sentences
def sentence_tokenize(source_path, target_path):
	# print(source_path + ' ' + target_path)
	source_text_file = open(source_path, 'r').readlines()
	target_text_file = open(target_path, 'w')
	page_number_pattern = re.compile("Page [0-9]* of [0-9]*")
	footer_line = "The National Transportation Safety Board (NTSB), established in 1967"
	i = 0 
	while(i<len(source_text_file)):
		if(source_text_file[i].strip()=="Analysis"):
			break
		if(source_text_file[i].strip().endswith(':') and (i<len(source_text_file)-1 and (not source_text_file[i+1].strip().endswith(':')))):
			target_text_file.write(source_text_file[i].strip() + ' ' + source_text_file[i+1].strip() + '\n')
			i = i + 1
		elif(not page_number_pattern.match(source_text_file[i].strip())):
			target_text_file.write(source_text_file[i])	
		i = i + 1

	content = ""
	while(i<len(source_text_file)):
		if(footer_line in source_text_file[i]):
			break
		if(not page_number_pattern.match(source_text_file[i].strip())):
			content = content + ' ' + source_text_file[i].strip()
		i = i + 1	
	sentences = sent_tokenize(content)
	for sentence in sentences:
		words = sentence.split(' ')
		if(len(words)<50):
			target_text_file.write(sentence + '\n')

start_year = input('Enter start year: ')
end_year = input('Enter end year: ')
for i in range(int(start_year), int(end_year) + 1):
	for j in range(1, 13):
		text_files = os.listdir('Reports/Texts/' + str(i) + '/' + str(j))
		for text_file in text_files:
			source_path = './Reports/Texts/' + str(i) + '/' + str(j) + '/' +str(text_file)
			target_path = './Reports/Tokenized/' + str(i) + '/' + str(j) + '/' + str(text_file)
			sentence_tokenize(source_path, target_path)
		print('Conversion done for ' + str(j) + ' month of ' + str(i) + ' year')
