
city1 = "?city"
country1 = "?coutry"
RunwaySurface1 = "?RunwaySurface"
Aircraftmodel1 = "?Aircraftmodel"
Aircraft1 = "?Aircraft"
pilot1 = "?pilot"
print_variable1 = "?accident"
def make_query (print_variable, city, country, RunwaySurface, Aircraftmodel, agee):

	Prefix_1 = "PREFIX aircraftaccident: &lt;https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#&gt; "
	Prefix_2 = "PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; "

	

	if city != "":
		city1 = "Aircraftaccident:" + city

	if country != "":
		country1 = "Aircraftaccident:" + country

	if RunwaySurface != "":
		RunwaySurface1 = "Aircraftaccident:" + RunwaySurface
	
	if Aircraftmodel != "":
		Aircraftmodel1 = "Aircraftaccident:" + Aircraftmodel


	Sparql_Query = "SELECT ?" + print_variable + " WHERE { "

	Sparql_Query = Sparql_Query + "?accident aircraftaccident:occurredAtCity " + city1 + " . "                            + "?accident aircraftaccident:occurredAtCountry " + str(country1) + " . "                                         + "?accident aircraftaccident:hasAircraft " + Aircraft1 + " . "                                                   + "?Aircraft hasAircraftModel " + Aircraftmodel1 + " . "                                                          + "?accident hasPilot" + pilot1 + " . "                                                                           + pilot1 + " hasAge ?Age . "                                                                                      + "?accident hasRunwaySurfaceType " + RunwaySurface + " . "                                                       + "FILTER( ?Age >= " + agee + " && ?Age <= " + agee + " ) . " 


	Sparql_Query = Prefix_1 + " " + Prefix_2 + " " + Sparql_Query

	print (Sparql_Query)
	return Sparql_Query


# make_query ("accident", "miami", "hh", "concrete", "1825", "30")