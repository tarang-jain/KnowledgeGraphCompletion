import PyPDF2 
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Converts pdf file to text given the month and year of the report
def convert_pdf_to_text(month, year):
	pdf_files = os.listdir('Reports' + '/' + str(year) + '/' + str(month))
	for pdf_file in pdf_files:
		pdf_object = open('Reports' + '/' + str(year) + '/' + str(month) + '/' + str(pdf_file), 'rb')
		pdf_reader = PyPDF2.PdfFileReader(pdf_object) 
		text_file = open('Text' + '/' + str(year) + '/' + str(month) + '/' + str(pdf_file), "a+")
		for i in range(pdf_reader.numPages):
			page_obj = pdf_reader.getPage(i) 
			text_file.write(page_obj.extractText())
			# print(page_obj.extractText())
 			# content = content + page_obj.extractText()
 		text_file.close()
		pdf_object.close() 

start_year = raw_input('Enter start year: ')
end_year = raw_input('Enter end year: ')
for i in range(int(start_year), int(end_year) + 1):
	for j in range(1, 13):
		convert_pdf_to_text(j, i)
		print('Conversion done for ' + str(j) + ' month of ' + str(i) + ' year')

