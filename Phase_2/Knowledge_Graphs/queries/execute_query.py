from owlready2 import *
import pickle

default_world.get_ontology("/home/tarangjain/KG_IMPRINT_II/TARANG/Knowledge_Graphs_rough/aircraft_base.owl").load()
onto = default_world.get_ontology("/home/tarangjain/KG_IMPRINT_II/TARANG/Knowledge_Graphs_rough/AircraftAccidentEvent_merged.owl").load()

graph = default_world.as_rdflib_graph()
strin = "IN_FLIGHT_COLLISION_WITH_OBJECT_-_BIRD\(S\)"
r = list(graph.query("""SELECT ?accident\nWHERE {?accident ?EventType <http://www.semanticweb.org/tarangjain/ontologies/AircraftAccident_merged.owl#IN_FLIGHT_COLLISION_WITH_OBJECT_-_BIRD(S)>\n}"""))

print(r)
