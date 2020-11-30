from .nlqpy_new import *
def __init__(self):
    print(Welcome)
                #my_world = World()
                #onto_path.append(r"C:\\Users\\Qumar\\Desktop\\")
                #my_world.get_ontology("https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl").load()
                #self.graph = my_world.as_rdflib_graph()
def get_class(self,o,x):
    print(o)
    q_class="SELECT DISTINCT ?type WHERE {?subject a ?type . ?subject ?p rdf:"+o+"}"
    print(q_class)
    query1 = "base <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident> " \
            "PREFIX rdf: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> " \
            +q_class
                #query is being run
    resultsList = self.graph.query(query1)
    print(list(resultsList))
    h='type'
    response1=[]
    response1=query_exec(self,resultsList,h)
    return response1
    #return resultsList
                #print(response1)
                #if(query1==x):
                #       return response1

                #else:
                #        return ""

def get_objectclass(self,r):
    #r1=str(r)
    q_relations="SELECT DISTINCT ?type WHERE { ?p a ?type . ?subject rdf:"+r+" ?p }"
    print(q_relations)
    query3 = "base <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident> " \
            "PREFIX rdf: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> " \
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"\
            +q_relations
            #query is being run
    resultsList = self.graph.query(query3)
    #print(list(resultsList))
    h='type'
    response1=[]
    response1=query_exec(self,resultsList,h)
    #print(response1)
    return response1

def get_relations(self,re1):
    q_relations="SELECT ?label WHERE { ?subject rdfs:label ?label. FILTER(regex(?label, '^"+re1+"', 'i') ) }"
    print(q_relations)
    query2 = "base <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident> " \
            "PREFIX rdf: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> " \
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"\
            +q_relations
            #query is being run
    resultsList = self.graph.query(query2)
    #print(list(resultsList))
    h='label'
    response1=[]
    response1=query_exec(self,resultsList,h)
    #print(response1)
    return response1

def get_predicate(self,o,x):
    print(o)
    q_predicate="SELECT DISTINCT ?p WHERE { ?subject ?p rdf:"+o+" }"
    print(q_predicate)
    query1 = "base <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident> " \
            "PREFIX rdf: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> " \
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"\
            +q_predicate
                #query is being run
    resultsList = self.graph.query(query1)
    print(list(resultsList))
    h='p'
    response1=[]
    response1=query_exec(self,resultsList,h)

    return response1
        #resultsList=[]
#def searchq(self,query_line,x):
#    p = 'hasAircraftModel'

#   query = "base <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident> " \
#           "PREFIX rdf: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> " \
#            +query_line
                #query is being run
#    resultsList = self.graph.query(query)
#   h=x
#    response1=query_exec(self,resultsList,h)
#    print(response1) #just to show the output
#    print('\n\n')
#    return response1


                #creating json object
def query_exec(self,resultsList,h):
    response = []
    for item in resultsList:
        s = str(item[h].toPython())
        s = re.sub(r'.*#',"",s)
        #s = re.sub(r'^rdflib.term.Literal',"",s)

        #p = str(item['Seats'].toPython())
        #p = re.sub(r'.*#', "", p)

        #o = str(item['o'].toPython())
        #o = re.sub(r'.*#', "", o)
        #response.append({'s' : s, 'p' : p, "o" : o})
        response.append({s})
    return response
