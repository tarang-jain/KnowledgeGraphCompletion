==================================
Submitted by: 
Dhaval Limdiwala (173050061)
Amit Patil (173050009)
M.Tech. CSE, IIT Bombay
Project Guide :- Prof. Pushpak Bhattacharyya
Project Title :- Information Retrieval via Knowledge Graphs Developed for Aircraft Accidents Database and Aircraft Manuals

Email Address :- 
dhaval.limdiwala@gmail.com
patil.amit155@gmail.com
Contact number:- 9727252446


#############################################################
This folder contains code for downloading NTSB Aircraft Accident Reports and preprocess the reports.
#############################################################

	-NTSB reports can be found on https://www.ntsb.gov/Pages/default.aspx
	-run "python3 download_pdfs.py" to download all pdf reports from the NTSB website.
	-run "python3 pdf_to_text.py" to convert all pdf reports into plain text files.
	-run "python3 sentence_tokenize.py" to tokenize the plain text report file into the file with every sentence as one token
	- beautifulsoup python library is used to extract the reports from the web.


