import requests
from bs4 import BeautifulSoup


# Download all PDFs from the given page URLs
def fetch_urls(month, year):
	page_url = 'https://www.ntsb.gov/_layouts/ntsb.aviation/AccList.aspx?month=' + str(month) + '&year=' + str(year)
	r = requests.get(page_url)
	soup = BeautifulSoup(r.content, 'html.parser')
	links = soup.findAll('a')
	pdf_counter = 1
	for link in links:
		if(link.string=='PDF'):
			#print(link.get('href'))
			pdf_name =  'Reports/' + str(year) + '/' + str(month) + '/' + str(year) + '_' + str(month) + '_' + str(pdf_counter)
			download_pdf(link.get('href'), pdf_name)
			pdf_counter += 1




# Download PDF file from the given page URL
def download_pdf(pdf_url, pdf_name):
	#pdf_url = "https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID=20041008X01608&AKey=1&RType=Final&IType=CA"
	r = requests.get(pdf_url, stream = True)
	with open(pdf_name,"wb") as pdf:
	    for chunk in r.iter_content(chunk_size=1024):
	        if(chunk):
        		pdf.write(chunk)


start_year = input('Enter the start year: ')
end_year = input('Enter the end year: ')
year = start_year
for i in range(int(start_year), int(end_year) + 1):
	for j in range(1, 13):
		fetch_urls(j, i)
		print('Downloading completed for ' + str(j) + ' month of ' + str(i) + ' year')
