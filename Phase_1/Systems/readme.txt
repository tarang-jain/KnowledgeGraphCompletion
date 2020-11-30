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
This folder contains the following systems:

#############################################################

(a) Association Rule Mining

Contents:
--------------------------------------
	(a) apriori.py : Python implementation of the apriori algorithm. This code reads a transactional database file specified by the user 		and based on user's specified support and confidence values, frequent itemsets and association rules are generated.
	(b) DataSetx.txt : (x: 1,2,3,4,5) Five different dataset files containing transactions.


#############################################################

(b) C-Value-Term-Extraction

Contents:
--------------------------------------
This repository contains implementations of the term extraction algorithm (without filters) from "Automatic Recognition of Multi-Word Terms: the C-value/NC-value Method Katerina Frantziy, Sophia Ananiadouy, Hideki Mima"
The sample algorithm testing file 'Turku.txt' was tagged by Stanford CoreNLP to Part of Speech, which gave out 'Turku-tagged.txt'

#############################################################

(c) KG Population
	text_to_excel_populate.py - This file extracts class indivuduals from report data and puts in the excel sheet in a Cellfie acceptable structure.

	rules_to_populate.json - This file contains transformation rules that capture data from excel sheet and populate the knowledge graph in Protege using Cellfie plugin.
	
#############################################################

(d) Protege
	Protege Software to open the KG (the OWL/RDF/RDFS files)
	
#############################################################


(e) Sentence Clustering
	-- Code for sentence clustering based on sentence similarity. (the cosine similarity is used to compute the similarity of the sentences)
	
#############################################################


(f) tf-idf
	-- The code to TF-IDF values for terms present in reports.
	
#############################################################


(g) Web Scraping
	-- Codes present in this folder can be used to download the NTSB Aircraft Accident Reports automatically.
	
#############################################################


(h) Web Service
	-- This folder contains the code of the web service designed to query the KG
	
#############################################################
