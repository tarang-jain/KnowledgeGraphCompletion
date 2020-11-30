from urllib.parse import quote
from urllib.request import urlopen
import requests
import json
import csv



# takes input fields, construct SPARQL Query from those fields, get results from the Fuseki API
def make_query (print_variable, city, country, RunwaySurface, Aircraftmodel, agee_min, agee_max, pilot_certificate, Aircraft_manufacturer, Engine_manufacturer):


	city1 = "?city"
	country1 = "?country"
	RunwaySurface1 = "?RunwaySurface"
	Aircraftmodel1 = "?Aircraftmodel"
	Aircraft1 = "?Aircraft"
	pilot1 = "?pilot"
	pilot_certificate1 = "?pilot_certificate"
	Aircraft_manufacturer1 = "?Aircraft_manufacturer"
	Engine_manufacturer1 = "?Engine_manufacturer"
	print_variable1 = "?accident"
	agee_min1 = "0"
	agee_max1 = "150"


	Prefix_1 = "PREFIX aircraftaccident: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> "
	Prefix_2 = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "

	

	if city != "":
		city1 = "aircraftaccident:" + city

	if country != "":
		country1 = "aircraftaccident:" + country

	if RunwaySurface != "":
		RunwaySurface1 = "aircraftaccident:" + RunwaySurface
	
	if Aircraftmodel != "":
		Aircraftmodel1 = "aircraftaccident:" + Aircraftmodel

	if pilot_certificate != "":
		pilot_certificate1 = "aircraftaccident:" + pilot_certificate

	if Aircraft_manufacturer != "":
		Aircraft_manufacturer1  = "aircraftaccident:" + Aircraft_manufacturer 

	if Engine_manufacturer != "":
		Engine_manufacturer1 = "aircraftaccident:" + Engine_manufacturer


	if agee_min != "":
		agee_min1 = agee_min

	if agee_max != "":
		agee_max1 = agee_max


	Sparql_Query = "SELECT ?" + print_variable + " WHERE { "

	# Make query
	Sparql_Query = Sparql_Query + "?accident aircraftaccident:occurredAtCity " + city1 + " . " + "?accident aircraftaccident:occurredAtCountry " + country1 + " . "                                         + "?accident aircraftaccident:hasAircraft " + Aircraft1 + " . "                                                          + "?accident aircraftaccident:hasPilot " + pilot1 + " . " + pilot1 + " aircraftaccident:hasAge ?Age . " + pilot1 + " aircraftaccident:hasCertificate " + pilot_certificate1 + " . " + "?Aircraft aircraftaccident:hasAircraftManufacturer " + Aircraft_manufacturer1 + " . " + "?Aircraft aircraftaccident:hasEngineManufacturer " + Engine_manufacturer1 + " . " + "?accident aircraftaccident:hasRunwaySurfaceType " + RunwaySurface1 + " . " + "FILTER( ?Age >= " + agee_min1 + " && ?Age <= " + agee_max1 + " ) . "
 #                                                   # + "?Aircraft hasAircraftModel " + Aircraftmodel1 + " . "
	Sparql_Query = Prefix_1 + " " + Prefix_2 + " " + Sparql_Query + "}"

	# Get results of the query
	Sparql_Query = find_results (Sparql_Query)

	return Sparql_Query
	




# Takes SPARQL query as a input and gives output of the query in ptocessed form 
def find_results (Sparql_Query):
	headers = {'Accept':'application/json'}

	# pass SPARQL Query to Fuseki API
	Sparql_Query = requests.get("http://localhost:3030/Accident_2/?query=" + quote(Sparql_Query), headers=headers).text
	

	# Process JSON LD format
	result = json.loads(Sparql_Query.replace('\'','"'))
	accident_number = []
	out = "";

	count = 0
	for i in range(len(result['results']['bindings'])):
		count += 1
		accident_number.append(result['results']['bindings'][i]['accident']['value'].split("#")[1]);
	print (count)
	text = "<ul>";
	for i in range(len(result['results']['bindings'])):
		text += "<li>" + accident_number[i] + "</li>";
	
	text += "</ul>";

	return text
