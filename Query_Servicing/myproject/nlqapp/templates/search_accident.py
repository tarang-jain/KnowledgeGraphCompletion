from .nlqpy_new import *
#def __init__(self):
        #my_world = World()
        #onto_path.append(r"C:\\Users\\Qumar\\Desktop\\")
        #my_world.get_ontology("https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl").load()
        #self.graph = my_world.as_rdflib_graph()
def searchq(self,query_line,x):
        p = 'hasAircraftModel'
        #query_line = query
        #Search query is given here
        #Base URL of your ontology has to be given here
        #rdf = URIRef('https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident#')
        query = "base <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident> " \
                "PREFIX rdf: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> " \
                +query_line
        #query is being run
        resultsList = self.graph.query(query)
        h=x

        #creating json object
        response = []
        for item in resultsList:
            s = str(item[h].toPython())
            s = re.sub(r'.*#',"",s)

            #p = str(item['Seats'].toPython())
            #p = re.sub(r'.*#', "", p)

            #o = str(item['o'].toPython())
            #o = re.sub(r'.*#', "", o)
            #response.append({'s' : s, 'p' : p, "o" : o})
            response.append({h : s})

        print(response)
        print('\n\n')
        return response
        #return list(resultsList)
