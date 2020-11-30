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
=================================================
Abstract: 
=================================================
Every day more than 8 million people travel using ?ight. Safety is a prime
concern in the aviation feld. It is a challenging task to identify all the safety
measures for an aircraft to avoid an accident. The causes of aircraft accidents are often convoluted and tangled. There might be cascading causes
which resulted in an aircraft accident, but they remain obscure after an investigation by humans because of the inability of a person to spot the root
cause of the accident in a long chain of events following an accident. The
objective of the project is to derive intelligence and insights from 2 domains
– Investigation report domain and operations domain and identify areas of
opportunity to improve safety and performance. The scope of the project is
limited to civil aviation aerospace domain. These insights derived can result
in improvements in system design, operational procedures, improvement in
training methods and new mandates thereby enhancing overall safety in the
domain.
The project is in collaboration with Honeywell Technology Solutions Inc.
started in 2019. It is a 3-year project. To retrieve information from data
and enable automated reasoning, we decided to design Knowledge Graphs
(KG) of two domains. Currently, we have built the KG of aircraft accident
reports using data of US National Transportation Safety Board (NTSB). In
this report, the development of the aircraft accident KG is described. We
have started inspecting the aircraft safety manuals to get started with the
KG of aircraft manuals and operations.
#################################################


=================================================
Contents of the folder:
=================================================
1. Data :: Contains Aircraft Accident Reports scraped from NTSB website
(a) PDFs- contains pdf reports of accidents year and month wise.
(b) Texts - processed pdf reports in text format.
(c) Tokenized - Contains tokenized sentences from Texts folder.
(d) OntologyData2001-2018.xlsx - contains all instances for the classes of knowledge graph. This sheet is created by extracting the required information from the NTSB aircraft accident reports.


2. Documents :: contains the documentation of my MTP.
(a) Manual : contains the USER Manual and the PROGRAMMER's Manual for the systems developed during my MTP.
(b) Papers : contains the literature survey paper and the papers read during MTP.
(c) Reports : contains reports of MTP stage I and mtp stage II.
(d) Slides : contains slides from my presentations for stage I and stage II of MTP.

3. Knowledge Graph :: This folder contains the three ontology and knowledge graph files in OWL format for the this three -
(a) Aircraft Accidents : Ontology and KG for Aircraft Accidents 
(b) Aircraft Manuals : Ontology for Aircraft Safety Manuals
(c) Unit Ontology : Unit Ontology integrated with the Aircraft Accident KG



4. Systems: Contains the scripts which can be used to learn the components of knowledge graph
    (a) Entity Extraction: TF-IDF and C-Value
    (b) Relation Extraction: Association Rule Mining
    (c) Web Service to query KG
#################################################
The images are created using creately.com
################################################