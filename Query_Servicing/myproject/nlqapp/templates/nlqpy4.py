from owlready2 import *
import types
onto_path.append(r"/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II-20200816T091910Z-001/KG IMPRINT II")
onto = get_ontology("https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl").load()
onto.AircraftAccident
namespace=onto.get_namespace("http://www.cse.iitb.ac.in/~amitpatil/aircraft_sbase.owl#")
def search4(qu):
    Aircraft ="AircraftAccident."+ qu
    qp=' '
    qp1=''
    qp2=''

    with onto:
        l1=(list(onto.classes()))

    return l1
